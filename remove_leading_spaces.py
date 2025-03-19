def remove_leading_spaces():
    #remove leading spaces from a string
    full_name = input("Enter your full name: ") #get string from user
    print(full_name.lstrip()) #display string with leading spaces removed


#call the function
if __name__ == '__main__':
    remove_leading_spaces()