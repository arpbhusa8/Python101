def get_evens(numbers):
    evens=[]
    for number in numbers:
        if number%2==0:
            evens.append(number)
    return evens

numbers=[1,2,3,4,5,6,7,8,9,10]
print(get_evens(numbers))





