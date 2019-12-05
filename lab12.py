class parking:
    def __init__(self, adresse, capacite, nbPortail):
        assert isinstance(adresse, str) and len(adresse) >= 0
        assert isinstance(capacite, int) and capacite >= 0
        assert isinstance(nbPortail, int) and nbPortail >= 0
        self._adresse = adresse
        self._capacite = capacite
        self._nbPortail = nbPortail

    def reset_portail(self, nbPortail_list):
        for i in range(1, self._nbPortail + 1):
            nbPortail_list.append(portail(i, 0, 0, 0))
        return nbPortail_list

class portail:
    def __init__(self, numPortail, nbPlacesLibres, nbEntrees, nbSorties):
        assert isinstance(numPortail, int) and numPortail >= 0
        assert isinstance(nbPlacesLibres, int) and nbPlacesLibres >= 0
        assert isinstance(nbEntrees, int) and nbEntrees >= 0
        assert isinstance(nbSorties, int) and nbSorties >= 0
        self._numPortail = numPortail
        self._nbPlacesLibres = nbPlacesLibres
        self._nbEntrees = nbEntrees
        self._nbSorties = nbSorties
         
    def place_disponible(self):  
        self._nbPlacesLibres -= self._nbSorties
        print("Nombre de places disponible est %s." + str(self._nbPlacesLibres))
    
    def place_indisponible(self):
        self._nbPlacesLibres += self._nbEntrees
        print("Nombre de places indisponible est %s." + str(self._nbPlacesLibres))

def main():
    prk = parking("Lyon 69003", 12, 1)
    nbPortail_list = prk.reset_portail([])

    for portail in nbPortail_list:
        portail.place_disponible()

if __name__ == "__main__":
    main()
