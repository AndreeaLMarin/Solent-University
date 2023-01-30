car = {
    "make" : "dacia",
    "model" : "logan",
    "year":2021
}
x = car["make"]
print(x)

print(car.keys())
print(car.values())
print(car.items())


car["make"] = "ford"
car["owner"] = "Marcel"
car.pop("year")
