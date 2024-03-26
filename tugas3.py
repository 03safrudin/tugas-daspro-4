belanja = int(input("harga belanja : "))
if belanja >=250000:
    diskon = belanja*0.5
    print ("Anda mendapatkan diskon\nHarga belanja menjadi : ",belanja-diskon)
else :
    print("Belanjaan anda kurang dari Rp 250.000, tidak ada diskon")
    print("Harga belanjaan anda : ",belanja)