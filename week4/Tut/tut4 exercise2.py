total = 0
count = 0
score = int(input("ENter score, (enter -9 to end):"))

try:
    while(score != -9):
        total = total + score
        count += 1
        score = int(input("ENter score, (enter -9 to end):"))
    average = total / count
    print(f"tOTAL SUBJECT {count}")
    print(f"tOTAL SUBJECT MARKS {total}")
    print(f"Class average is {average}%")

except:
    print("please enter marks.Otherwise you can't continue this!")