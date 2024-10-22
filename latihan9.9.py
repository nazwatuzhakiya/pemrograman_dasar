#jarak diinputkan oleh user
nazwajarak= float(input("Masukan Jarak Yang Ditempuh:"))

#hitung biaya sewa
if nazwajarak == 1:
    biaya= 4500
else:
    biaya= 4500 + (nazwajarak-1) * 2000

    #menampilkan biaya sewa
    print("Biaya sewa: Rp.", biaya)