scores = []

for i in range(5):
    score = int(input("점수를 입력하세요: "))
    scores.append(score)

print(f"입력된 점수: {scores}")
print(f"학생 수: {len(scores)}")
print(f"총점: {sum(scores)}, 최저 점수: {min(scores)}, 최고 점수: {max(scores)}")
print(f"평균 점수: {sum(scores)/len(scores)}")

print(f"80점 이상 점수:", end=" ")
for score in scores:
    if score >= 80:
        print(f"{score}", end=", ")

print()

scores.sort()
print(f"정렬된 점수: {scores}")