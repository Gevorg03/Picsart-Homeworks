//1
lst_numbers = []
number = 'space'
while number != '':
    number = input("Input classic numbers: ")
    if number != '':
        lst_numbers.append(number)
print(set(lst_numbers))

//2
def divider(num):
    return [i for i in range(1, num) if num % i == 0]
number = int(input("Input a number: "))    
print(divider(number)) 

//3
def perfect(num):
    return sum([i for i in range(1, num) if num % i == 0]) == num
number = int(input("Input a number: "))
print(perfect(number))

//4
def zip(data1, data2):
    new_lst = []
    for i in range(len(data1)):
        lst = []
        lst.append(data1[i])
        lst.append(data2[i])
        new_lst.append(lst)
    return new_lst
print(zip([1, 2, 3], [11, 22, 33]))

//5
import string
sentence = input('Input a sentence: ')
sentence_without_punctuation = sentence.translate(str.maketrans('', '', string.punctuation))
lst_sentence = sentence_without_punctuation.split()
if lst_sentence == lst_sentence[::-1]:
    print("palindrome")
else:
    print("no palindrome")

//6
lst_numbers = []
number = 'space'
while number != '':
    number = input("Input classic numbers: ")
    if number != '':
        lst_numbers.append(number)
lst_numbers = list(map(int, lst_numbers))
average_numbers = sum(lst_numbers) / len(lst_numbers)
print(average_numbers)
lst_numbers.sort()
print(lst_numbers)  

//7
list = []
    for i in range(6):
        r = random.randint(1, 49)
        if r not in list:
            list.append(r)
    print(list)

//8
def is_sorted(data):
    return data == sorted(data)
lst_numbers = []
value = 'space'
while value != '':
    value = input("Input data: ")
    if value != '':
        lst_numbers.append(value)
lst_numbers = list(map(int, lst_numbers))
print(is_sorted(lst_numbers))

//9
def is_sublist(larger, smaller):
    if len(smaller) == 0:
        return True
    ind = larger.index(smaller[0])
    count = 0
    for i in range(ind, len(smaller) + ind):
        if larger[i] != smaller[count]:
            return False
        count += 1
    return True
print(is_sublist([1, 2, 3, 4, 5, 6], [2, 3, 4]))
