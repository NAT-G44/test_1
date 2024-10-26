food=["tomato","potato", "carrot"]
print(food)
print(food[1])
food[1]="cucumber"
print(food)
food[0]="onion"
print(food)
food.append("beet")
print(food)
food.extend("string")
print(food)
food.extend(["string", 5])
print(food)
food.remove("beet")
print(food[0:2])
