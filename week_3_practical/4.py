BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password1 = input("Enter a new password (8-12 characters): ")

if 8 <= len(password1) <= 12:
   
    if password1 not in BAD_PASSWORDS:
    
        password2 = input("Confirm the password: ")

        if password1 == password2:
            print("Congratulations Password Set..")
        else:
            print("Error: Passwords do not match. Please try again.")
    else:
        print("Error: Common password chosen. Please choose a different password.")
else:
    print("Error: Password must be between 8 and 12 characters long.")
