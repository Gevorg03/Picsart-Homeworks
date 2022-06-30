//1
def name_address(name, address):
    return f"My name is {name}, my address is {address}"
print(name_address("Gevorg", "Arabkir 26th 6/2")) 

//2
def name(_name):
    return f"Hi {_name}"
print(name(input("Input a name: ")))

//3
def room_square(width, length):
    return width * length
width = float(input("Input the width: ")) 
length = float(input("Input the length: "))  
print(f"The room square = {room_square(width, length)}") 

//4
def land_square(width, length):
    return width * length
def akr():
    return 43560 * land_square_(width, _length)
_width = float(input("Input the width: ")) 
_length = float(input("Input the length: "))
print(f"The square of land = {akr()}")  

//5
def amount(count_min_1, count_max_1):
    sum = count_min_1 * 0.1 + count_max_1 * 0.25
    return sum
min_from_1 = int(input("Input the count of bottles, that smaller than 1 litre: "))
max_from_1 = int(input("Input the count of bottles, that bigger than 1 litre: "))
print(f"The amount = {amount(min_from_1, max_from_1):.2f}$")

//6
def tip(amount):
    return amount * 18 / 100
def taxes(amount):
    return amount * 20 / 100
amount = int(input("Input the amount of delivery: "))
print(f"Tip = {tip(amount):.2f}")  
print(f"Taxes = {taxes(amount):.2f}")
print(f"Amount = {amount:.2f}")

//7
def sum_1_num(number):
    count = 0
    sum = 0
    res = number
    while count < number:
        sum += res
        count += 1
        res -= 1
    return sum    
num = int(input("Input a number: "))
print(f"The sum from 1 to {num} = {sum_1_num(num)}") 

//8
def weight(count_souvenir, count_trifle):
    qash = count_souvenir * 75 + count_trifle * 112
    return qash
souvenir = int(input("Input the count of souvenir: "))
trifle = int(input("Input the count of trifle: "))
print(f"The weight = {weight(souvenir, trifle)} gram")

//9
def deposit(amount):
    count = 1
    while count <= 3:
        amount += amount * 4 / 100
        print(f"the {count} year deposit = {amount:.2f}")
        count += 1
_deposit = int(input("Input the amount of deposit: "))
deposit(_deposit)

//10
import math
def operations_with_a_b(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} / {b} = {(a / b):.2f}")
    print(f"[{a} / {b}] = {a // b}")
    print(f"logarithm base 10 of {a} = {math.log(a, 10):.2f}")
num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
operations_with_a_b(num1, num2)

//11
def mpg_to_l_100():
    gal = 3.78541178 
    mi = 1.609344
    l_km = gal / mi * 100 #mpg
    return l_km
def l_100(mpg):
    return mpg_to_l_100() / mpg
_mpg = int(input("Input the counf of mpg: "))
print(f"{_mpg} mpg = {l_100(_mpg):.1f} l/100km")

//12
def duym_to_cm(size):
    return size * 2.54
def ft_to_cm(_size):
    return 12 * duym_to_cm(_size)
ft = int(input("Input your tall with ft: "))
duym = int(input("Input your tall with duym: "))
print(f"your given tall with ft = {ft_to_cm(ft)} cm")
print(f"your given tall with duym = {duym_to_cm(duym)} cm")

//13
def ft_to_duym(ft):
    return 12 * ft
def ft_to_yard(ft):
    return 0.333333 * ft
def ft_to_mile(ft):
    return 0.000189394 * ft
_ft = int(input("Input your tall with ft: "))
print(f"{_ft} ft = {ft_to_duym(_ft):.2f} duym")
print(f"{_ft} ft = {ft_to_yard(_ft):.2f} yard")
print(f"{_ft} ft = {ft_to_mile(_ft):.5f} mile")

//14
import math
def circle_area(r):
    area = math.pi * r**2
    return area
def sphere_area(r):
    cal = math.pi * r**3
    area = 4 / 3 * cal
    return area
_r = int(input("Input radius: "))
print(f"The area of circle = {circle_area(_r):.2f}")
print(f"The area of sphere = {sphere_area(_r):.2f}")

//15
import math
def cylinder_volume(r, h):
    area = math.pi * r**2 * h
    return area
_r = int(input("Input radius: "))
_h = int(input("Input height: "))
print(f"The volume of cylinder = {cylinder_volume(_r, _h):.1f}")

//16
import math
def speed(h):
    v0 = 0
    g = 9.8
    v = math.sqrt(v0**2 + 2 * g * h)
    return v
_h = int(input("Input the height: "))  
print(f"The speed is {speed(_h):.2f}")

//17
def area_triangle(b ,h):
    area = (b * h) / 2
    return area
_b = int(input("Input the base of triangle: "))    
_h = int(input("Input the height of triangle: "))  
print(f"The area of trangle is {area_triangle(_b, _h)}")

//18
import math
def area_triangle(s1, s2, s3):
    s = (s1 + s2 +s3) / 2
    area = round(math.sqrt(s * (s - s1) * (s - s2) * (s - s3)), 2)
    return area
_s1 = int(input("Input the first side of triangle: "))    
_s2 = int(input("Input the second side of triangle: "))
_s3 = int(input("Input the third side of triangle: "))
print(f"The area of triangle = {area_triangle(_s1, _s2, _s3)}")

//19
def day_to_sec(day):
    return day * 86400
def hour_to_sec(hour):
    return hour * 3600
def minute_to_sec(minute):
    return minute * 60
_day = int(input("Input day: "))    
_hour = int(input("Input hour: "))
_minute = int(input("Input minute: "))
_second = int(input("Input second: "))
time = day_to_sec(_day) + hour_to_sec(_hour) + minute_to_sec(_minute) + _second
print(f"{_day} day {_hour} hour {_minute} minute {_second} second = {time} second")

//20
from datetime import datetime
def current_date():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    return date
print("date and time =", current_date())

//21
def days_of_month(month):
    if month in ('april', 'june', 'september', 'november'):
        return "30"
    elif month == 'february':
        return "28 or 29"
    return "31"
_month = input("Input a month: ")
print(f"The dyas of {_month} is {days_of_month(_month)}")

//22
def letter_vocal_consonant(letter):
    if letter in ('a', 'e', 'i', 'o', 'u'):
        return "vocal"
    elif letter == 'y':
        return "and vocal and consonant"
    return "consonant"
_letter = input("Input a letter: ")
print(f"The {_letter} is {letter_vocal_consonant(_letter)}")

//23
def season(month):
    if month in ('march', 'april', 'may'):
        return "spring"
    elif month in ('june', 'july', 'august'):
        return "summer"
    elif month in ('september', 'october', 'november'):
        return "autumn"
    return 'summer'
_month = input("Input a month: ")
_day = int(input("Input a day: "))
print(f"The {_month} {_day} is a day of {season(_month)}")

//25
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32
count = 10    
while count <= 100:
    fahrenheit = celsius_to_fahrenheit(count)
    print(f"{count} celsius = {fahrenheit} fahrenheit")
    count += 10
    
//26
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "FIzz"
    elif num % 5 == 0:
        return "Buzz"
    return num
count = 1    
while count <= 100:
    print(fizz_buzz(count))
    count += 1
