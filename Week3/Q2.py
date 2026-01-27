#question 2 : shopping Card (list- Searching and Removal)
cart = ["apple","banana","milk","eggs"]
print("number of apples",cart.count("apple"))
print("position of milk",cart.index("milk"))
cart.remove("apple")
print("removed item using  pop",cart.pop)
print("Is banana in the cart ?","Banana" in cart)
print("final cart",cart)