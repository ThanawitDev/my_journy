print ("ระบบคำนวณคะแนนเฉลี่ยของนักเรียน")
print ("--------------------------------")
first_score = input("คะแนนสอบครั้งที่ 1: ")
second_score = input("คะแนนสอบครั้งที่ 2: ")
third_score = input("คะแนนสอบครั้งที่ 3: ")
total_score = int(first_score)+int(second_score)+int(third_score)
point_average = total_score/3
print ("---สรุปผล---")
name =input("ชื่อนักเรียน: ")
print ("คะแนนรวม", total_score)
print ("คะแนนเฉลี่ย", point_average)

