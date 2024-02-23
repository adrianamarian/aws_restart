myFruitList=["applie", "banana", "cherry"]
print("Initial list: ",myFruitList)
print(myFruitList)

myFruitList[2]="orange"
print("My updated list is: ", myFruitList)

myFruitList.append("peach")
print(myFruitList)

myFruitList.insert(2,"strawberry")
print(myFruitList)

myFruitList.pop()
print(myFruitList)

tuple1= ("apple", "banana", "pineapple", "apple")
print(tuple1)

print(tuple1.count("apple"))

dictionary1={
    "Akua":"apple",
    "Sanvi":"banana",
    "Paulo":"pineapple"
}
print(dictionary1["Akua"])

print(dictionary1.get("Sanvi"))
dictionary1["Paulo"]= "xxx"

print(dictionary1)

