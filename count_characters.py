def count_characters():
    #count the number of characters in a string
    full_name = input("Enter your full name: ") #get full name from user
    print(f"number of characters in {full_name} is {len(full_name)}") #count the number of characters in the string


#call the function
if __name__ == '__main__':
    count_characters()