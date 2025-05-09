# Directory: python-if-else-loops-functions
تم انشاء هذا المجلد لتعزيز المهارات التي تعلمتها في معسكر Holberton by Tuwaiq Academy 
تحديدا في كورس الPython لتعلم مفاهيم اساسية مثل الif Statement و الLoops و الFunctions في لغة البرمجة Python


# الاهداف التعليمية :

استخدام المكتبات مثل مكتبة random

استخدام وفهم الشروط if/elif/else

استخدام و فهم الLoops

فهم الFunctions و التعامل مع مفاهيم مثل F-string



# Task 0
 بناء برنامج بسيط يحدد اذا كانت الارقام موجبة سالبة او تساوي صفر ويطبع النتيجة المناسبة واسم الملف هو 0-positive_or_negative.py


# شرح الاكواد سطرا بسطر :

هذا يسمى Shebang يحدد يجب ان يشتغل باستخدام البايثون الموجود بهذا المسار

```#!/usr/bin/python3```

  استيراد مكتبة random التي تدخل ارقام عشوائية 
  
```import random```

    توليد رقم عشوائي بين -10 و 10 وتخزينه في المتغير number
    
```number = random.randint(-10, 10)```

شرط اذا كانت number اكبر من 0 (عدد موجب)

```if number > 0:```

تعني اطبع قيمة المتغير الموجبة باستخدام F-string

```print(f"{number} is positive")```


   شرط في حال لم يتحقق الشرط الاول ويعني اذا المتغير يساوي 0 
   
```elif number == 0:```

اطبع قيمته 

```print(f"{number} is zero")```


اذا الشرط الاول والثاني  لم يتحققوا وبالطبع هذا يعني بان الاعداد ليست موجبة ولا تساوي صفر فاذا هو بالتالي سيكون سالب

```
else:
print(f"{number} is negative")
```


📌 امثلة على الoutputs :
```
-4 is negative
0 is zero
7 is positive
```
