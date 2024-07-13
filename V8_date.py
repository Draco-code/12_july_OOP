class Date: 
    def checkValidness(self, month: int = 1, day: int = 1, year: int = 1):
        try: 
            if 0 > month or month > 12 or 0 > day or day > 32:
                raise ValueError(f"Wrong Date Format! [{day}.{month}.{year}]")
            
        except ValueError as Error:
            print(Error)
            return -1 
        else:
            return 0

    def __init__(self, year: int, month: int, day: int) -> None:
        if not self.checkValidness(month, day, year):
            self.year = year
            self.month = month
            self.day = day
        
    def get_day(self):
        return self.day
    
    def get_month(self):
        return self.month
    
    def get_year(self):
        return self.year
    
    def set_day(self, new_day: int):
        if not self.checkValidness(day=new_day):
            self.day = new_day
            return self.day
        
    def set_month(self, new_month: int):
        if not self.checkValidness(month=new_month):
            self.month = new_month
            return self.month
    
    def set_year(self, new_year: int):
        self.year = new_year
        return self.year
    
    def set_date(self, new_day: int, new_month: int, new_year: int):
        if not self.checkValidness(new_month, new_day, new_year):
            self.day = new_day
            self.month = new_month
            self.year = new_year

    def toString(self):
        return "%02d/%02d/%d"%(self.day, self.month, self.year)

    def __str__(self) -> str:
        return f"""
    Year: {self.year}
    Month: {self.month}
    Day: {self.day}
"""
    
d = Date(2006, 7, 26)
# d.set_date(3000, 70, 43)
print(d.toString())