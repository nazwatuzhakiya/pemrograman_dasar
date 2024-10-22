#user mengiinputkan jumlah gaji pokoknya
nazwagaji_pokok = float(input("Masukan Gaji Pokok:"))

#deklarasi
nazwatunjangan= nazwagaji_pokok*0.20
nazwapajak=(nazwagaji_pokok + nazwatunjangan) *0.10

#menghitung gaji bersih
nazwagaji_bersih= nazwagaji_pokok+nazwatunjangan-nazwapajak

#menampilkan hasil geji bersih
print("Gaji Bersih:", nazwagaji_bersih)
print("Tunjangan:", nazwatunjangan)
print("Pajak:", nazwapajak)

