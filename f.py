mhs = input("Nama : ")
kehadiran = int(input("kehadiran : "))
uts = float(input("Nilai uts : "))
uas = float(input("Nilai uas : "))
tugas = float(input("Nilai tugas : "))

Nilai_akhir = (kehadiran/16 * 0.2 *100) + (uts * 0.3) + (uas * 0.4) + (tugas * 0.1)
if Nilai_akhir <=100 and Nilai_akhir >=90 :
    print("Nilai akhir mahasiswa : A")
elif Nilai_akhir <=89 and Nilai_akhir >=80 :
    print("Nilai akhir mahasiswa : B")
elif Nilai_akhir <=79 and Nilai_akhir >=70 :
    print("Nilai akhir mahasiswa : C")
elif Nilai_akhir <=69 and Nilai_akhir >=60 :
    print("Nilai akhir mahasiswa : D")
elif Nilai_akhir <=59 and Nilai_akhir >=0 :
    print("Nilai akhir mahasiswa : E")
else :
    print("Error")