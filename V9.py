class Employee:
    def __init__(self, id: int, firstName: str, lastName: str, salary: int) -> None:
        self.id = id
        self.firstN = firstName.title()
        self.lastN = lastName.title()
        self.salary = salary

    def get_id(self):
        return self.id
    def get_firstName(self):
        return self.firstN
    def get_lastName(self):
        return self.lastN
    def get_fullName(self):
        return f'{self.firstN} {self.lastN}'
    def get_salary(self):
        return self.salary
    def getAnnualSalary(self):
        return self.salary * 12
    
    def set_salary(self, new_salary: int):
        self.salary = new_salary
    
    def raiseSalary(self, by_percent: int):
        self.salary = round(self.salary * (1 + by_percent/100), ndigits=2)
        return self.salary
    
    def toString(self):
        return f"Employee[id: {self.id}, name: {self.get_fullName()}, salary: ${self.salary}]"


u = Employee(1234, 'asadulloh', 'yusuf', 100)

print(u.raiseSalary(14.5679))
print(u.toString())
