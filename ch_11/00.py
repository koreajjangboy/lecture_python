import statistics

scores =[86,92,78,66,77,88,99,100,55,25]

count_high = 0
count_low = 0

sum_high = 0
sum_low = 0

med_score = statistics.median(scores)
print(f"중간값 : {med_score}")

for score in scores:
    if score >= med_score:
        count_high += 1
        sum_high += score
    else:
        count_low += 1
        sum_low += score

print(f"상위 점수 학생수 : {count_high} 합계 : {sum_high} 평균 : {sum_high/count_high}")
print(f"하위 점수 학생수 : {count_low} 합계 : {sum_low} 평균 : {sum_low/count_low}")