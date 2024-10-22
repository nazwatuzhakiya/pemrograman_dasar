#deklarasi
nazwanama = "Andi"
nazwaumur = 18
nazwaprogram_studi = "sistem informasi"
nazwajenis_kelamin = "perempuan"
nazwatinggi = 160
nazwakelas = "SI-1A"
nazwalulus = False

nazwanama = "budi"
nazwaumur = 21
nazwatinggi= 157
nazwakelas = "SI-3F"
nazwalulus = True

#menampilkan output
print("nama:", nazwanama)
print("umur:", nazwaumur, "tahun")
print("tinggi badan:", nazwatinggi, "cm")
print("program studi:", nazwaprogram_studi)
print("kelas:", nazwakelas)
print("jenis kelamin:", nazwajenis_kelamin)

#pernyataan kondisional
if nazwalulus == True: #kurang titik 2: dan true
  print("Status: Alumni")
else:
  print("Status: Mahasiswa aktif")