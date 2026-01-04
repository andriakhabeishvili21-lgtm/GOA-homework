#   3)მომხმარებელს შეეკითხეთ ასაკი,თუ ასაკი მეტი ან ტოლი იქნება 18-ზე,გამოიტანეთ "უნივერსიტეტი" თუ ქინება 7ის ტოლი მაშინ "სკოლა",დანარჩენ შემთხვევაში "ბაღი"

age=int(input("enter your age : "))

if  age >= 18:
    print("university")
elif  age==7:
    print("school")    
else:
    print("kindergarden")    