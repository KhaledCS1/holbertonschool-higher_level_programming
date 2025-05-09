# python-if_else_loops_functions
تم انشاء هذا المجلد لتعزيز المهارات التي تعلمتها في معسكر Holberton by Tuwaiq Academy تحديدا في كورس الPython تعلم مفاهيم الif Statement و الLoops و الFunctions في لغة البايثون
# الاهداف التعليمية :
1- استخدام المكتبات مثل مكتبة random
2-  استخدام وفهم الشروط if/elif/else
3- استخدام و فهم الLoops
4- فهم الFunctions
5- التعامل مع مفاهيم مثل F-string
# Task 0
 بناء برنامج بسيط يحدد اذا كانت الارقام موجبة سالبة او تساوي صفر ويطبع النتيجة المناسبة واسم الملف هو 0-positive_or_negative.py

🧾 شرح الاكواد سطرا بسطر :
'''
#!/usr/bin/python3
'''
   هذا يسمى Shebang يحدد يجب ان يشتغل باستخدام البايثون الموجود بهذا المسار
  

3. import random
   استيراد مكتبة random التي تدخل ارقام عشوائية

4. number = random.randint(-10, 10)
   توليد رقم عشوائي بين -10 و 10 وتخزينه في المتغير number.

5. if number > 0:
   التحقق إذا كان الرقم موجبًا.

6. print(f"{number} is positive")
   طباعة رسالة أن الرقم موجب باستخدام تنسيق f-string.

7. elif number == 0:
   شرط بديل إذا كان الرقم يساوي صفر.

8. print(f"{number} is zero")
   طباعة أن الرقم هو صفر.

9. else:
   إذا لم يكن موجبًا أو صفرًا، فبالتالي هو سالب

10. print(f"{number} is negative")
   طباعة أن الرقم سالب

📌 امثلة على الoutputs :
 -4 is negative
0 is zero
7 is positive
