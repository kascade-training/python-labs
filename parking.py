class Parking:
    def __init__(self, Address, Capacity,PlaceOccup, Nportal):
        assert isinstance(Address, str)
        assert isinstance(Capacity, int) and Capacity > 0
        assert isinstance(PlaceOccup, int) and PlaceOccup >= 0
        assert isinstance(Nportal, int) and Nportal > 0
        
        self.Address = Address
        self.Capacity = Capacity
        self.PlaceOccup = PlaceOccup
        self.Nportal = Nportal
     
    def full(self):
        if self.Capacity == self.PlaceOccup
            return True
     
    def enter(self):
        if not self.full():
            self.PlaceOccup += 1
        else : Exception
         
    def out(self):
        self.PlaceOccup -= 1        
            
        
class Portail:
    def __init__(self, numPortail,Parking):
        assert isinstance(numPortail, int)
        assert isinstance(parking, Parking)
        
        self.numPortail = numPortail
        self.parking = parking
        
    