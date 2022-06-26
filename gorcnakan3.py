//1
def reverse(number):
    return int(str(num)[::-1])
num = int(input("Input a number: "))
print(f"The reverse of {num} is {reverse(num)}")

//2
def combine(data):
    num = ""
    for el in data:
        num += str(el)
    return num    
print(combine((1, 2, 3, 4)))

//3
def sum_of_min_max(data : list):
    return [data.index(el) for el in data if el % 2 == 0]
print(sum_of_min_max([15, 24, 10, 5]))

//4
def even_index(data : list):
    return [data.index(el) for el in data if el % 2 == 0]
print(even_index([15, 24, 10, 5]))

//5
def reverse_word(word):
    reversed_word = ""
    for el in word:
        reversed_word = el + reversed_word
    return reversed_word
word = input("Input a word: ")
print(f"The reverse of {word} is {reverse_word(word)}")

//6
def is_prime(n):
    for i in range(2,n // 2):
        if n % i == 0:
            return False
    return True 
num = int(input("Input a number: "))
number = num + 1
while not is_prime(number):
    number += 1
print(f"The smallest prime number,that larger than {num} is {number}")

//7
def median(data):
    mid = len(data) // 2
    return (data[mid] + data[mid-1]) / 2 if len(data) % 2 == 0 else data[mid] 
print("Median =", median([1, 2, 3, 4, 5, 6]))    

//8
def count_days(year, month):
    if month in (4, 6, 9, 11):
        return 30
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2 and year % 4 == 0:
        return 29
    return 28    
year = int(input("Input the year: "))
month = int(input("Input the month: "))
print(count_days(year, month), "day")
 
//9
import random
def random_passwd(n):
    password = ""
    for i in range(n):
        num = random.randint(33, 126)
        password += chr(num)
    return password
size = int(input("Input the size: "))
print("Password =", random_passwd(size))

//10
def same_parity(n, *args):
    return [el for el in args if el % n == 0]
n = 5    
print(f"The multiple of {n} are {same_parity(5, 10, 21, 3, 45, 80)}")
