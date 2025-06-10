cities = ["ktm", "bkt" ,"pkr"]
print(cities[1])
print(len(cities))
cities.append('damak')
for i in  range(len(cities)):
    cities[i]= "visit " + cities[i] + "!"
print(cities[:])
