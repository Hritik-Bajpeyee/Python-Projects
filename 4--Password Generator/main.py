import string
import secrets

def gener_Password(length):
    if length < 8:
        print("Password Length Should Be at Least 8 Characters For Security Reasonn!!!")
        return None;
    if length > 200:
        print("Why You  Need This Password It's Too Long!!!")
        return None
    

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    password = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]

    all_chars = letters+digits+special_chars
    password += [secrets.choice(all_chars) for _ in range(length-3)]

    secrets.SystemRandom().shuffle(password)

    return''.join(password)

while True:
    try:
        length = int(input("Enter The Desired Password Length: "))
        if length < 8:
            print("Password Length must be 8 Try Again!!!")
            continue
        if length >= 200:
            print("Why You  Need This Password Too Long (Use Under 200)!!!")
            continue
        password =gener_Password(length)

        if password:
            print(f"Generate Password: {password}")
            break
    except ValueError:
        print("Invalid Try Again!!!!!")
    


