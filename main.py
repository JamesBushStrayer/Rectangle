class Rectangle:
  def __init__(self, width, height):
      self.width = int(width)
      self.height = int(height)

  def calculate_perimeter(self):
      return 2 * (self.width + self.height)

  def calculate_area(self):
      return self.width * self.height

  def draw(self):
      for row in range(self.height):
          if row == 0 or row == self.height - 1:
              print('*' * self.width)
          else:
              print('*' + ' ' * (self.width - 2) + '*')

  def display(self):
      print("Rectangle Width: {}".format(self.width))
      print("Rectangle Height: {}".format(self.height))
      print("Area: {}".format(self.calculate_area()))
      print("Perimeter: {}".format(self.calculate_perimeter()))
      print("\nDrawing of the rectangle:")
      self.draw()

def main():
  width = float(input("Enter the width of the rectangle: "))
  height = float(input("Enter the height of the rectangle: "))

  rect = Rectangle(width, height)
  rect.display()

if __name__ == "__main__":
  main()
