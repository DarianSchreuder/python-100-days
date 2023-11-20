#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for nr in range(0,nr_letters):
    password += letters[random.randint(0,25)]

for nr in range(0,nr_symbols):
    password += numbers[random.randint(0,9)]
    
for nr in range(0,nr_numbers):
    password += symbols[random.randint(0,8)]   
    
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""

while ((nr_letters or nr_numbers or nr_symbols) > 0):
    match random.randint(1,3):    
        case 1:
            if(nr_letters > 0):
                password += letters[random.randint(0,25)]
                nr_letters -= 1
        case 2:
            if(nr_numbers > 0):
                password += numbers[random.randint(0,9)]
                nr_numbers -= 1
        case 3:
            if(nr_symbols > 0):
                password += symbols[random.randint(0,8)]
                nr_symbols -= 1
                
print(password)
                