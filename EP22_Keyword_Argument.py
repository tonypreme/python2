# Keyword Arguments


def showitem(fname,lname,city):
    print('ชื่อ :',fname)
    print('นามสกุล:',lname)
    print('จังหวัด :',city)


# showitem("pachara","sangarun","samutsakorn")
# การแสดงผลจะเรียงลำดับ ของตัวแปลที่เรากำหนด 
'''
fname = ลำดับแรก
lname = ลำดับสอง
city = ลำดับสุดท้าย
'''

# หากต้องการระบุ โดยไม่ต้องเรียงลำดับ
showitem(city="ปทุม",lname='ojo',fname='ตูตะตู่ตี้ตู')