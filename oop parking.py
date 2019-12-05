
class Parking:
    def __init__(self, adresse, capacitéacceuil, nombreportail):
        assert isinstance(adresse,str) and len(adresse)>0
        assert isinstance(capacitéacceuil,int) and capacitéacceuil>0
        assert isinstance(nombreportail,int) and nombreportail>0
        self.adr = adresse
        self.capacity = capacitéacceuil
        self.nbrportail = nombreportail
        self.lPortails = []
        for i in range(self.nbrportail):
            self.lPortails.append(Portail(i, 100))
class Portail:  
    
    def __init__(self, numportail, nbrpl, nbrentréé=0, nbrsortie=0):
        assert isinstance(numportail,int) and numportail>=0
        assert isinstance(nbrpl,int) and nbrpl>=0
        assert isinstance(nbrentréé,int) and nbrentréé>=0
        assert isinstance(nbrsortie,int) and nbrsortie>=0
        self.nump = numportail
        self.nbrpl = nbrpl
        self.nbrentréé = nbrentréé
        self.nbrsortie = nbrsortie
    def __str__ (self): 
        return str(self.nump)

def main():

    monparking = Parking ("avenue x", 100, 10)
    print(monparking.lPortails[0])

    
if __name__ == "__main__":
    main()



