# Arbitrary Arguments (*kwargs) 

# โดยปกติจะกำหนด ส่งค่าพารามิเตอร์ได้ 1 ตัวเท่านั้น 
# แต่ถ้าใส่ค่า * ดอกจันท์นำหน้า จะสามารถส่งค่ากำหนดได้ไม่จำกัด


# *args อันนี้คือ * อันเดียวนำหน้า ค่าใน paraneter มีได้หลายค่าตัวอย่างด่านล่าง
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

displayData(fname="tony Ja") # ส่งค่าได้ตำเดียว 

# ---------------------------------------------------------------------------
# ตัวอย่างการใช้ **Kwargs
# กรณีระบุหลายรูปแบบ 

'''
บางคนต้องการแสดงแค่ชื่อ ไม่แสดงอายุ
บางคนแสดงทั้งหมดเลย
บางคนไม่อยากให้เห็นที่อยู่ ตัวอย่าง **
'''


# **Kwargs 
# def displayData2(**kwargs):
def displayData2(**item): # ตัวอย่างการเปลี่ยนชื่อตัวรับค่า ต้องมี ** 
    # print(kwargs)
    print(item) 

displayData2(fname="tony 2")
displayData2(fname="tony 2",lname="no2")
displayData2(fname="tony 2",lname="no2",age="27")
displayData2(fname="tony 2",lname="no2",age="27",city="ปทุม")
displayData2(fname="tony 2",lname="no2",age="27",city="ปทุม",status="โสด")
displayData2(singleName="tony 2")

# พอแสดงผล เราจะได้ข้อมูลมาเป็น Dictionary <= ชนิดข้อมูล 
# สามารถตั้งชื่ออะไรก็ได้ อิสระ
# kwargs เป็นค่าเริ่มต้น ไม่มีชื่อที่ชัดเจน เราสามารถแก้ไขชื่อมันได้แต่จำเป็นต้องมี ** นำหน้า 