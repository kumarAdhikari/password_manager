from cryptography.fernet import Fernet

def retrivepassword():
    print("Now retriving Password mode\n")
    email = input("What would you like to retrive: ")
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username, passwd = data.split("|")
            if email == username:
                print(f"Account Name: {username}\nPassword: {passwd}\n")
                break
            else:
                print("Username NOT FOUND")
                break
    print()



def insertpassword():
    print("Now inserting password mode")
    account = input("Your Account Name: ")
    pwd = input("Your Password: ")

    with open('password.txt', 'a') as f:
        f.write(account + '|' + pwd + '\n')

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

while True:
    print("******** WELCOME TO PASSWORD MANAGER *********")
    masterpassword = input("Please Type your Master Password: ")
    key = load_key() + masterpassword.encode()
    fer = Fernet(key)
    reason_for_visit = int(input("Do you want to retrive password or insert password ? "
                                 "\n\nPlease press 1 to retrive, 2 to insert new password and 3 to Quit"))
    if reason_for_visit == 1:
        retrivepassword()
    elif reason_for_visit == 2:
        insertpassword()
    elif reason_for_visit == 3:
        exit()
    else:
        print("\nINVALID RESPONSE. Please Try Again\n")
