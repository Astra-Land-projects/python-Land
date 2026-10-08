class ChatBot:
  def __init__(self, name, version):
    self.name = name
    self.version = version

  def introduce(self):
    print(self.name + " - " + self.version)


class NeoBot(ChatBot):
  def __init__(self, name, version, language_support):
    super().__init__(name, version)
    self.language_support = language_support

  def interact(self):
    print(self.name + ": آماده‌ی پاسخ دادن به سوالات شما هستم! (پشتیبانی از " + str(self.language_support) + " زبان)")


class ZetaTalk(ChatBot):
  def __init__(self, name, version, humor_level):
    super().__init__(name, version)
    self.humor_level = humor_level

  def interact(self):
    if self.humor_level > 7:
      print(self.name + ": آماده‌ باش که قراره کلی شوخی باحال یاد بگیری")
    else:
      print(self.name + ": یه شوخی کوچولو بلدم، ولی خیلی خفن نیست!")


# ساخت لیست برای ذخیره چت‌بات‌ها
chatbots = []

# ساخت نمونه‌هایی از چت‌بات‌ها
neobot = NeoBot("NeoBot", "2.5", 60)
zetatalk = ZetaTalk("ZetaTalk", "1.0", 9)

# اضافه کردن چت‌بات‌ها به لیست
chatbots.append(neobot)
chatbots.append(zetatalk)

# معرفی چت‌بات‌ها
print("معرفی چت‌بات‌های موجود:")
for bot in chatbots:
  bot.introduce()

print("شروع ارتباط با چت‌بات‌ها:")

# تعامل با چت‌بات‌ها
for bot in chatbots:
  bot.interact()