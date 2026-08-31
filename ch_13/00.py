products = [
    {"name" : "세제", "price" : 35000, "stock" : 3},
    {"name" : "비누", "price" : 10000, "stock" : 2},
    {"name" : "책", "price" : 40000, "stock" : 0}]

for product in products:
    if product["price"] >= 30000:
        print(product["name"])


for product in products:
    if product["stock"] <= 0 :
        print(product["name"])