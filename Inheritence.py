class University:
    def __init__(self,depart,year):
        self.depart = depart
        self.year = year

class Student(University):
    def __init__(self,depart,year,name,roll,ispaid):
        super().__init__(depart,year)
        self.name = name
        self.roll = roll
        self.ispaid =ispaid

s1 = Student("CS",2024,"Rohit sharma",62,True)
s2= Student("CIS",2025,"Tilak Verma",32,False)

print(f"{s1.name} {s1.roll} {s1.depart} {s1.year} {s1.ispaid}")
print(s2.name)
