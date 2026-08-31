scores = [78, 92, 85, 100, 67]

# 1. 학생 수
print(f"학생 수: {len(scores)}")
# 2. 총점
print(f"총점: {sum(scores)}")
# 3. 최저 점수
print(f"최저 점수: {min(scores)}")
# 4. 최고 점수
print(f"최고 점수: {max(scores)}")
# 5. 평균 점수
print(f"평균 점수: {sum(scores)/len(scores)}")
# 6. 80점 이상인 점수만 반복문으로 출력
over_80_sum = 0
for score in scores:
    if score >= 80:
        over_80_sum += score

print(f"80점 이상 점수의 합: {over_80_sum}")