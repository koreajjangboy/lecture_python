import statistics

scores = [85, 92, 78]
print(scores)
print(statistics.mean(scores))  # 평균

del scores[1]  # 인덱스 1의 요소 삭제
print(scores)


fruits = ["사과", "바나나", "사과", "포도"]
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)