# Arbitrary Arguments (*kwargs) 

# โดยปกติจะกำหนด ส่งค่าพารามิเตอร์ได้ 1 ตัวเท่านั้น 
# แต่ถ้าใส่ค่า * ดอกจันท์นำหน้า จะสามารถส่งค่ากำหนดได้ไม่จำกัด

def add(*number):
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

add(10,5) 
# โดยปกติ number จะรับได้ค่าเดียวแต่พอใส่ *number นำหน้าสามารถส่งค่าได้ไม่จำกัด 
add(10,5,6) 

# แบบปกติ 
def displayData(fname):
    print(fname)

displayData("tony Ja") # ส่งค่าได้ตำเดียว 