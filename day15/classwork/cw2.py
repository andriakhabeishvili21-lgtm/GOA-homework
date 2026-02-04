# 2)იგივე რაც ზემოთა მაგრამ პიქირით, სიაში ამოჭერით ელემენტი მომხარებლის მეორე შემოტანილი რიცხვის ინდექსიდან მომხარებლის პირველი შემოტანილი რიცხვის ინდექსამდე

# მაგ:  input1: 6
#      input2: 3
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# output: 4, 5, 6

numbers=[1,2,3,4,5,6,7,8,9,10]

num=int(input("enter a number 1-10 : "))
num1=int(input('enter a number 1-10 thats less than ur last pick : '))

print(numbers[num1:num])
