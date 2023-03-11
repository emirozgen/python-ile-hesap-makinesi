#Toplama
def Topla(x, y):
    return x + y

#Çıkarma
def Çıkarma(x, y):
    return x - y

#Çarp
def Carpma(x, y):
    return x * y

#Böl
def Bolme(x, y):
    return x / y

print("İşlem Seç")
print("==========")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarp")
print("4.Böl")

#Kullanıcı Veri Girişi
secin = input("Seciniz (1/2/3/4):")
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))

if secin == "1":
    print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))
elif secin == "2":
    print(sayi1,"-",sayi2,"=", Çıkarma(sayi1,sayi2))
elif secin == "3":
    print(sayi1,"*",sayi2,"=", Carpma(sayi1,sayi2))
elif secin == "1":
    print(sayi1,"/",sayi2,"=", Bolme(sayi1,sayi2))
else:
    print("geçersiz")                