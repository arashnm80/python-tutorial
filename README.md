# آموزش پایتون
## نصب پایتون روی سیستم
https://www.python.org/downloads/

موقع نصب گزینه (add python to path) رو هم بزنید.
## محیط های توسعه یا همون IDE ها (هر کدوم که کار کردن باهاش براتون راحت تره رو انتخاب کنید)
### pycharm
نسخه community رایگانه و میتونید اون رو از اینجا دانلود کنید:

https://www.jetbrains.com/pycharm/download
### vscode
https://code.visualstudio.com/Download
### sololearn code playground
نیازی به نصب نیست و میتونید تحت وب کدتون رو اجرا کنید:

https://www.sololearn.com/compiler-playground/python

## شروع برنامه نویسی
### نوشتن متن روی صفحه
```python
print("hello world!")
```
### کامنت گذاری
```python
print("این خط اجرا میشه")
# print("این خط اجرا نمیشه")
```
### استفاده از متغیر
```python
age = 20
print(age)
```
### انواع متغیر ها
```python
age = 20 # integer
score = 19.25 # float
name = "Arash" # string
status = False # boolean
```
### گرفتن ورودی از کاربر
```python
print("enter your age:")
age = input()
print("your age is:", age)
```
### محاسبه سن از روی تاریخ تولد
```python
birthday = input("enter your birthday: ")
age = 2023 - int(birthday)
print(age)
```
یکبار هم به جای `int(birthday)` بنویسید `birthday` تا خطایی که میده رو ببینید
### توابع تبدیل نوع متغیر ها
```python
int() # تبدیل به عدد صحیح
float() # تبدیل به عدد اعشاری
bool() # تبدیل به غیر بولین (درست یا غلط)
str() # تبدیل به متن
```
### توابع کار با متن
```python
text = "Arash Nemat Zadeh"
print(text) # حالت معمولی
print(text.upper()) # حروف بزرگ
print(text.lower()) # حروف کوچک
```
