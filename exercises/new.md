# نکته مهم درباره هوش مصنوعی ها:
استفاده از هوش مصنوعی ها مثل chatGPT نه تنها ممنوع نیست بلکه کاملا توصیه میشه. فقط به 2 تا نکته توجه کنید:
1. قبل از پرسیدن از AI هر چه قدرش رو که میتونید با استفاده از ذهن خودتون حل کنید. هر چه قدر بیشتر از مغزتون کار بکشید ورزیده تر میشه.
2. بعد از گرفتن جواب وقت بذارید و ریز به ریز کاری که کرده رو بفهمید و مهارت اینکه دفعه بعد همون رو خودتون بدون کمک بنویسید رو به دست بیارید.

# تمارین
## نکته: (تا وقتی خودتون تلاش نکردید پاسخ ها رو باز نکنید)

- **برنامه ای بنویسید که اسمتون رو چاپ کنه (یعنی در خروجی نمایش بده).**
<details>
<summary>پاسخ</summary>

محمدطاها زرینی:

```python
print ("Mohammad taha zarini")
```
محمد کهنوی:

```python
print("Mohammad Kahnavi")
#www.coffeete.ir/mohammadkah
```

</details>

---

- **برنامه ای بنویسید که اسمتون رو از ورودی بگیره و بهتون سلام بده، یعنی ورودی و خروجی اش مشابه زیر باشه:**

input: (ورودی)
```
Arash Nemat Zadeh
```
output: (خروجی)
```
Hello Arash Nemat Zadeh
```

<details>
<summary>پاسخ</summary>

پارسا صفائی:
```python
x = input()
print ("Hello" , x)
```
محمدطاها زرینی:

```python
print ("enter your name")
name = input()
print("Hello " + name)
```
محمد کهنوی:
```python
print("Enter your name?")
name = input()
print("Hello" , name)
#www.coffeete.ir/mohammadkah
```

</details>

---

- **2. برنامه ای بنویسید که 2 عدد از ورودی بگیری و جمعشون رو توی خروجی چاپ کنه:**

input:
```
4
5
```
output:
```
9
```

<details>
<summary>پاسخ</summary>

پارسا صفائی:
```python
x = int(input (("")))
y = int(input ())
print (x + y)
```
محمدطاها زرینی:
```python
x = int(input())
y = int(input())
print (x+y)
```
محمد کهنوی:
```python
x = int(input())
y = int(input())
print(x+y)
#www.coffeete.ir/mohammadkah
```

</details>

---

**3. تمرین 2 رو خوانا تر کنید و قبل هر مرحله پیغام مربوط بهش رو هم چاپ کنید:**

input:
```
Adade aval ra vared konid: 4
Adade dovom ra vared konid: 5
```
output:
```
Hasel Jame 2 adad barabar ast ba: 9
```

<details>
<summary>پاسخ</summary>

پارسا صفائی:
```python
x = int (input(("Adade aval ra vared konid: ")))
y = int (input (("Adade dovam ra vared konid: ")))
print (("Hasel Jame 2 adad barabar ast ba: " + str(x+y)))
```
محمدطاها زرینی:
```python
x = int(input("adad avval ra vared konid:"))
y = int(input("adad dovvom ra vared konid:"))
z = str(x+y)
print ("hasel jame barabar ast ba: " + z )
```
محمد کهنوی:
```python
x = int(input("Whrite the first number"))
y = int(input("Whrite the second number"))
z = str(x+y)
print("The sum of them is equal to: " + z)
#www.coffeete.ir/mohammadkah
```

</details>

---

**4. مشابه تمرین قبل رو با نام و نام خانوادگی تون تکرار کنید، یعنی برنامه ای بنویسید که نام و نام خانوادگی تون رو توی ورودی بگیره و نام کاملتون رو در خروجی چاپ کنه:**

input:
```
Name koochak khod ra vared konid: Arash
Name khanevadegi khod ra vared konid: Nemat zadeh
```
output:
```
Name kamele shoma barabar ast ba: Arash Nemat Zadeh
```

<details>
<summary>پاسخ</summary>

پارسا صفائی:
```python
x = input (("Name koochak khod ra vared konid: "))
y = input (("Name khanevadegi khod ra vared konid: "))
print (("Name kamele shoma barabar ast ba: ") + x , y)
```
محمدطاها زرینی:
```python
name1 = str(input("enter your fist name: "))
name2 = str(input("enter your last name: "))
name3 = str(name1+" "+name2)
print ("your complete name is: " + name3)
```
محمد کهنوی:
```python
x = input("Whats your first name?")
y = input("Whats your last name?")
z = print(x,y)
#www.coffeete.ir/mohammadkah
```

</details>

---

**5.برنامه ای بنویسید که 2 عدد رو تو ورودی از ما بگیره و حاصل جمع، ضرب، تفریق، تقسیم، تقسیم همراه با رند کردن، یکی به توان دیگری و باقیمانده تقسیم یکی به دیگری مربوط به اون 2 عدد رو به ما برگردونه**

<details>
<summary>پاسخ</summary>

پارسا صفائی:
```python
x = int (input(("adad bozorg tar ra vared konid (x): ")))
y = int (input(("adad kocheck tar ra vared konid: (y) ")))
print (("hasel jam x ba y =") , str (x + y))
print (("hasel tafrigh x az y =") , str (x - y))
print (("hasel zarb 2 adad barabar ast ba =") , str (x * y))
print (("hasel taghsim x bar y barabar ast ba =") , str (x / y))
print (("hasel taghsim rond shode x bar y =") , str (x // y))
print (("hasel baghi mande taghsim x bar y =") , str (x % y))
print (("hasel x be tavan y =") , str (x ** y))
```
محمد کهنوی:
```python
#Mathematical operations
print("Mohammad Kahnavi")
x = int(input())
y = int(input())
print("sum:",x + y)
print("Subtraction:", x - y)
print("split rand down:",x // y)
print("Times:", x * y)
print("The power off:", x ** y)
print("Divided:", x / y)
print("Remainder:", x % y)
#www.coffeete.ir/mohammadkah
```

</details>

---

**6.برنامه ای بنویسید که یک یا چند string رو در ورودی از ما بگیره و چند تابع یا عملیات دلخواه رو روی اون ها انجام بده. هر چند تا تابع که تونستید یاد بگیرید و پیاده سازی کنید بهتر. هدف از این تمرین اینه که خودتون شروع به سرچ کردن کنید و مطالب جدید رو پیدا کنید. برای مثال میتونید سرچ کنید: string functions in python. اسم هر سایتی که ازش کمک گرفتید رو هم ترجیحا بگید تا من تو فایل جواب ها هفته بعد لینکش رو برای بقیه بچه ها هم بذارم.**

اگر برای این تمرین توضیحات بیشتر نیاز دارید میتونید این ویدیو رو ببینید: https://aparat.com/v/Z1qYE

<details>
<summary>پاسخ</summary>

پارسا صفائی:
```python
name = str (input (("name khod ra vared konid: ")))
print (name.upper())
print (name.lower())
print (name.find ("Parsa"))
print ("Parsa" in name)
print (name.replace( "Parsa", "Safaei"))
print (name.split())
print(name.rfind("Safaei"))
print (name.title())
print (name.isalpha())
print (name.index("Safaei"))
```
مهدی یار برزگر:
```python
x = str(input("inter your name: "))
y = str(input("inter your last name: "))
fullname = x +" "+ y
txt = fullname
x = txt.isnumeric()
print(x)
```
محمد کهنوی:
```python
#String functions
#Center()
text = "Love"
x = text.center(24, "♡")
print(x)
#find()
text = "Hello, My name is Mohammad kahnavi"
x = text.find("m")
print(x)
y = text.find("z")
print(y)
#Make trans()
text = "Hellp Mphammad!"
mytable = str.maketrans("p", "o")
print(text.translate(mytable))
#upper()
text = "Welcome To Alcatraz Prison"
x = text.upper()
print(x)
#lower()
text ="Welcome To Alcatraz Prison"
y = text.lower()
print(y)
#title()
text = "welcome to alcatraz prison"
x = text.title()
#copy()
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
#www.coffeete.ir/mohammadkah
```

</details>

---

**7. برنامه ای بنویسید که نمره شما رو در ورودی ازتون بگیره و با توجه به نمره تون یکی از این ها رو چاپ کنه: 19 تا 20: عالی، 16 تا 18: خیلی خوب، 12 تا 15: خوب، 10 تا 11: متوسط، زیر 10: نیاز به تلاش بیشتر**

<details>
<summary>پاسخ</summary>

محمد کهنوی:
```python
x = int(input("your average is in...level:"))
if 20 >= x >= 18:
    print("Excellent")
elif 18 > x >= 15:
    print("Very good")
elif 15 > x >= 11:
    print("Good")
elif 11 > x >= 9:
    print("Normal")
elif 0 <= x < 9:
    print("Need more effort")
elif x > 20 or x < 0:
    print("The entered number is invalid")
#www.coffeete.ir/mohammadkah
```
پارسا صفائی:
```python
x = int (input(("moadel khod ra vared konid: ")))
if (x) > 20 :
    print ("your mark is wrong")
elif (x) > 18:
    print ("ypur mark is great")
elif (x) > 15:
    print ("your mark is very good")
elif (x) > 11:
    print ("your mark is good")
elif (x) > 9:
    print ("your mark is medium")
elif (x) < 10:
    print ("you need more try")
```
امیررضا شهماردخت:
```python
nomre = int(input('nomre shoma')
If nomre >= 19:
    print('aalliii')
elif nomre == (18 or 17)
    print('bad nist')
else:
    print ('eftezah')
```
امیر حسین عسکری :
```python
x = int(input())
if x <= 20 and >=19):
    print("Excellent")
elif x <=18 and >=16:
    print("Very good")
elif x <=15 and >=12:
    print("Good")
elif x <=11 and >=10:
    print("medium")
if x <= 10:
    print("Need more effort")
print ("end")
```

</details>

---

**8. برنامه ای بنویسید که 5 عدد رو در ورودی از شما بگیره و برای هر کدوم اگر عدد بزرگ تر از صفر بود اون رو توی یه لیست قرار بده. در نهایت محتویات لیست رو چاپ کنه**

<details>
<summary>پاسخ</summary>

پارسا صفائی:
```python
numbers = ['c']
x = int (input())
y = int (input())
m = int (input())
n = int (input())
a = int (input ())
if (x) > 0:
    numbers.append(x)
if (y) > 0:
    numbers.append(y)
if (m) > 0:
    numbers.append(m)
if (n) > 0:
    numbers.append(n)
if (a) > 0:
    numbers.append(a)
    
numbers.remove('c')

print (numbers)
```
محمد کهنوی:
```python
numbers = []
a = int(input())
if a > 0:
    numbers.append(a)
b = int(input())
if b > 0:
    numbers.append(b)
c = int(input())
if c > 0:
    numbers.append(c)
d = int(input())
if d > 0:
    numbers.append(d)
e = int(input())
if e > 0:
    numbers.append(e)
print(numbers)
#www.coffeete.ir/mohammadkah
```

پارسا صفائی:
```python
for i in range (5):
    x = input ("nam")
for i in range (5) :
    y = input ("name khanevadegi")
    
print ("name kamel shoma barabar ast ba: " + x , y)
```

</details>

---

**9. برنامه ای بنویسید که 5 بار هر بار نام کوچک و نام خانوادگی رو در ورودی از ما بگیره و در خروجی نام کامل رو چاپ کنه**

<details>
<summary>پاسخ</summary>

محمد کهنوی:
```python
for i in range (5):
    x = input("Enter your name:")
    print(x)
#www.coffeete.ir/mohammadkah
```

</details>

---


**10. برنامه ای بنویسید که از 1 تا 100 اعداد بخش پذیر به 7 را چاپ کند**

<details>
<summary>پاسخ</summary>

محمد کهنوی:
```python
for x in range(1, 101):
    if x % 7 == 0:
        print(x)
#www.coffeete.ir/mohammadkah
```
جوابی که تو کلاس با هم نوشتیم:
```python
for i in range(100):
    x = i + 1
    if x % 7 == 0:
        print(x,"hast+++++++++")
    # elif x % 7 > 0:
        # print(x,"nist")
```

</details>

---

**11. برنامه ای بنویسید که شکل های زیر را چاپ کند:**
```
a)
*
**
***
****
*****
```
```
b)
*****
****
***
**
*
```
```
c)
    *
   **
  ***
 ****
*****
```
```
d)
*****
 ****
  ***
   **
    *
```

<details>
<summary>پاسخ</summary>

محمد کهنوی:
```python
# C)
i = 1
while i <= 5:
    print(i * "*")
    i = i + 1
# d)
i = 5
while i >= 1:
    print(i * "*")
    i = i - 1
#www.coffeete.ir/mohammadkah
```
امیررضا شهماردخت:
```python
For i in range(6):
    Print((i-1) * '*'

For i in range(6):
    Print((i+1) * '*'
```
جواب سر کلاس:
```python
print("a:")
i = 1
while i <= 5:
    print(i * "*")
    i = i + 1

print("b:")
i = 5
while i >= 1:
    print(i * "*")
    i = i - 1

print("c:")
i = 1
while i <= 5:
    print((5 - i) * " " + i * "*")
    i = i + 1

print("d:")
i = 5
while i >= 1:
    print((5 - i) * " " + i * "*")
    i = i - 1
```

</details>

---

**12. برنامه ای بنویسید که تابعی به نام prime تعریف کنه که کارش گرفتن عدد و تشخیص دادن این که اون عدد اول هست یا نه باشه. سپس از این تابع یکبار در همون فایل و یکبار دیگه تو یک فایل دیگه با استفاده از import کردن استفاده کنید.**

<details>
<summary>پاسخ</summary>

خودم:
```python
# file 1 named functions.py
from math import sqrt

def prime(x):
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

# file 2 named main.py
import functions

x = int(input("enter your number: "))
if functions.prime(x):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")
```
محمد کهنوی:
```python
import math
def prime():
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
x = int(input())
print(prime())
#www.coffeete.ir/mohammadkah
استفاده از تابع تعریف شده در یک فایل دیگه:
from text import prime
prime()
```

</details>

---

**13. برنامه ای بنویسید که با استفاده از tkinter یک پنجره تو صفحه ایجاد کنه، توی پنجره یک دکمه و یک جای خالی برای وارد کردن نوشته داشته باشه. ما داخل جای خالی اسممون رو وارد کنیم و با زدن دکمه به ما سلام بده، مثلا ما وارد کنیم Arash و اون با زدن دکمه پیغام Hello Arash رو نمایش بده.**

<details>
<summary>پاسخ</summary>

خودم:
```python
from tkinter import *
from tkinter import messagebox

def hello():
    name = blank_space.get()
    messagebox.showinfo("hello window","hello " + name)

win = Tk()

blank_space = Entry(win)
blank_space.pack()

hello_button = Button(win, text="say hello", command=hello)
hello_button.pack()

win.mainloop()
```
امیدرضا قربانی (با کمک chatGPT):
```python
import tkinter as tk

def say_hello():
    name = name_entry.get()
    greeting = "Hello " + name
    greeting_label.config(text=greeting)

root = tk.Tk()
root.title("Greeting App")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

greeting_label = tk.Label(root)
greeting_label.pack()

hello_button = tk.Button(root, text="Say Hello", command=say_hello)
hello_button.pack()

root.mainloop()
```

</details>

---

**14. برنامه ای بنویسید که توش مکان 2 تا مهره شطرنج رو بهش بدیم و بگه که مهره اول میتونه دومی رو بزنه یا نه؟ مهره اول رو یکبار رخ، اسب، فیل و وزیر در نظر بگیرید و برای هر حالت حل کنید. (فرض کنید فقط همین 2 مهره توی صفحه وجود دارند و حالت های خیلی خاص و نادر شطرنج رو هم نیاز نیست در نظر بگیرید. برای حالت کلی حل کنید.) - نحوه حرکت مهره ها در شطرنج اگه نمیدونید: https://docs.kde.org/trunk5/en/knights/knights/piece-movement.html**

<details>
<summary>پاسخ</summary>

خودم:
```python
# first piece of chess
p1 = input()
p1 = [int(x) for x in p1.split()]
# second piece of chess
p2 = input()
p2 = [int(x) for x in p2.split()]

# gets p1 and p2 as list
def rook(p1, p2):
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return True
    else:
        return False
    
# gets p1 and p2 as list
def bishop(p1, p2):
    if abs(p1[0] - p2[0]) == abs(p1[1] - p2[1]):
        return True
    else:
        return False
    
# gets p1 and p2 as list
def queen(p1, p2):
    if rook(p1, p2) or bishop(p1, p2):
        return True
    else:
        return False
    
# gets p1 and p2 as list
def knight(p1, p2):
    if abs(p1[0] - p2[0]) == 2 and abs(p1[1] - p2[1]) == 1:
        return True
    elif abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 2:
        return True
    else:
        return False

print("If p1 is a rook:")
if rook(p1, p2):
    print("p1 can capture p2\n")
else:
    print("p1 can not capture p2\n")

print("if p1 is a bishop:")
if bishop(p1, p2):
    print("p1 can capture p2\n")
else:
    print("p1 can not capture p2\n")

print("if p1 is a queen:")
if queen(p1, p2):
    print("p1 can capture p2\n")
else:
    print("p1 can not capture p2\n")

print("if p1 is a knight:")
if knight(p1, p2):
    print("p1 can capture p2\n")
else:
    print("p1 can not capture p2\n")
```
سر کلاس با هم:
```python
s = input()
s = s.split()
for i in range(2):
    s[i] = int(s[i])

d = input()
d = d.split()
for i in range(len(d)):
    d[i] = int(d[i])

def rook(s, d):
    if s[0] == d[0] or s[1] == d[1]:
        return True
    else:
        return False

def fil(s, d):
    if abs(s[0] - d[0]) == abs(s[1] - d[1]):
        return True
    else:
        return False

def queen(s, d):
    if rook(s, d) or fil(s, d):
        return True
    else:
        return False
    
def knight(s, d):
    if abs(s[0] - d[0]) == 2 and abs(s[1] - d[1]) == 1:
        return True
    elif abs(s[0] - d[0]) == 1 and abs(s[1] - d[1]) == 2:
        return True
    else:
        return False
    
print("if s is a rook:")
if rook(s, d):
    print("s can capture d.")
else:
    print("s can not capture d.")

print("if s is a fil:")
if fil(s, d):
    print("s can capture d.")
else:
    print("s can not capture d.")

print("if s is a queen:")
if queen(s, d):
    print("s can capture d.")
else:
    print("s can not capture d.")

print("if s is a knight:")
if knight(s, d):
    print("s can capture d.")
else:
    print("s can not capture d.")
```
امیدرضا قربانی (با کمک chatGPT):
```python
def can_capture(piece1, piece2):
    x1, y1 = piece1
    x2, y2 = piece2
    if x1 == x2 or y1 == y2:
        return True
    elif abs(x1 - x2) == abs(y1 - y2):
        return True
    else:
        return False
pieces = [('rook', 1, 1), ('knight', 3, 3), ('bishop', 5, 5), ('queen', 7, 7)]
for i in range(len(pieces)):
    for j in range(i+1, len(pieces)):
        if can_capture(pieces[i][1:], pieces[j][1:]):
            print(f"{pieces[i][0]} can capture {pieces[j][0]}")
        else:
            print(f"{pieces[i][0]} cannot capture {pieces[j][0]}")
```
محمد کهنوی:
```python
#Queen
s1 = input()
s2 = input()
x1, y1 = s1.split()
x2, y2 = s2.split()
x1, x2 = int(x1), int(x2)
y1, y2 = int(y1), int(y2)
count = 0
if x1 == x2 or y1 == y2 or x1 - y2 == x2 - y1 or y1 - x2 == y2 - x1 or y2 - x1 == y1 - x2 or x2 - y1 == x1 - y2:
    count = count + 1
if count == 1:
    print("You can hit the nut")
else:
    print("You can't hit the nut")
#Rook
s1 = input()
s2 = input()
x1, y1 = s1.split()
x2, y2 = s2.split()
x1, x2 = int(x1), int(x2)
y1, y2 = int(y1), int(y2)
count = 0
if x1 == x2 or y1 == y2:
    count = count + 1
if count == 1:
    print("You can hit the nut")
else:
    print("You can't hit the nut")
#chess bishop
s1 = input()
s2 = input()
x1, y1 = s1.split()
x2, y2 = s2.split()
x1, x2 = int(x1), int(x2)
y1, y2 = int(y1), int(y2)
count = 0
if x1 - y2 == x2 - y1 or y1 - x2 == y2 - x1 or y2 - x1 == y1 - x2 or x2 - y1 == x1 - y2:
    count = count + 1
if count == 1:
    print("You can hit the nut")
else:
    print("You can't hit the nut")
#knight
s1 = input()
s2 = input()
x1, y1 = s1.split()
x2, y2 = s2.split()
x1, x2 = int(x1), int(x2)
y1, y2 = int(y1), int(y2)
count = 0
if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
    count = count + 1
if count == 1:
    print("You can hit the nut")
else:
    print("You can't hit the nut")
#www.coffeete.ir/mohammadkah
```


</details>

---

