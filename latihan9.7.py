
# Deklarasi variabel a dan b dengan tipe data integer
nazwa_a = int(input("Masukkan nilai a: "))
nazwa_b = int(input("Masukkan nilai b: "))

# Menampilkan nilai a dan b awal
print("Nilai a awal: ", nazwa_a)
print("Nilai b awal: ", nazwa_b)

# Menukar nilai variabel a dan b
nazwa_a = nazwa_a + nazwa_b
nazwa_b = nazwa_a - nazwa_b
nazwa_a = nazwa_a - nazwa_b

# Menampilkan nilai a dan b setelah ditukar
print("Nilai a setelah ditukar: ", nazwa_a)
print("Nilai b setelah ditukar: ", nazwa_b)