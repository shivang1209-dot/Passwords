import random
import string

def main():
    #Input The Length Of Password
    length = int(input("Length Of Password: "))
    #Join The Returned List Into 1 String 
    a = ''.join(randomizer(length))
    print("Your Desired Password Is: " + a)

def randomizer(length):
    return random.choices(string.ascii_letters + string.digits + string.punctuation,k=length)

if __name__ == "__main__":
    main()



    