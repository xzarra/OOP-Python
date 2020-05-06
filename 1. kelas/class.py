class Buah:
    
    def __init__(self, nama, warna, rasa):
        self.warna = warna
        self.rasa = rasa
        self.nama = nama
        
    def Tampildata(self):
        print("Ini adalah buah {}, berwarna {}, dan rasanya {}".format(self.nama,self.warna,self.rasa))
    
    def Tampildatasatuan(self):
        print("Nama Buah : ", self.nama)
        print("Warna Buah : ", self.warna)
        print("Rasa buah : ", self.rasa)

buah1 = Buah("apel","merah","manis")
buah2 = Buah("nanas","kuning","asam")

buah1.Tampildatasatuan()
print('\n')
buah2.Tampildatasatuan()
print("\n")
buah1.Tampildata()
buah2.Tampildata()

''' outputnya adalah
Nama Buah :  apel
Warna Buah :  merah
Rasa buah :  manis


Nama Buah :  nanas
Warna Buah :  kuning
Rasa buah :  asam


Ini adalah buah apel, berwarna merah, dan rasanya manis
Ini adalah buah nanas, berwarna kuning, dan rasanya asam
'''