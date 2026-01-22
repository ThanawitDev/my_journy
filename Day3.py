name = input("ชื่อนักเรียน: ")
score = int(input("กรอกคะแนนสอบ(เต็มร้อยคะแนน): "))
print ("-----------------------------------------")
if score >80:
    print ("คุณได้เกรด: A")
elif score >=75:
    print ("คุณได้เกรด: B+")
elif score >=70:
    print ("คุณได้เกรด: B")
elif score >=60:
    print ("คุณได้เกรด: C")
elif score >=50:
    print ("คุณได้เกรด: D")
else:
    print ("คุณได้เกรด: F")