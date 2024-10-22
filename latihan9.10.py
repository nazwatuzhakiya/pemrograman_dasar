
#def digunakan untuk mendefinisikan sebuah fungsi (mutu adalah angka mutu)
# fungsi untuk menghitung ips (indeks prestasi semester)
def hitung_ips(mutu):
    # Menghitung total bobot
    mata_kuliah = ((mutu[0] * 2) + (mutu[1] * 2) + (mutu[2] * 2) + 
                      (mutu[3] * 3) + (mutu[4] * 4) + (mutu[5] * 3) + (mutu[6] * 4))
    #mutu0 adalah AMPA
    #mutu1 adalah AMPP
    #mutu2 adalah BI1
    #mutu3 adalah AMPDI
    #mutu4 adalah AMPTIK
    #mutu5 adalah AMMD
    #mutu6 adalah AMPDI

    ips = mata_kuliah / 20  # total mutu dibagi 20(20 adalah jumlah sks)
    return ips

# Fungsi untuk menentukan status kelulusan
def status_kelulusan(ips):
    if ips >= 2.75: #jika ips lebih atau sama dengan 2.75 maka  kriteria menjadi tetap
        return "Tetap"
    elif 2.00 < ips < 2.75: 
        return "Percobaan"
    else:
        return "Tidak Lulus"

# nama dan NIm diinputkan oleh user
nama = input("Masukkan Nama Mahasiswa: ")
nim = input("Masukkan NIM Mahasiswa: ")

# Data SKS mata kuliah semester 1
sks = [2, 2, 2, 3, 4, 3, 4]  # SKS sesuai tabel

# konversi huruf mutu menjadi angka
huruf_mutu = {
    'A': 4, 'AB': 3.5, 'B': 3, 'BC': 2.5, 'C': 2, 'D': 1, 'E': 0
}

# Input nilai mata kuliah
nilai = []
for i in range(7):
    huruf = input(f"Masukkan huruf mutu untuk mata kuliah {i+1}: ")
    nilai.append(huruf_mutu[huruf.upper()])

# Hitung IPS
ips = hitung_ips(nilai, sks)

# Tentukan status kelulusan
status = status_kelulusan(ips)

# Tampilkan hasil
print("\n===== Hasil Akademik Mahasiswa =====")
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"IPS: {ips:.2f}")
print(f"Status Kelulusan: {status}")