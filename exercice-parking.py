class Parking:
    def __init__(self, adr, cap, nbPort, portes=[]):
        assert isinstance(adr,str) and len(adr)>0
        assert isinstance(cap, int) and cap > 0
        assert isinstance(nbPort, int) and nbPort >0
        self.adr=adr
        self.cap=cap
        self.nbPlacesOcc=0
        self.mports=portes
        for i in range(nbPort):
            self.mports.append(Portail(i, self))

    def getNbPort(self):
        return len(self.mports)
    
    def full(self):
        return(self.nbPlacesOcc==self.cap)
    
    def getPort(self, port):
        if port>0 and port < self.getNbport():
            return(self.mports[port])
        else:
            raise Exception

    def enter(self):
        if not self.full():
            self.nbPlacesOcc += 1
            #Mettre à jour l'affichage
            self.afficher()
        else:
            raise Exception

    def out(self):
        self.nbPlacesOcc -= 1
        self.afficher()

    def placesLibres(self):
        return(self.cap - self.nbPlacesOcc)
    
    def afficher(self):
        for i in range(len(self.mports)):
            self.mports[i].afficher()

class Portail:
    def __init__(self, num, parking):
        assert isinstance(parking, Parking)
        assert isinstance(num, int) and num >= 0

        self.parking=parking
        self.num=num
        self.nbEntree=0
        self.nbSortie=0
    
    def entrer(self):
        try:
            self.nbEntree+=1
            self.parking.enter()
        except:
            self.nbEntree-=1
    
    def out(self):
        self.nbSortie+=1
        self.parking.out()