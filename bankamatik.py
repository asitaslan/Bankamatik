

AsitHesap = {
    'ad': 'Asit Aslan',
    'HesapNo': '123511258',
    'bakiye': 5000,
    'ekHesap': 1000

}
HasanHesap = {
    'ad': 'Hasan Erk',
    'HesapNo': '875578842',
    'bakiye': 600,
    'ekHesap': 3000

}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranizi alabilirsiniz")
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanilsin mi (e/h) :")
            if ekHesapKullanimi == 'e':
                hesap['bakiye'] = 0
                hesap['ekHesap'] = toplam - miktar
                print('paranizi alabilirsiniz')
            else:
                print(f"{hesap['HesapNo']} nolu hesabinizda {hesap['bakiye']}TL bulunmaktadir")
        else:
            print('Uzgunuz hesaplarnizda yeterli miktar bulunamamaktadir')

def paraYatir(hesap, miktar):
    print(f"Merhaba Sayin {hesap['ad']}")
    hesap['bakiye'] += miktar
    print(f"{hesap['HesapNo']} nolu hesabnizin guncel bakiyesi {hesap['bakiye']} ")

islem = input('Merhaba Lutfen yapmak istediginiz islemi secin (Para Yatirma: Y/ Para Cekme C) :')

if islem == 'Y':
    miktar = int(input('Lutfen Yatirmak Istediginiz Miktari giriniz :'))
    paraYatir(HasanHesap, miktar)
else:

    miktar = int(input('Lutfen Cekmek Istediginiz Miktari Giriniz :'))
    paraCek(HasanHesap, miktar)



print(HasanHesap)