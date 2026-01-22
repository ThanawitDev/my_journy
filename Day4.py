total_saving = 0

for i in range(1,8):
    save_money =int(input(f"วันนี้วันที่{i} ออมเงินได้กี่บาท:"))
    total_saving = total_saving + save_money
    if save_money >= 100:
        print ("เยี่ยมมาก")
    else:
        print ("เก็บต่อไป")
print ("ยอดเงินรวมใน7วันของคุณคือ", total_saving, "บาท")
    