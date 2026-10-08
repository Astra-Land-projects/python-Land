import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# ------------------------------------------------------------
# بخش دیتابیس
# ------------------------------------------------------------
DB_NAME = "expenses.db"

def init_db():
    """ایجاد جدول هزینه‌ها اگر وجود نداشت."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expense (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_expense(date, category, amount, note):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expense (date, category, amount, note) VALUES (?,?,?,?)",
        (date, category, amount, note)
    )
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, date, category, amount, note FROM expense ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_by_month(year_month):
    """دریافت هزینه‌ها برای ماهی خاص به فرم YYYY-MM"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "SELECT id, date, category, amount, note FROM expense "
        "WHERE date LIKE ? ORDER BY date DESC",
        (f"{year_month}%",)
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM expense WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()

# ------------------------------------------------------------
# بخش واسط گرافیکی
# ------------------------------------------------------------
class ExpenseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("مدیریت هزینه‌ها")
        self.geometry("720x500")
        self.resizable(False, False)

        self.create_widgets()
        self.refresh_table()

    def create_widgets(self):
        # فرم افزودن هزینه
        frm = ttk.LabelFrame(self, text="ثبت هزینه جدید")
        frm.pack(fill="x", padx=10, pady=5)

        ttk.Label(frm, text="تاریخ (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ent_date = ttk.Entry(frm, width=15)
        self.ent_date.grid(row=0, column=1, padx=5, pady=5)
        self.ent_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

        ttk.Label(frm, text="دسته‌بندی:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.ent_category = ttk.Entry(frm, width=15)
        self.ent_category.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frm, text="مبلغ:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.ent_amount = ttk.Entry(frm, width=10)
        self.ent_amount.grid(row=0, column=5, padx=5, pady=5)

        ttk.Label(frm, text="یادداشت:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ent_note = ttk.Entry(frm, width=60)
        self.ent_note.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky="w")

        btn_add = ttk.Button(frm, text="اضافه کردن", command=self.on_add)
        btn_add.grid(row=0, column=6, rowspan=2, padx=10, pady=5)

        # جدول هزینه‌ها
        tbl_frame = ttk.Frame(self)
        tbl_frame.pack(fill="both", expand=True, padx=10, pady=5)

        cols = ("id", "date", "category", "amount", "note")
        self.tree = ttk.Treeview(tbl_frame, columns=cols, show="headings", selectmode="browse")
        self.tree.heading("id", text="شناسه")
        self.tree.heading("date", text="تاریخ")
        self.tree.heading("category", text="دسته")
        self.tree.heading("amount", text="مبلغ")
        self.tree.heading("note", text="یادداشت")
        for c in cols:
            self.tree.column(c, anchor="center")
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tbl_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscroll=scrollbar.set)

        # بخش فیلتر ماهانه و مجموع
        bottom = ttk.LabelFrame(self, text="پیلن‌گذاری و مجموع")
        bottom.pack(fill="x", padx=10, pady=5)

        ttk.Label(bottom, text="ماه (YYYY‑MM):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ent_month = ttk.Entry(bottom, width=12)
        self.ent_month.grid(row=0, column=1, padx=5, pady=5)
        self.ent_month.insert(0, datetime.now().strftime("%Y-%m"))

        btn_filter = ttk.Button(bottom, text="فیلتر", command=self.on_filter)
        btn_filter.grid(row=0, column=2, padx=5, pady=5)

        btn_show_all = ttk.Button(bottom, text="نمایش همه", command=self.refresh_table)
        btn_show_all.grid(row=0, column=3, padx=5, pady=5)

        btn_delete = ttk.Button(bottom, text="حذف مورد انتخاب‌شده", command=self.on_delete)
        btn_delete.grid(row=0, column=4, padx=5, pady=5)

        self.lbl_total = ttk.Label(bottom, text="مجموع: 0")
        self.lbl_total.grid(row=0, column=5, padx=10, pady=5, sticky="e")

    # --------------------------------------------------------
    # رویدادها
    # --------------------------------------------------------
    def on_add(self):
        date = self.ent_date.get().strip()
        category = self.ent_category.get().strip()
        amount_text = self.ent_amount.get().strip()
        note = self.ent_note.get().strip()

        # اعتبارسنجی ساده
        if not (date and category and amount_text):
            messagebox.showwarning("خطا", "فیلدهای تاریخ، دسته‌بندی و مبلغ الزامی‌اند.")
            return
        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showwarning("خطا", "مبلغ باید عددی معتبر باشد.")
            return

        try:
            # اطمینان از فرمت تاریخ
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("خطا", "فرمت تاریخ باید YYYY-MM-DD باشد.")
            return

        add_expense(date, category, amount, note)
        self.refresh_table()
        self.clear_form()

    def clear_form(self):
        self.ent_category.delete(0, tk.END)
        self.ent_amount.delete(0, tk.END)
        self.ent_note.delete(0, tk.END)
        self.ent_date.delete(0, tk.END)
        self.ent_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

    def refresh_table(self):
        """نمایش تمام ردیف‌ها"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        rows = fetch_all()
        total = 0.0
        for r in rows:
            self.tree.insert("", tk.END, values=r)
            total += r[3]  # مقدار ستون amount

        self.lbl_total.config(text=f"مجموع: {total:,.2f}")

    def on_filter(self):
        ym = self.ent_month.get().strip()
        try:
            datetime.strptime(ym, "%Y-%m")
        except ValueError:
            messagebox.showwarning("خطا", "فرمت ماه باید YYYY-MM باشد.")
            return

        for row in self.tree.get_children():
            self.tree.delete(row)

        rows = fetch_by_month(ym)
        total = 0.0
        for r in rows:
            self.tree.insert("", tk.END, values=r)
            total += r[3]

        self.lbl_total.config(text=f"مجموع: {total:,.2f}")

    def on_delete(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("حذف", "هیچ ردیفی انتخاب نشده است.")
            return
        item = self.tree.item(sel)
        expense_id = item["values"][0]
        if messagebox.askyesno("حذف", f"آیا مطمئنید که می‌خواهید هزینهٔ شناسه {expense_id} حذف شود؟"):
            delete_expense(expense_id)
            self.refresh_table()

# ------------------------------------------------------------
# نقطهٔ ورود برنامه
# ------------------------------------------------------------
if __name__ == "__main__":
    init_db()
    app = ExpenseApp()
    app.mainloop()
    #کتابخانه می خوهد