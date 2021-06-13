# Marisa's 25th Birthday Puzzle Hunt Password Checker
# June 2021
# Josh Miller

import hashlib
import time

passwords = {
    "thesty"        :   "c6b41b47e50cd90eefccc9f7ae0f99814b82615c5cee99133e1c95a5693cdecd",
    "thetower"      :   "95b40c5764a32607a96753cbddcb55b0256d724866906168b932f77864edb3c1",
    "thelibrary"    :   "75261701c075c0ab4e24ca1fb0b9f7d601cc6b3914092421eafc1808dcaf0347",
    "thesecondact"  :   "84db3ef4fe208927de0352a0a9686962b2b93d1c30492d5d7fe2db7af6552ac5"
}

def dictChecker(bin):
    binKey = bin.replace(' ','').lower()
    return not binKey in passwords

def checker(bin,password):
    binKey = bin.replace(' ','').lower()
    shaPassword = hashlib.sha256(password.encode()).hexdigest()

    if not binKey in passwords:
        print("I don't recognize that pastebin name. Check your spelling maybe?")
    else:
        if passwords[binKey] == shaPassword:
            print("The password is correct! \n")
        else:
            print("The password is incorrect. \n")
            #print("the sha256 conversion of your guess is "+shaPassword)


def main():
    print("Welcome to this password checker tool. \n")
    time.sleep(2)
    print("Since pastebin has an attempt limit on passwords, you can use this tool to verify your guesses. \n")
    time.sleep(3)
    print("To use this tool, first enter the name of the paste you're trying to unlock. \n")
    time.sleep(2)
    print("Then try your guess for the password to see whether it's correct. \n")
    time.sleep(2)

    pastebin = ""
    while pastebin != "exit":
        password = ""
        pastebin = input("Enter the pastebin you'd like to unlock. Type 'exit' to exit. ")
        if pastebin == "exit":
            break
        elif dictChecker(pastebin):
            print("I don't recognize that pastebin name. Check your spelling maybe?")
        else:
            while password != "back":
                password = input("Enter your password guess for "+pastebin+". Type 'back' to go back and select a different pastebin. ")
                if password == "back":
                    break
                else:
                    checker(pastebin,password)

if __name__ == "__main__":
    main()
