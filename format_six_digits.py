def format_six_digits():
    #always display 6 digits with leading zeros
    number = int(input("Enter a number: ")) #get number from user
    print(f"{number:06}") #display number with leading zeros



#call the function
if __name__ == '__main__':
    format_six_digits()