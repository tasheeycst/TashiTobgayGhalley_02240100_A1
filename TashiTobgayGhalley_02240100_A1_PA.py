import math

# Prime number sum calculator
def my_prime(x):
    if x<= 1:
        return False
    
    for i in range(2,int(x**0.5)+1):
        if x %i== 0:
            return False
    return True

def total_sum (start,end):
    total = 0
    for x in range (start , end + 1):
        if my_prime(x):
            total += x
    return total

# Length unit converter
def LengthConvert(value, direction):
    mt_to_ft = 3.28084
    ft_to_mt= 0.3048
    
    if direction == 'M':
        converted_value = value * mt_to_ft
    elif direction == 'F':
        converted_value = value * ft_to_mt
    else:
        return ("Invalid direction! Use 'M' for meters to feet or 'F' for feet to meters.")
    return round(converted_value, 1)

# Consonant counter
def ConsonantCount(text):
  
    vowels = "aeiouAEIOU"
    ConsonantCount = 0

    for char in text:
       
        if char.isalpha() and char not in vowels:
            ConsonantCount += 1
    
    return ConsonantCount

# Min-Max number Finder
def MinMaxFinder(num):
    smallest = min(num)
    largest = max(num)
    return f"Smallest: {smallest}, Largest: {largest}"


# Palindrome checker
def palindrome(text):
    CleanText = ''.join(text.split()).lower()
    return CleanText == CleanText[::-1]

# Word counter
import requests

def word_count(text_file_url):
    response = requests.get(text_file_url)
    text = response.text.lower()
    wlist = ['the', 'was', 'and']
    word= {word: text.count(word) for word in wlist}
    return word

# Menu and main program flow
def main():
    while True:
        print("\nMenu:")
        print("1. Prime number sum calculator")
        print("2. Length unit converter")
        print("3. Consonant counter")
        print("4. Min-Max number finder")
        print("5. Palindrome checker") 
        print("6. Word counter")
        print("7. Exit")
        
        choice = input("choose a function by entering a number (1-7): ").strip()
        
        if choice == '1':
            # Prime number sum calculator
            try:
                start  = int (input("enter the start range"))
                end = int (input("enter the end range"))
                result = total_sum (start , end)
                print(f"the prime sum of the  range given :{result}")
                
              
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == '2':
            # Length unit converter
            try:
                value = float(input("Enter the numeric value: "))
                direction = input("Enter the direction to convert ('M' for meters to feet, 'F' for feet to meters): ")

                result = LengthConvert(value, direction)
                print(f"Converted length value: {result}")
               
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            # Consonant counter
            text = input("Enter a text string: ")
            result = ConsonantCount(text)
            print(f"Number of consonants: {result}")
            
        elif choice == '4':
            #Min - Max
            n = int(input("How many numbers do you want to enter? "))
            num1 = []
            for i in range(n):
                num2 = float(input(f"Enter number {i+1}: "))
                num1.append(num2)
            print(MinMaxFinder(num1))

        elif choice == '5':
            # Palindrome checker
            text = input("Enter a text string: ")
            result = palindrome(text)
            print(f"Is the string a palindrome? {result}")

        elif choice == '6':
            # Word counter
            file_url = input("Enter the URL of the text file: ").strip()
            try:
                result = word_count(file_url)
                print(f"Word counts: {result}")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching the file: {e}")

        elif choice == '7':
            print("EXIT DONE  Thank you!")
            break

        else:
            print("Invalid.")

        # Ask user if they want to perform another calculation
        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the program. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
