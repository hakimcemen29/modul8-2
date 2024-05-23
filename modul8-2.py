class Masyarakat:
    def __init__(self, golongan="LAINNYA", gaji=150000):
        self.golongan = golongan
        self.gaji = gaji

    def info(self):
        return f"Golongan: {self.golongan}, Gaji: {self.gaji}"


class Dosen(Masyarakat):
    def __init__(self, gaji=200000):
        super().__init__("DOSEN", gaji)


class Staff(Masyarakat):
    def __init__(self, gaji=150000):
        super().__init__("STAFF", gaji)
        
class Lainnya(Masyarakat):
    def __init__(self, gaji=150000):
        super().__init__("Lainnya", gaji)


if __name__ == "__main__":
    gaji_dosen = int(input("Masukkan gaji dosen: "))
    dosen1 = Dosen(gaji_dosen)
    
    gaji_staff = int(input("Masukkan gaji staff: "))
    staff1 = Staff(gaji_staff)
    
    gaji_lainnya = int(input("Masukkan gaji Lainnya: "))
    lainnya1 = Lainnya(gaji_lainnya)

    print(dosen1.info())
    print(staff1.info())
    print(lainnya1.info())
