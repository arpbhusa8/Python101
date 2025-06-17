cityPop={
    'kathmandu':30000,
    'bharatput':200000,
    'pokhara':23321312
}

def printdata(dictionary):
        
    for data in dictionary:
        print(data)
        print(cityPop.get(data,"no data found for this"))

def addCity(dictionary):
    a=str(input("Please enter the city name : "))
    b=int(input("please give the population for the city : "))
    dictionary[a]=b
    return dictionary

printdata(cityPop)
addCity(cityPop)
printdata(cityPop)