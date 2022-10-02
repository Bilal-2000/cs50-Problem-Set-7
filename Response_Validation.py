from validator_collection import checkers


def main():
    str = input("Email address: ")
    if checkers.is_email(str):
        print("Valid")
    else:
        print("Invalid")


main()
