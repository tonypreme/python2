# กลุ่มเลขคู่-เลขคี่

number=[] # [] <=  ตัวแปรชนิดข้อมูล list
odd=[] # เลขคี่
even=[] # เลขคู่

while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0: # ทำไว้เพื่ออกจาก loop ถ้าใส่ค่าต่ำกว่า 0 
        break
    if x%2 ==0: # ถ้าค่า x หาร 2 ลงตัวจะเป็นเลขคู่ ให้ add ค่าไว้ใน even
        even.append(x)
    else : # ถ้าค่า x หาร 2 ไม่ลงตัวจะเป็นเลขคี่ ให้ add ค่าไว้ใน odd
        odd.append(x)

    number.append(x)

print("ตัวเลขทั้งหมด =>",number)
print("จำนวนเลขคู่",even)
print("จำนวนเลขคี่",odd)
