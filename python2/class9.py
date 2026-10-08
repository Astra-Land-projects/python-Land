class A:
  def __init__(self):
    print("Hello from A")

class B(A):
  def __init__(self):
    super().__init__()
    print("Hello from B")


b = B()