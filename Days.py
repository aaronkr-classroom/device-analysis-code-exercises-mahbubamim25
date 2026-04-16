# SayDays.py

class SayDays:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
        
    def is_leap(self) -> bool:
        y = self.year
        
        return (
            (y % 4 ==0 and y % 100 !=0) or
            (y % 400 == 0)
        )
    
    def days(self):
        # From Jan 1, how many days untill now?
        days_in_month = [
            31, 29 if self.is_leap() else 28, 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31
            ] # 31 + 28 = 59 + 31 = 90 + 16 = 115
        
        total = 0
        m = 0 #0th month = january
        
        
        while m < self.month - 1: # 0 < 4
            total += days_in_month[m]
            m += 1
            
        total += self.day
        return total
        
    def days_left(self)-> int:
        # Until Dec 31, how many days left?
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days() # not 16th, but
        
    def weekday(self) -> int:
        
        y = self.year
        m = self.month
        d = self.day
        
        if m < 3:
            m += 12
            y -= 1
        
        K = y % 100
        J = y // 100
        
        h = (d + (13 * (m + 1)) //
             5 + K + K // 4 + J // 4 + 5 * J) % 7
        
        
        return h # 5 = thusday
        
    def weekday_name(self) -> str:
        
        names = [
            "saturday", "sunday", "monday", "tuesday",
            "wednesday", "thusday", "friday"
            ]
        return names[self.weekday()]
    
    
while True:
    year = int(input("what year is it? "))
    month = int(input("what month is it? "))
    day = int(input("what day is it? "))
    
    date= SayDays(year, month, day)
    
    print("days after jan 1: ", date.days())
    print("days after dec 31: ", date.days_left())
    print("numeric day of the week : ", date.weekday())
    print("english day of the week: ", date.weekday_name())
    