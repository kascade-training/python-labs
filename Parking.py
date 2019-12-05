class parking:
    def __init__(self, address, cap, nbPort)
    assert isinstance(address,str) and len(adr) > 0
    assert isinstance(cap, int) and cap > 0
    assert isinstance(nbPort, int) and nbPort > 0

    self.address=address
    self.cap=cap
    self.nbPort=nbPort

    def totalplace(self):
        return self.cap
    def complet(self):
        return 