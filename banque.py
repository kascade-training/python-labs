class CompteBanque:
    def __init__(self, Banque, Titulaire, Solde=0):
        assert isinstance(Banque, str) and len(Banque) > 0
        assert isinstance(Titulaire, str) and len(Titulaire) > 0
        assert isinstance(Solde, float) and Solde >= 0
        
        self.nBanque = Banque
        self.nTitulaire = Titulaire
        self.solde = Solde
        
    def Retirer(self, montant):
        assert isinstance(montant, float) and montant <= self.solde and montant >= 0
        self.solde -= montant
        
    def Deposer(self, montant):
        assert isinstance(montant, float) and montant >0
        self.solde += montant
        
    def __str__(self):
        res="Titulaire \t: %s"+self.nTitulaire
        res="\n Banque \t: %s"+self.nBanque
        res="\n Solde \t: %s"+self.solde
        return res
    
    def __cmp__(self, autre):
        assert isinstance(autre, CompteBanque)
        