name = input("ชื่อนักเรียน: ")
middle = input("คะแนนสอบกลางภาค (40): ")
final = input("คะแนนสอบปลายภาค (60): ")
total_score = int(middle) + int(final)
percent_score = (total_score/100)*100
print ("-------------------------------")
print(f"นักเรียน: {name} | คะแนนรวม: {total_score}%")
print ("คะแนนของคุณอยู่ที่", percent_score, "%")
if percent_score >=80:
    print ("เกรดของคุณคือ:A")
elif percent_score >75:
    print ("เกรดของคุณคือ:B+")
elif percent_score >70:
    print("เกรดของคุณคือ:B")
elif percent_score >65:
    print("เกรดของคุณคือ:C+")
elif percent_score >60:
    print("เกรดของคุณคือ:C")
elif percent_score >55:
    print("เกรดของคุณคือ:D+")
elif percent_score >50:
    print("เกรดของคุณคือ:D")
else:
    print("เกรดของคุณคือ:F (ติดต่ออาจารย์ประจำรายวิชาเพื่อทำการแก้ไข)")