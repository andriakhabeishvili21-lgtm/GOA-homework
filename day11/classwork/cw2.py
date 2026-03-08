# 2)მომხარებელს შემოატანინე რიცხვი, და თუ ეს რიცხვი  მეტია 15 ზე, 1 დან ან რიცხვამდე ყველა რიცხვი დაპრინტეთ  ფორ ლუპით

number=int(input( "enter a number:  " ))

if number > 15:
    for i in range (1, number):
        print(i)
                 
          
else:
    print("nothing")    