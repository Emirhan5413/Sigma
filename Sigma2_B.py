number = int(input("Bir Tam Sayı Giriniz: "))

def isprime(number):
    for n in range(2,number):
        if number%n==0:
            return False
    return True

while not isprime(number):
    number +=1
print(number)
