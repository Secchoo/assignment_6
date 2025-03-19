def reverse_case():
    #reverse the case of each character
    full_name = input("Enter your full name: ") #get full name from user
    print(full_name.swapcase()) #reverse the case of each character in the string


#call the function
if __name__ == '__main__':
    reverse_case() #call the function