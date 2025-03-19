def convert_to_snake_case():
    #convert anything to snake case
    full_name = input("Enter your name: ")
    words = full_name.split() #split full name into words
    snake_case = '_'.join(word.lower() for word in words) #join words with underscore
    print(snake_case)


#call the function
if __name__ == '__main__':
    convert_to_snake_case()