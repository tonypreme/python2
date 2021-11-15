# Set 
'''
มีสมาชิก มากกว่า 1 
มีชนิดข้อมูลได้หลายแบบ

แต่ข้อมูลไม่สามารถซ้ำกันได้  
join set  
'''

'''
จัดกลุ่มข้อมูลพื้นฐาน
List =[] , ข้อมูลต่างชนิดกันได้ , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Tuple =() , ข้อมูลต่างชนิดกันได้ , แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Set ={} , ข้อมูลต่างชนิดกันได้ , แก้ไขข้อมูลสมาชิกไม่ได้ (ไม่มี index ให้อ้างอิงในการแก้ไข) , ข้อมูลซ้ำกันไม่ได้ , ลำดับไม่แน่นอน
'''
# *** set จะมีค้นหาข้อมูล ได้เร็วที่สุด *** 
#-----------------------------------------

# สร้าง Set ไม่มี index  

# แบบปกติ
fruit={"มะม่วง","มะขาม","มะยม",50,True}
print(fruit) # การเรียงลำดับไม่แน่นอน  

# constructor
fish=set(["ปลาดุก","ปลาหมอ"])
print(fish)
# *** set ข้อมูลไม่สามารถซ้ำกันได้ ไม่สามารถแก้ไขได้ แต่เพิ่มข้อมูลได้ไม่จำกัด ***

# กรณีเรามีข้อมูลเป็น list และมีสมาชิกใน list เป็นจำนวนหลายร้อยตัว
# เราจะทำการคัดแยกตัวซ้ำใน list ได้โดยการแปลง list เป็น set 

#-----------------------------------------
# เพิ่มข้อมูลสมาชิกใน Set
fruit2={"มะม่วง","มะขาม","มะยม",50,True}

fruit2.add("ทุเรียน") # สามารถเพิ่มสมาชิกได้เรื่อยๆ แต่ลบไม่ได้ 
print(fruit2)

# หากต้องการเพิ่มทีละหลายๆสมาชิก 
lis2=["มะนาว","ส้มตำ","มะละกอ"]

fruit2.update(lis2) # ใช้ update 