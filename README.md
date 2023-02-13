# آموزش پایتون
## مقدمه و آشنایی
### ویدیو های جالب
- این ویدیو ها رو ببینید (انگلیسی هستن اما اصلا مهم نیست که بفهمید چی گفته میشه، حتی میتونید صداش رو اصلا ببندید. مهم هم نیست که بفهمید هر خط کد که نوشته میشه کارش چیه. میخوام ببینید که وقتی داریم یه برنامه درست میکنیم چه مسیری طی میشه و با این مسیر آشنا بشید. مثلا به ازای چند خط کد یه صفحه ساخته میشه، چند خط دیگه اون صفحه مربع مربع میشه، چند خط دیگه یه شکل رو صفحه اضافه میشه، چند خط دیگه اون شکل رنگی میشه و ...)
    - نمونه بازی مار ساخته شده در 60 خط طی 5 دقیقه با پایتون -> https://www.youtube.com/watch?v=_-KjEgCLQFw
    - نمونه بازی tetris یا همون خونه سازی در 180 خط طی 9 دقیقه با پایتون -> https://www.youtube.com/watch?v=7kGNs5R-AM8
- مقایسه پایتون با بقیه زبان های برنامه نویسی
    - پر کاربرد ترین زبان های برنامه نویسی از 1965 تا 2022 -> https://www.youtube.com/watch?v=qQXXI5QFUfw
    - مقایسه تعداد خطوط، مدت زمان ساخت و مدت زمان اجرای یک کار یکسان با 3 زبان برنامه نویسی مختلف -> https://www.youtube.com/watch?v=3PcIJKd1PKU
### مزایای پایتون
- سادگی و توانایی نوشتن برنامه هایی با تعداد خطوط کم تر در زمان کوتاه تر
- سطح بالا بودن (برای مثال مدیریت حافظه به صورت خودکار انجام میشه و دیگه نیازی نیست ما کاری کنیم)
- توانایی ساخت برنامه برای پلتفرم های مختلف (ویندوز، مک، لینوکس، اندروید، ...)
- کتاب خانه های متعدد
### کاربرد ها و کتاب خانه ها
- Natural Language Processing (پردازش زبان طبیعی)
- Computer Vision (پردازش تصویر)
- GUI (رابط کاربری گرافیکی)
- Game (ساخت بازی)
- Web (وب)
- Data Science (علوم داده)
- Math (ریاضی)
- Machine Learning (یادگیری ماشین)
### نصب پایتون روی سیستم
https://www.python.org/downloads/

موقع نصب گزینه (add python to path) رو هم بزنید.
### محیط های توسعه یا همون IDE ها (هر کدوم که کار کردن باهاش براتون راحت تره رو انتخاب کنید)
### vscode
میشه گفت در حال حاضر محبوب ترین محیط برنامه نویسی برای اکثر زبان هاست:
https://code.visualstudio.com/Download
بعد از نصبش به هر زبانی که بخواید برنامه نویسی کنید پیغام دانلود extension یا افزونه مربوط به اون زبان رو میده که از داخل خودش قابل دانلوده.
### pycharm
نسخه community رایگانه و میتونید اون رو از اینجا دانلود کنید:
https://www.jetbrains.com/pycharm/download
### sololearn code playground
نیازی به نصب نیست و میتونید تحت وب کدتون رو اجرا کنید:
https://www.sololearn.com/compiler-playground/python
### Online Compiler - Code on Mobi
کامپایلر آنلاین برای اندرویده که میتونید از گوگل پلی دانلود کنید:
https://play.google.com/store/apps/details?id=app.compiler

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
other_age = age + 1
print(other_age)
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
### شمارش در دنیای کامپیوتر و برنامه نویسی از صفر شروع میشه
```
01234567...
↓↓↓↓↓
Arash...
```
همچنین:
```
True = 1 = وصل بودن، روشن بودن، درست بودن
False = 0 = قطع بودن، خاموش بودن، غلط بودن
```
### توابع کار با متن
```python
text = "Arash Nemat Zadeh"
print(text) # حالت معمولی
print(text.upper()) # حروف بزرگ
print(text.lower()) # حروف کوچک
print(text.find("Nemat")) # پیدا کردن نوشته
print("Arash" in text) # True
print("Korosh" in text) # False
print(text.replace("Arash","Korosh")) # جایگزین کردن نوشته
```
### عملیات های ریاضی
```python
print("taghsim:", 10 / 3)
print("taghsim rond shode be paeen:", 10 // 3)
print("zarb:", 10 * 3)
print("jam:", 10 + 3)
print("tafrigh:", 10 - 3)
print("baghi mande:", 10 % 3)
print("tavan:", 10 ** 3)
```
اگر توی یه عبارت ترکیب چند تا عملیات ریاضی باشه مشابه چیزی که تو ریاضی خوندیم اول پرانتز حساب میشه، بعد ضرب و تقسیم و نهایتا جمع و تفریق.
### مقایسه
```python
x = input("enter x:")
x = int(x)
print(x == 10) # مساوی
print(x != 10) # مخالف
print(x > 10) # بزرگ تر
print(x >= 10) # بزرگ تر یا مساوی
print(x < 10) # کوچک تر
print(x <= 10) # کوچک تر یا مساوی
```
### عبارات منطقی
```python
x = input("enter x:")
x = int(x)
print(x < 20 and x > 10) # و
print(x > 100 or x < -100) # یا
print(not x == 10) # برعکس
```
### شرط
```python
temperature = 25

if temperature > 30: # اگر
    print("hot")
    print("drink water")
elif temperature > 20: # در غیر این صورت اگر
    print("nice weather")
    print("go and play outside")
else: # در غیر این صورت
    print("cold")
print("end")
```
