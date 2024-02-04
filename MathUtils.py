class MathUtils:
    def __init__(self):
        self.x=5
        self.y=0
    
    def add(self):
        return self.x+self.y
    
    def substract(self):
        return self.x-self.y
    
    def times(self):
        return self.x*self.y

    def divide(self):
        if(self.y==0):
            return -1.0
        return self.x/self.y
    
    def checkType(self):
        return "x= "+str(type(self.x))+" y= "+str(type(self.y))
    
    def print(self):
        return "x= "+str(self.x)+" y= "+str(self.y)
    
'''o=MathUtils()
print(o.checkType())'''
    
