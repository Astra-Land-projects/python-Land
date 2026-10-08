class Character:
  def __init__(self, name, level, attack_power, heal_power):
    self.name = name
    self.level = level
    self.max_hp = 100
    self.current_hp = 100
    self.attack_power = attack_power
    self.heal_power = heal_power

  def __str__(self):
    return "character name: " + self.name + " | " + "character hp: " + str(self.current_hp)

  def heal(self):
    if self.current_hp == 0:
      return

    if self.current_hp >= 95:
      self.current_hp = self.max_hp
    else:
      self.current_hp += self.heal_power
   
  def attack(self, other):
    if other.current_hp == 0:
      return

    if other.current_hp <= self.attack_power:
      other.current_hp = 0
    else:
      other.current_hp -= self.attack_power

# ساخت دو کاراکتر بازی
wizard = Character("Oz", 20, 12, 15)
tank = Character("Ghul", 17, 15, 3)

# معرفی هر کاراکتر
print(wizard)
print(tank)

# حمله کاراکتر اول به کاراکتر دوم و کاهش جون این کاراکتر
wizard.attack(tank)
print(tank)