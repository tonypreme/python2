# Default Parameter

'''
การกำหนดค่าเริ่มต้น
*** กรณีเราสร้างตัวแปรในฟังชั่นไว้ ถ้าเราไม่ใส่ค่าลงไป จะเกิด Error
เราจึงต้องมีการ กำหนดค่าเริ่มต้นไว้ 
เพื่อถ้าเราไม่ใส่ข้อมูล ตัวแปร ก็จะมีค่าในข้อมูลของมันเองได้ ***
'''

def Showdata(fname,lname,city="Bangkok"): # city มีการกำหนดค่าเริ่มต้นไว้ 
    # ถ้าหากไม่ใส่ข้อมูลใน city ก็จะมีค่าเริ่มต้นเป็น Bangkok
    
    print("Name :",fname)
    print("Lastname :",lname)
    print("City :",city)


Showdata(fname="Pachara",lname="Sangarun")
Showdata(fname="Pachara",lname="Sangarun",city="Samutsakorn")