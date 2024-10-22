#input alas dan tinggi dari user
nazwaalas = float(input("Masukan panjang alas: "))
nazwatinggi = float(input("Masukkan tinggi: "))
nazwasisi_miring = float(input("masukan sisi miring:"))

#hitung keliling dan luas
keliling  = 2* (nazwaalas*nazwasisi_miring)
luas = nazwaalas*nazwatinggi


#menampilkan hasil hitung keliling dan luas
print("keliling jajar genjang: ", keliling)
print(" luas jajar genjang: ", luas)