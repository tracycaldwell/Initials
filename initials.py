def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    uppercase_name = fullname.upper()
    name_list = uppercase_name.split()
    initials = []
    for char in name_list:
        initials.append(char[0])
    return (''.join(initials))

def main():
    fullname = (input("What is your full name?"))
    print ("The initials of", fullname, "are", get_initials(fullname))

if __name__ == "__main__":
    main()
        