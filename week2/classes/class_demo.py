# Structure

class Bottle:
    x = 0
    y= 1

    def __init__(self, turn_direction):
        print("Bottle.. initializing.... ")
        self.turn_cap = turn_direction

    def open_cap(self): #member func
        print("Address of self:", id(self))
        print("Opening cap..")
        print("Turn cap to: ",self.turn_cap)
    
    def shape(self):
        raise NotImplementedError


bottle_pepsi = Bottle("right")
bottle_pepsi.open_cap()

#bottle_pepsi.shape()
#bottle_pepsi.new_var = 89
#print(dir(bottle_pepsi))

bottle_cola = Bottle("left")
bottle_cola.open_cap()
#print(dir(bottle_cola))

#print("Address of bottle_pepsi:", id(bottle_pepsi))


# member functions
# the 'self' object, id(self) and the id(obj)
# Inheritance

class GlassBottle(Bottle): #inheritance
    def __init__(self, turn_direction):
        super().__init__(turn_direction)
        self.turn_cap = turn_direction
        print("GlassBottle, opens ", self.turn_cap)

    def open_cap(self): #member func
        print("Upside..")

    def shape(self):
        print("Shape is oval")

g = GlassBottle("right")
print("------")
print(dir(g), type(g))
g.open_cap()
g.shape()
# Polymorphism
# Encapsulation
# Abstraction