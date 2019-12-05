class parking:
    def __init__(self, address, capmax, nbPort):
        assert isinstance(address,str) and len(address) > 0
        assert isinstance(capmax, int) and capmax > 0
        assert isinstance(nbPort, int) and nbPort > 0

        self.address=address
        self.capmax=capmax
        self.nbPort=nbPort

    def capacite_total(self):
        return self.capmax

    def place_libre(self):
        self.capmax -= 1

    def nbportail(self):
        return self.nbPort

class portail:
    def __init__(self, num_port, place_libre, nb_in, nb_out):
        assert isinstance(num_port, str) and len(num_port)>1
        assert isinstance(place_libre, int) and place_libre > 0
        assert isinstance(nb_in, int) and nb_in > 0
        assert isinstance(nb_out, int) and nb_out > 0

        self.num_port=num_port
        self.place_libre=place_libre   
        self.nb_in=nb_in
        self.nb_out=nb_out

        def count_in(self):
            self.nb_in += self.nb_in
            return self.nb_in

        def count_out(self):
            self.nb_out += self.nb_out
            return self.nb_out

        def nom_portail(self):
            return self.num_port
        
        def affichage(self):
            return 
        
        

pardieu=parking( "Lyon", 500, 200)
print(parking.nbportail(pardieu))