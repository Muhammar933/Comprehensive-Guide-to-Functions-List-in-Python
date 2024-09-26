#here is a Simple List 
Fruit = ["Mango","Banana","Orange"]
print(Fruit)

#Accsessing list Elements
print(Fruit[0])
print(Fruit[1])
print(Fruit[2])

#Here is a list methods
#There are Nine methods
#append()
#insert()
#remove()
#pop()
#sort()
#reverse()
#index()
#count()
#clear()

#Now we are going to do code in first method
Food = ["Biryani", "Korma", "Karhai"]
Food.append("Kabab")
print(Food)

#Now we are going to do code in Second method
Fast_food = ["Pizza", "Pasta", "Zingar Burger"]
Fast_food.insert(2, "Sandwich")
print(Fast_food)

#Now we are going to do code in Third method
Food = ["Biryani", "Korma", "Karhai"]
Food.remove("Korma")
print(Food)

#Now we are going to do code in Fourth method
Fast_food = ["Pizza", "Pasta", "Zingar Burger"]
Fast_food.pop(2)
print(Fast_food)


#Now we are going to do code in Fifth method
Numbers = [0 ,4,5,2,9,3,7,1,8,6,10]
Numbers.sort()
print(Numbers)


#Now we are going to do code in Six method
Numbers = [0 ,4,5,2,9,3,7,1,8,6,10]
Numbers.reverse()
print(Numbers)

#Now we are going to do code in Seven method
fruits = ["apple", "banana", "mango"]
position = fruits.index("banana")
print(position)

#Now we are going to do code in Eight method
Fast_food = ["Pizza", "Pasta", "Pasta" , "Zingar Burger"]
Count_food = Fast_food.count("Pasta")
print(Count_food)

#Now we are going to do code in Nine method
Fast_food = ["Pizza", "Pasta", "Zingar Burger"]
Fast_food.clear()
print(Fast_food)
