daftar_nilai = []

ulangi =  True

while ulangi:
    nama = input("Masukan nama: ")
    nim = input ("Masukan NIM: ")
    tugas = int(input("Nilai Tugas: "))
    UTS = int(input ("Nilai UTS: "))
    UAS = int(input("Nilai UAS: "))
    akhir = (tugas * 30/100) + (UTS * 35/100) + (UAS * 35/100)

    daftar_nilai.append([nama, nim, int(tugas), int(UTS), int(UAS), int(akhir)])
    if (input("tambah data lagi (y/t)?")== 't'):
        ulangi = False

print("\nDaftar Nilai Mahasiswa: ")
print("=======================================================================")
print("| No |   Nama   |   NIM   |   Tugas   |   UTS   |   UAS   |   Akhir   |")
print("=======================================================================")
i=0
for item in daftar_nilai:
    i+=1
    print("|{no:2d}|{nama:12s}| {nim:9s}|{tugas:7d}|{UTS:5d}|{UAS:5d}|{akhir:6.2f}|"
          .format(no=i, nama=item[0], nim=item[1], tugas=item[2], UTS=item[3], UAS=item[4], akhir=item[5]))
print("=======================================================================")
