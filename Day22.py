# Super() = Function used to give access to the methods of a parent class
#           Return a temporary object of a parent class when used.


class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width
class Square(Rectange):
  def __init__(self,length,width):
    super().__init__(length,width)
  def area(self):
    return self.length* self.width
class Cube(Rectangle):
  def __init__(self,length,width):
    super().__init__(length,width)
    self.height=height
  def volume(self):
    return self.length* self.width* self.height
square=Square(3,3)
cube=Cube(3,3,3)
print(square.area())         # 9
print(cube.volume())         # 27
