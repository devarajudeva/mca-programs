class car:
     name="cars"
     def __init__(self,name,mileage,price,color):
        self.name=name
        self.mileage=mileage
        self.price=price
        self.color=color
class super(car):
    pass
class base(car):
    pass
c1=super("super mk4",1050000,"black")
c2=base("base m4",1550000,"white")