# overriding
# berfungsi mengabaikan fungsi dari kelas induk di dalam kelas anak.
class Induk:
    def fungsi(self):
        print("Memanggil metode induk")

class Anak(Induk):
    def fungsi(self):
        print("Memanggil metode anak")

c = Anak()
c.fungsi()