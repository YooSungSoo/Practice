class FourCal:

    def __init__(self,first,second):
        self.first = first
        self.second = second

    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
       result =  self.first + self.second
       return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a=FourCal()
b=FourCal()
a.setdata(4,2)
b.setdata(6,3)

print(a.add(),a.sub(),a.mul(),a.div())
print(b.add(),b.sub(),b.mul(),b.div())