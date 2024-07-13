class Car:
    def __init__(self, name: str, type: str, cost: int = 4000, production_year: int = 2024) -> None:
        self.name = name
        self.type = type
        self.cost = cost
        self.p_year = production_year

    def get_info(self):
        return f"""
    Name: {self.name}
    Type: {self.type}
    Cost: {self.cost}
    Year produced: {self.p_year}
"""
    
c1 = Car('Suberban', 'SUV', 200000, 2022)
c2 = Car('Tesla Model S', 'Sedan', 90000, 2023)
c3 = Car('Ford Mustang', 'Coupe')
c4 = Car('Honda Civic', 'Sedan', 25000, 2024)
c5 = Car('Chevrolet Tahoe', 'SUV', 65000, 2022)
c6 = Car('BMW X5', 'SUV', 75000, 2023)
c7 = Car('Porsche 911', 'Coupe', 120000, 2024)
c8 = Car('Audi Q7', 'SUV', 70000, 2023)
c9 = Car('Mazda MX-5 Miata', 'Convertible', 30000, 2020)
c10 = Car('Toyota Camry', 'Sedan', 28000, 2023)

lst = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

lst.sort(key= lambda x: x.p_year)

for i in lst:
    print(i.get_info())