class Student:
  def __init__(self, name, grade, major):
    self.name = name             
    self.grade= grade           
    self.major = major

  def show_info(self):
    print("نام:", self.name)
    print("معدل:", self.grade)
    print("رشته تحصیلی:", self.major)


student1 = Student("Sara", 19, "Math")
student1.show_info()

