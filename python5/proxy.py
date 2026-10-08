import socket
import select
import struct

# تنظیمات آدرس و پورت پروکسی
HOST = '127.0.0.1'  # localhost
PORT = 1080         # پورت استاندارد SOCKS5

def handle_client(client_socket):
    try:
        # ۱. مرحله Handshake (مذاکره اولیه)
        # دریافت نسخه و روش‌های احراز هویت
        version, nmethods = struct.unpack("!BB", client_socket.recv(2))
        methods = client_socket.recv(nmethods)

        # پاسخ به کلاینت: انتخاب روش بدون نیاز به رمز عبور (0x00)
        client_socket.sendall(struct.pack("!BB", 5, 0))

        # ۲. مرحله Request (دریافت آدرس مقصد)
        version, cmd, _, address_type = struct.unpack("!BBBB", client_socket.recv(4))

        if cmd != 1:  # فقط از دستور CONNECT پشتیبانی می‌کنیم
            client_socket.close()
            return

        # تشخیص نوع آدرس مقصد (IPv4, Domain Name, IPv6)
        if address_type == 1:    # IPv4
            remote_host = socket.inet_ntoa(client_socket.recv(4))
        elif address_type == 3:  # Domain Name
            domain_length = ord(client_socket.recv(1))
            remote_host = client_socket.recv(domain_length).decode('utf-8')
        else:
            client_socket.close()
            return

        remote_port = struct.unpack("!H", client_socket.recv(2))[0]

        # ۳. اتصال پروکسی به سرور مقصد
        try:
            remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_socket.connect((remote_host, remote_port))
           
            # ارسال پاسخ موفقیت‌آمیز به کلاینت (0x00 = Success)
            bind_address = remote_socket.getsockname()
            reply = struct.pack("!BBBBIH", 5, 0, 0, 1,
                                struct.unpack("!I", socket.inet_aton(bind_address[0]))[0],
                                bind_address[1])
            client_socket.sendall(reply)
            print(f"[+] تونل برقرار شد: -> {remote_host}:{remote_port}")

        except Exception as e:
            # ارسال پاسخ خطا در صورت عدم اتصال به مقصد
            reply = struct.pack("!BBBBIH", 5, 1, 0, 1, 0, 0)
            client_socket.sendall(reply)
            client_socket.close()
            return

        # ۴. رد و بدل کردن داده‌ها بین کلاینت و مقصد (Relay Data)
        sockets = [client_socket, remote_socket]
        while True:
            readable, _, _ = select.select(sockets, [], [])
            if client_socket in readable:
                data = client_socket.recv(4096)
                if not data: break
                remote_socket.sendall(data)

            if remote_socket in readable:
                data = remote_socket.recv(4096)
                if not data: break
                client_socket.sendall(data)

    except Exception as e:
        pass
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(100)
    print(f"==================================================")
    print(f"[🚀] پروکسی SOCKS5 روی آدرس {HOST}:{PORT} فعال شد!")
    print(f"==================================================")

    while True:
        client_socket, addr = server.accept()
        # پردازش هر اتصال
        handle_client(client_socket)

if __name__ == '__main__':
    main()