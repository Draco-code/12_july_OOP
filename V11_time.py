class Time:
    def checkValidness(self, hour: int = 1, minut: int = 1, second: int = 1):
        try: 
            if 0 > hour or hour > 23 or 0 > minut or minut > 59 or 0 > second or second > 59:
                raise ValueError(f"Wrong Time Format! [{hour}:{minut}:{second}]")
            
        except ValueError as Error:
            print(Error)
            return -1 
        else:
            return 0
    
    def __init__(self, hour: int, minut: int, second: int) -> None:
        if not self.checkValidness(hour, minut, second):
            self.hour = hour
            self.minut = minut
            self.second = second

    def get_hour(self):
        return self.hour
    def get_minut(self):
        return self.minut
    def get_second(self):
        return self.second
    
    def set_hour(self, new_hour: int):
        if not self.checkValidness(hour= new_hour):
            self.hour = new_hour
    def set_minut(self, new_minut: int):
        if not self.checkValidness(minut= new_minut):
            self.minut = new_minut
    def set_second(self, new_second: int):
        if not self.checkValidness(second= new_second):
            self.second = new_second

    def set_time(self, new_hour: int, new_minut: int, new_second: int):
        if not self.checkValidness(hour= new_hour, minut=new_minut, second=new_second):
            self.hour = new_hour
            self.minut = new_minut
            self.hour = new_second

    def toString(self):
        return "%02d:%02d:%02d"%(self.get_hour(), self.get_minut(), self.get_second())
    
    def nextSecond(self):
        if self.second +1 == 60:
            if self.minut + 1 == 60:
                if self.hour +1 == 24:
                    return "00:00:00"
                else:
                    return "%02d:00:00"%(self.hour +1)    
            else: 
                return "%02d:%02d:00"%(self.hour, self.minut+1)
        else:
            return "%02d:%02d:%02d"%(self.hour, self.minut, self.second+1)

    def previousSecond(self):
        if self.second -1 == -1:
            if self.minut -1 == -1:
                if self.hour -1 == -1:
                    return "23:59:59"
                else:
                    return "%02d:59:59"%(self.hour -1)    
            else: 
                return "%02d:%02d:59"%(self.hour, self.minut-1)
        else:
            return "%02d:%02d:%02d"%(self.hour, self.minut, self.second-1)
        
t1 = Time(0, 1, 0)
print(t1.previousSecond())