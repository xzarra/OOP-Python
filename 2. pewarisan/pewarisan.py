# Pewarisan
class ibu:
    def __init__(self):
        print("Ini adalah kelas ibu")
    
    def sifatibu(self):
        print("sifatnya penyayang")

class anak(ibu):
    def __init__(self):
        print("ini kelas anak")
    
    def sifatanak(self):
        print("sifatnya nakal")

berubah= anak()
berubah.sifatanak()

berubah.sifatibu()
