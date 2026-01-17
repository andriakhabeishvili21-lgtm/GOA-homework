# 1)შექმენით სია, 10 ელემენტით, ნებისმიერი მონაცემთა ტიპის, შემდეგ მომხარებელს შემოატანინეთ 2 ცალი რიცხვი, პირველი რიცხვი რაც შემოიტანეს მაგ ინდექსზე მდგომი ელემენტი გამოიტანეთ, და  მეორე რიცხვი რაც შემოიტანეს სიაში მაგ ინდექსზე მდგომი ელემენტი შეცვალეთ "new element" ით

schoolUtencils=["books" , "notebooks" , "pencils" , "pens", "pencilcase" , "backpack" "eraser", "ruler" ,"markers" , "notes"] 

num=int(input("enter a number 1-10 : "))


print(schoolUtencils[num])


num1=int(input("enter another number 1-10 : "))
schoolUtencils[num1] = "new element"
