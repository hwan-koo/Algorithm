score = {}
score["A+"] = 4.5
score["A0"] = 4
score["B+"] = 3.5
score["B0"] = 3
score["C+"] = 2.5
score["C0"] = 2
score["D+"] = 1.5
score["D0"] = 1
score["F"] = 0
sum = 0
point_sum = 0
for _ in range(20):
    name, point, degree = input().split()
    point = float(point)
    point_sum += point
    if degree == "P":
        point_sum -= point
        continue
    sum += score[degree] * point

print(round(sum/point_sum,6))