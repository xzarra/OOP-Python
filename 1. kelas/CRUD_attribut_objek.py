# inisialisasi kelas
class Buah:
    # membuat fungsi didalam kelas
    def __init__(self, nama, warna, rasa, harga):
        self.warna = warna
        self.rasa = rasa
        self.nama = nama
        self.harga = harga
    # membuat fungsi tampil data secara terperinci
    def Tampildata(self):
        print("Ini adalah buah {}, berwarna {}, dan rasanya {}".format(self.nama,self.warna,self.rasa))
    # membuat fungsi tampil data secara satuan
    def Tampildatasatuan(self):
        print("Nama Buah : ", self.nama)
        print("Warna Buah : ", self.warna)
        print("Rasa buah : ", self.rasa)
        print("Harga : ", self.harga)
# membuat data / instansiasi objek
buah1 = Buah("apel","merah","manis","")
buah2 = Buah("nanas","kuning","asam","")

# Membuat attribut objek (CREATE)
setattr(buah1, 'harga', "Rp 15.000 /Kg")
# output akan menambahkan variabel harga

# Melihat attribut objek (READ)
getattr(buah1, 'harga')
# outputnya adalah harga menjadi 15.000 /Kg

# Mengubah attribut objek (UPLOAD)
setattr(buah1, 'rasa',"masam")
# outputnyaa adalah rasa yang awalnya manis menjadi masam

# Menghapus attribut objek (DELETE)
delattr(buah1,'nama')

# memnampilkan data / objek
buah1.Tampildatasatuan()
print('\n')
buah2.Tampildatasatuan()
print("\n")
buah1.Tampildata()
buah2.Tampildata()
