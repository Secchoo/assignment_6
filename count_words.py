def count_words():
    #count the number of words in a string
    full_name = input("Enter your full name: ") #get full name from user
    print(f"number of words in {full_name} is {len(full_name.split())}") #count the number of words in the string



#call the function
if __name__ == '__main__':
    count_words()