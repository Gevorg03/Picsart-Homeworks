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
