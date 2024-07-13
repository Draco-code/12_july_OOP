class Rectangle: 
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def get_height(self):
        return self.height
    def get_width(self):
        return self.width
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def set_height(self, new_height: int):
        self.height = new_height
        return self.height
    def set_width(self, new_width: int):
        self.width = new_width
        return self.width
    
    def get_info(self):
        return f"""
    Height: {self.height}
    Width: {self.width}
    Area: {self.get_area()}
    Perimeter: {self.get_perimeter()}
"""
    
r1 = Rectangle(4, 5)
print(r1.get_info())