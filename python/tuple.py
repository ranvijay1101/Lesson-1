pizza = ("Vegetable Pizza", 30, "Italian")
pasta = ("Cheese Pasta", 25, "Italian")
pizza_ingredients = {"flour", "cheese", "tomato", "onion"}
pasta_ingredients = {"pasta", "cheese", "tomato", "pepper"}
print("Recipe 1:", pizza[0])
print("Recipe 2:", pasta[0])
print("All ingredients:", pizza_ingredients | pasta_ingredients)
print("Common ingredients:", pizza_ingredients & pasta_ingredients)
print("Only Pizza:", pizza_ingredients - pasta_ingredients)
print("Only Pasta:", pasta_ingredients - pizza_ingredients)
print("Unique ingredients", pizza_ingredients ^ pasta_ingredients)