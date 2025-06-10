def multiply(x,y):
    return x*y

def is_adult(age):
    if age>=18:
        return True
    else:
        return False

a =eval(input('enter your number => '))
b =eval(input('enter you another number => '))
print(f' the multiplied version of the given variables are {multiply(a,b)}')
print(f'the kid arpan is an adult? {is_adult(a)}')
