# Tugas Praktikum 4

## Buatlah program sederhana untuk menambahkan data kedalam sebuah list dengan rincian sebagai berikut :
* Program meminta memasukan data sebanyak banyaknya (gunakan perulangan)
* Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban t(tidak), maka program akan menampilkan daftar datanya.
* Nilai akhir diambil dari perhitungan 3 komponen nilai (tugas:30%, uts:35%, uas:35%)
* Buat flowchart dan penjelasan programnya pada Readme.md
* Commit dan push repository

### Program List Data Mahasiswa
* Kode :
```
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
```
* Mendeklarasikan variabel dan list ```daftar_nilai = []```
* Perulangan terus menerus jika memenuhi syarat
```
ulangi =  True

while ulangi:
```
* Masukan data pengguna
```
nama = input("Masukan nama: ")
    nim = input ("Masukan NIM: ")
    tugas = int(input("Nilai Tugas: "))
    UTS = int(input ("Nilai UTS: "))
    UAS = int(input("Nilai UAS: "))
```
* Menentukan nilai akhir dengan operator ```akhir = (tugas * 30/100) + (UTS * 35/100) + (UAS * 35/100)```
* Memasukan data kedalam list ```daftar_nilai.append([nama, nim, int(tugas), int(UTS), int(UAS), int(akhir)])```
* Perulangan jika dikehendaki pengguna
```
daftar_nilai.append([nama, nim, int(tugas), int(UTS), int(UAS), int(akhir)])
    if (input("tambah data lagi (y/t)?")== 't'):
        ulangi = False
```
* Menampilkan kolom data
```
print("\nDaftar Nilai Mahasiswa: ")
print("=======================================================================")
print("| No |   Nama   |   NIM   |   Tugas   |   UTS   |   UAS   |   Akhir   |")
print("=======================================================================")
```
* Menentukan cetak dalam list berupa data yang telah ditentukan
```
i=0
for item in daftar_nilai:
    i+=1
    print("|{no:2d}|{nama:12s}| {nim:9s}|{tugas:7d}|{UTS:5d}|{UAS:5d}|{akhir:6.2f}|"
          .format(no=i, nama=item[0], nim=item[1], tugas=item[2], UTS=item[3], UAS=item[4], akhir=item[5]))
```
* Output

![output](https://user-images.githubusercontent.com/56512562/72222441-41e3bf80-3597-11ea-8057-cd54da2fbe2d.png)

# Terima Kasih
