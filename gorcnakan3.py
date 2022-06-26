def reverse(number):
    return int(str(num)[::-1])
num = int(input("Input a number: "))
print(reverse(num))

def sum_of_min_max(data : list):
    return [data.index(el) for el in data if el % 2 == 0]
print(sum_of_min_max([15, 24, 10, 5]))

def even_index(data : list):
    return [data.index(el) for el in data if el % 2 == 0]
print(even_index([15, 24, 10, 5]))

def reverse_word(word):
    reversed_word = ""
    for el in word:
        reversed_word = el + reversed_word
    return reversed_word
_word = input("Input a word: ")
print(reverse_word(_word))

def median(data):
    mid = len(data) // 2
    return (data[mid] + data[mid-1]) / 2 if len(data) % 2 == 0 else data[mid] 
print("Median =", median([1, 2, 3, 4, 5, 6]))    

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
 
