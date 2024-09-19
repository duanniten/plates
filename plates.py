def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str):
    #All vanity plates must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    #vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if not 1<len(s)<7:
        return False
    
    #Numbers cannot be used in the middle of a plate
    first_number = False
    for l in s:
        if l.isdigit():
            first_number = True
        elif first_number and l.isalpha():
            return False
    #No periods, spaces, or punctuation marks are allowed.
    if not s.isalnum():
        return False
main()