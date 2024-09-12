class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*self.radius**2
    
    def peremeter(self):
        return (22/7)*self.radius*2
    
are1=Circle(21)
print(are1.area())
print(are1.peremeter())