number = int(input("Bir Tam Sayı Giriniz: "))

prime_check = True

for dividing in range (2,number):
    if number%dividing == 0:
        prime_check = False
        print("Sayı Asal Değildir.")
        break

if prime_check:
    print("Sayı Asaldır.")  