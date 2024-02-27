number = -10.6

print("5")
print('hello world')

input= input("input somthing:")

newlist= [1, 2, {}, "abc", ["name", [1,2,3], "name2"]]
# doubt:
print(newlist[1])
a=2
b=3

print(a-b )

#### Class 3 FUnctions


#try:
    even_numbers= [2,4,6]
    x= (even_numbers[1])
    result= x/1
    print(result)
#except
    

##-------------------------------------------------------------------------
import random

# Set the winning numbers
winning_numbers = random.sample(range(1, 11), 3)  # Choose 3 random numbers from 1 to 10

def announce_prize(user_numbers):
    if user_numbers == winning_numbers:
        print("Congratulations! You won the first-place prize!")
    elif len(set(user_numbers).intersection(winning_numbers)) == 2:
        print("Congratulations! You won the second-place prize!")
    elif len(set(user_numbers).intersection(winning_numbers)) == 1:
        print("Congratulations! You won the third-place prize!")
    else:
        print("Sorry, you did not win any prize this time.")

def get_user_numbers():
    try:
        numbers = []
        for i in range(3):
            num = int(input(f"Enter number {i+1} (1-10): "))
            if num < 1 or num > 10:
                raise ValueError("Numbers must be between 1 and 10.")
            numbers.append(num)
        return numbers
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter valid numbers.")
        return get_user_numbers()

if __name__ == "__main__":
    print("Welcome to the Lottery Winner Program!")
    print(f"Winning numbers: {winning_numbers}")
    
    user_numbers = get_user_numbers()
    print(f"Your numbers: {user_numbers}")
    
    announce_prize(user_numbers)

###------------------------------------------
#Class 4:

dict

for keys, values in x.items():
    print(keys, "=", values)


with open("/Users/vineethkotala/Desktop/Endeavour Consult/Data Engineering/sample_file.csv", 'r') as f:
    line = f.readline()
    #f.read readds entire file into a string. input.readlines entire lines into string.
    #f.read(digits) readds entire file into a string. 
    while line:
        print(line, end='')
        line = f.readline()


import csv 
with open("/Users/vineethkotala/Desktop/Endeavour Consult/Data Engineering/sample_file.csv", 'w') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



list= ["abc", 1, 2, 3, {keys, values}]
with open('sample.txt', 'w') as f:
    for x in list:
        f.write(str(x)+ "\n")


################################################
#Class 5


#JSON
#Date-time
import datetime
d=datetime.date(year=2023,month=6,day=9)
print(d)

    