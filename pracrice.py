class FourCal:

    def __init__(self,first,second): #생성자
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

class MoreFourCal(FourCal): #FourCal Class 상속

    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal): #FourCal Class 상속

    def div(self):  #오버라이딩 / 덮어쓰기 / 덮어쓴 메서드가 호출됨
        if self.second == 0:    
            return 0
        else : 
            return self.first / self.second

a=FourCal(4,2)
b=FourCal(6,3)
print(a.add(),a.sub(),a.mul(),a.div())
print(b.add(),b.sub(),b.mul(),b.div())
c=MoreFourCal(10,5)
print(c.pow())
d=SafeFourCal(3,0)
print(d.div())