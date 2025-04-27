quiz = input("გამარჯობა, მოდი ვითამაშოთ სახალისო ქვიზი!(Y/N): ")
if quiz == "N":
    print("კარგი, თუ გადაიფიქრებ მითხარი!")
    exit()
else:
    print("მოდი დავიწყოთ!")

print("ტესტში არის 10 შეკითხვა, მაქსიმალური ქულა 100") 

score = 0

# კითხვა 1
print("რა არის Python?")
print("1.	ვირუსი")
print("2.	პროგრამირების ენა")
print("3.	გველი")
print("4.	საიტი")
answer = input("შეიყვანეთ სწორი პასუხი(1-4): ")
if answer == "2":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 2
print("რა ენით იწერება ვებსაიტის სტილი?")
print("1.	Html")
print("2.	Css")
print("3.	Java")
print("4.	Python")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "2":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 3
print("რა არის Html?")
print("1.	პროგრამირების ენა")
print("2.	საიტის დიზაინი")
print("3.	ვებსაიტის სტრუქტურა")
print("4.	ვებ-სერვერი")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "3":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 4
print("რა არის Css?")
print("1.	სტილის ფაილი")
print("2.	ვებ-დიზაინი")
print("3.	ვირუსი")
print("4.	გრაფიკული პროგრამა")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "1":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 5
print("რას გამოიტანს ეს კოდი: print(2 + 4)?")
print("1.	8")
print("2.	6")
print("3.	10")
print("4.	4")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "2":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 6
print("რას აბეჭდავს print('3' + '4')?")
print("1.	7")
print("2.	34")
print("3.	Syntax Error")
print("4.	12")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "2":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 7
print("რა არის ცვლადი Python-ში?")
print("1.	ფაილი, რომელიც ინახავს მონაცემებს გარე ბაზაში")
print("2.	ფუნქცია, რომელიც ამუშავებს მონაცემებს")
print("3.	სიმბოლო, რომელიც წარმოადგენს ლოგიკურ ოპერატორს")
print("4.	ობიექტი, რომელიც ინახავს მონაცემს")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "4":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 8
print("რომელი თეგი გამოიყენება Html-ში სათაურისთვის?")
print("1.	<title>")
print("2.	<h1>")
print("3.	<p>")
print("4.	<head>")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "2":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 9
print("რას გამოიტანს კოდი: len('hello')?")
print("1.	4")
print("2.	5")
print("3.	6")
print("4.	Error")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "2":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# კითხვა 10
print("რომელი ფუნქცია აბრუნებს მთელი რიცხვის ტიპს?")
print("1.	float()")
print("2.	str()")
print("3.	int()")
print("4.	bool()")
answer = input("შეიყვანე სწორი პასუხი(1-4): ")
if answer == "3":
    print("სწორია ✅")
    score += 10
else:
    print("არასწორია ❌")
    score -= 5

# ქულა უარყოფითი რომ არ იყოს
if score < 0:
    score = 0

# საბოლოო ქულა
print(f"საბოლოო ქულა: {score}")

if score == 100:
    print("შესანიშნავია! შენ მიიღე მაქსიმალური ქულა")
elif score >= 80:
    print("ყოჩაღ! მაღალი ქულა გაქვს")
elif score >= 50:
    print("კარგი შედეგია, მაგრამ შეგიძლია უკეთესი შედეგიც აჩვენო")
else:
    print("დასაწყისთვის კარგია. სწავლა გააგრძელე და გაუმჯობესდები")
