password = input("Enter Password: ").strip()
f = 0
Upper = Lower = Num = SpChar = False
for i in password:
    f += 1
    if i.isupper():
        Upper = True
    elif i.islower():
        Lower = True
    elif i.isnumeric():
        Num = True
    else:
        SpChar = True

if 7 < f:
    if Upper and Lower and Num and SpChar:
        print("Very Strong")
    else:
        if Lower and Num and SpChar:
            print("Strong")
        elif Upper and Lower and Num:
            print("Okay")
        elif Upper and Num and SpChar:
            print("Strong")
        elif Upper and Lower and SpChar:
            print("Strong")
        else:
            print("Very Weak")
else:
    print("Password Too Short")
    
