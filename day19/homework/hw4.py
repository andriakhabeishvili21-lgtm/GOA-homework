# 4) მომხმარებელს შემოატანინეთ ელფოსტის მისამართი და გადაამოწმეთ შეიცავს თუ არა '@' სიმბოლოს, შედეგი კი დაბეჭდეთ დიდი ასოებით.

email=input("enter ut email : ")
u=email.find("@")
if u >= 1:
    print("true".upper)
else:
    print("error")
