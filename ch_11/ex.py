foods = ["김밥", "라면", "떡볶이", "우동"]

print(foods)

foods[foods.index("라면")] = "파스타"
foods[foods.index("우동")] = "냉면"

print(foods)

foods.insert(foods.index("떡볶이"), "순대")

print(foods)