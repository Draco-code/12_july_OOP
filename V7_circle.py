from math import pi

class Circle:
    def __init__(self, radius : float = 0, color : str = "White") -> None:
        "Aylanaga tegishli klass"
        self.radius = radius
        self.color = color

    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color
        return f'Current color: {self.color}'
    
    def area(self):
        return round(pi*self.radius**2, ndigits=2)

    def get_circumference(self):
        return round(2*pi*self.radius, ndigits=2)

    
    def __str__(self) -> str:
        return f"""    
    Radius: {self.get_radius()}
    Color: {self.color}
    Area: {self.area()}
    Circumference: {self.get_circumference()}
"""
    

c1 = Circle(4, 'Green')
print(c1)