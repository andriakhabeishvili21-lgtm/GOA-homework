#  4)მოსწავლეს შეეკითხეთ მის მიერ მიღებული ქულა,თუ ქულა უდრის 100-ს მაშინ გამოუტანეთ "A Group),თუ იქნება 80-დან 99-მდე მაშინ გამოიტანეთ "B Group",თუ იქნება 40-დან 70-მდე მაშინ "C Group",დანარჩენ შემთხვევაში კი "D Group"

score=int(input("enter your score : "))

if score==100:
    print("A group")
elif score<=99 and score>79:
    print("B group")    
elif score<=70 and score>=40:
    print("C group")
else:
    print("D group")

