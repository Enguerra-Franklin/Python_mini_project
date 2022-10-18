from os import remove


flavors = ["chocolate", "vanilla", "mango", "apple", "ube"]
print(flavors)
print(flavors[0])
flavors.append("pineapple")
print(flavors)
flavors.remove("mango")
print(flavors)
count = len(flavors)
for flavors in flavors:
    print(flavors)