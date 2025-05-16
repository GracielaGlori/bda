#nama = input ("masukkan nama anda   :")
#umur = int(input("masukkan umur  :"))
#jur = input("masukkan jurusan  :")
#ipk = input("masukkan ipk  :")
#print("====cetak====")
#print("nama anda    :"+nama)
#print("umur anda    :"+str(umur))
#print("jurusan anda :"+jur)
#print("ipk anda     :"+str(ipk))

#a= int(input("nilai pertama :"))
#b= int(input("nilai kedua :"))
#c=a*b
#print(a,' kali ',b,' = ',c)

#print('penentuan bilangan genap atau ganjil')
#print('------------------------------------')
#bilangan = int(input('bilangan : '))
#if bilangan % 2 == 0:
#    print('bilangan', bilangan, 'merupakan bilangan genap')
#else:
#    print('bilangan', bilangan, 'merupakan bilangan ganjil')

#print('penghitungan huruf')
#print('-------------------')
#teks=input('masukkan string')
#jumHurufKapital=0
#jumHurufKecil=0
#for j in range(0, len(teks)):
#    kar=teks[j]
#    if kar.isupper():
#        jumHurufKapital = jumHurufKapital+1
#    elif kar.islower():
#        jumHurufKecil = jumHurufKecil+1
#print('jumlah huruf kapital =', jumHurufKapital)
#print('jumlah huruf kecil =', jumHurufKecil)

import math
jejari = float(input("jari-jari :   "))
luas = 2 * math.pi * jejari * jejari
print("luas %5f"%(luas))