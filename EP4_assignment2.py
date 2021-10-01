# หาค่าตัวเลขต่ำสุด-สูงสุด และผลรวม

number=[]
while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0: # ทำไว้เพื่ออกจาก loop ถ้าใส่ค่าต่ำกว่า 0 
        break
    number.append(x) # .append นำตัวเลขที่ป้อนใส่ลงไปใน number 

print("ค่าปกติ รวมทั้งหมด=>",number)


print("ค่ามากที่สุด =>",max(number)) # ค่ามากที่สุด
print("ค่าน้อยที่สุด =>",min(number)) # ค่าน้อยที่สุด 
print("ค่าน้อยที่สุด =>",sum(number)) # ผลรวม

print("จบโปรแกรม")