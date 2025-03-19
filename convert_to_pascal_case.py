def convert_to_pascal_case():
    #convert full name to pascal case
    full_name = input("Enter your full name: ") #get full name from user
    words = full_name.split() #split full name into words
    pascal_case = ''.join(word.capitalize() for word in words) #join words with no space
    print(pascal_case) #print pascal case


#call the function
if __name__ == '__main__':
    convert_to_pascal_case()