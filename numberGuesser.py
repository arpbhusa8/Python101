import random
a=random.randint(1,1000) 
# random.randint(1,1000) --> gives random number between 1 and 10000
# for i in range(10):
#     b=eval(input("enter a number:"))
#     if a>b:
#         print('your number guess is too low')
#     elif a<b:
#         print('your number guess is too high')
#     else:
#         print('you guessed it right')
#         break

#doing the same thing in while loop     
i =0
while i in range(5):
    b=eval(input("enter a number:"))
    i+=1
    if a>b:
        print('your number guess is too low')
    elif a<b:
        print('your number guess is too high')
    else:
        print('you guessed it right')
        break

    