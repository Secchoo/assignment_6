def convert_to_pascal_case():
    #convert full name to pascal case
    full_name = input("Enter your full name: ")
    words = full_name.split()
    pascal_case = ''.join(word.capitalize() for word in words)
    print(pascal_case)


if __name__ == '__main__':
    convert_to_pascal_case()