# Noah Preston , CSC-231-001

class FootMeasure:
    def __init__(self, feet = 0, inches = 0):
        total_inches = feet * 12 + inches
        self.feet = total_inches // 12
        self.inches = total_inches % 12

    def __str__(self):
        if self.inches == 0:
            return f"{self.feet} feet."
        else:
            return f"{self.feet} feet. {self.inches} inches."
        
    def __add__(self, other):
        total_inches = (self.feet * 12 + self.inches) + (other.feet * 12 + other.inches)
        return FootMeasure(inches = total_inches) 
    
    def __eq__(self, other):
        return self.feet == other.feet and self.inches == other.inches
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return (self.feet * 12 + self.inches) < (other.feet * 12 + other.inches)
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)
    
