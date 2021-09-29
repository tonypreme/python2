# รับและการเรียงลำดับตัวเลข

number=[]
while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0: # ทำไว้เพื่ออกจาก loop ถ้าใส่ค่าต่ำกว่า 0 
        break
    number.append(x) # .append นำตัวเลขที่ป้อนใส่ลงไปใน number 

print("ก่อนเรียง=>",number)

number.sort() # .sort คือการเรียงตัวเลข ใน list  (น้อยไปมาก)
# ** ต้องใช้คำสั่ง .sort ก่อนไม่งั้นค่าข้อมูลจะเพี้ยน
print("น้อยไปมาก=>",number) 

number.reverse() # เรียงจากมากไปน้อย ** ต้อง เรียงจากน้อยไปมากก่อน
print("มากไปน้อย=>",number)
print("จบโปรแกรม")
