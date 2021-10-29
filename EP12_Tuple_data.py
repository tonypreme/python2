# ชนิดข้อมูล Tuple ทูเปิล & ทับเปิล

'''
คุณสมบัติ
คล้ายๆ list สามารถเก็บข้อมูลได้หลาย ชนิด 

สิ่งที่แตกต่างจาก list 
list ข้อมูลสมาชิก สามารถเปลี่ยนแปลงได้
tuple ข้อมูลสมาชิก ไม่สามารถเปลี่ยนแปลงได้ 

Ex. ข้อมูลที่ไม่สามารถเปลี่ยนแปลงได้ ข้อมูลแบบ tuple 
 ID รหัสบัตร ปชช ข้อมูลค่าคงที่ <= ไม่สามารถแก้ไขได้ 

'''
# การนิยาม tuple แบบทั่วไป
tup=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple
lis=[1,2,3,4,"พชร","มะม่วง",True,3.99] # list 

lis[0]="กทม" # การเปลี่ยนแปลงข้อมูลในตัวแปร list เข้าถึงข้อมูลผ่าน index[]
# ข้อมูลสมาชิกของ list สามารถเปลี่ยนแปลงได้

# ส่วนของ tuple  ไม่สามารถแก้ไขได้เลย

print(type(tup))
print(type(lis))

# การนิยาม constructer ด้วยการ ชื่อ=ตัวแปร((ชนิดข้อมูล))
tup2=tuple((1,2,3,4,"พชร","มะม่วง",True,3.99)) # tuple
lis2=list([1,2,3,4,"พชร","มะม่วง",True,3.99]) # list 

print(type(tup2))
print(type(lis2))

# -------------------------------------
# การเข้าถึงข้อมูล
tup3=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple

print("หัวข้อที่ 2 ",tup[0:1]) # หากต้องการระบุตำแหน่งต้อง index[] 
# 0 -> ...
# ... <- -1

# -------------------------------------
# การเข้าถึงข้อมูลแบบกำหนดช่วง (slice)

tup4=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple
print("หัวข้อที่ 3 ",tup4[1:4])

# -------------------------------------
# การแก้ไขข้อมูลในตัวแปร tuple ** ทำงานคู่กับ list
tup5=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple
print("หัวข้อที่ 4 ","ก่อนแก้ไข = ",tup5)

# ถ้าอยากแก้ไขให้แปลงข้อมูลเป็น list
lis3=list(tup5) # แปลง tiple เป็น list 
lis3[0]="กรุงเทพ"
tup5=tuple(lis3) # แปลงกลับมาเป็น tuple

print("หัวข้อที่ 4 ","หลังแก้ไขข้อมูลแล้ว = ",tup5)

# -------------------------------------
# แสดงผลด้วย loop
tup6=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple

for item in tup6:
    print("หัวข้อที่ 5 ","สมาชิก = ",item)

# -------------------------------------
# การตรวจสอบข้อมูล เช็คข้อมูลสมาชิกภานในข้อมูล
tup7=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple

if "พชร" in tup7:
    print("หัวข้อที่ 6 ","เป็นสมาชิก")
else :
    print("หัวข้อที่ 6 ","ไม่เป็นสมาชิก")
# ใช้ if else ในการตรวจสอบ

# -------------------------------------
#  นับจำนวนสมาชิก (len)
tup8=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple

# index 0-7 วิธีการนับ
# len 1-8 วิธีนับ

print("หัวข้อที่ 7 ",len(tup8))

# -------------------------------------
# len() ทำงานร่วมกับ loop for 
tup9=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple

for item in range(len(tup9)): # (0-8) เพราะมี index จาก range
    print("หัวข้อที่ 8 ",tup9[item]) # tup[0],....tup[7]

# -------------------------------------
# การสร้างและเพิ่มข้อมูล (join)

tup10=()
print("หัวข้อที่ 9 ",type(tup10))
x=("tuple ตัวเดียว" ,) # ถ้าหากข้อมูลมีตัวเดียว ชนิดข้อมูลจะยังไม่ใช่ tuple ต้องใส่ , ด้วย
print(x)

# การเพิ่มข้อมูลนั้น ต้องเป็นการเอา ชนิดข้อมูล tuple มาต่อกัน
name=("tony","maew")
new=("jaja",)

name=name+new # ต้องแปลงข้อมูลเป็น ชนิด tuple เหมือนกันก่อน
print("หัวข้อที่ 9 ",name)
'''
กรณี name=("tony","maew") <= tuple
    new="jaja" <= str

    ทำแบบนี้เลยก็ได้
 name=name+(new,) <= มาแปลงข้อมูลตรงนี้ก็ได้ ** 
 
 หรือ name=name+tuple(new) 
 ## แต่ถ้าทำแบบนี้จะแยกสมาชิกออกเป็นแต่ละตัวอักษรเลย ##

print(nname)
'''
# -------------------------------------
# การทำงานร่วมกัย list 
tup11=(1,2,3,4,"พชร","มะม่วง",True,3.99) # tuple

lis11=list(tup11) # พอเปลี่ยนชนิดได้แล้ว 
print("หัวข้อที่ 10 ",type(lis))

# list สามารถเข้าถึง index ได้
lis11[1]="กรุงเทพ" # พอทำการแก้ไขข้อมูล

tup11=tuple(lis11) # ทำการแปลงข้อมูล list กลับเป็น tuple ต่อ

# อีก 1 ตัวอย่างกรณี ต้องการนำข้อมูล list มาเพิ่มใน tuple 

city=["กรุงเทพ","สมุทรสาคร","ปทุม"]
name11=("tony","tinuy")

newtup=name11+tuple(city)
print("หัวข้อที่ 10 ",newtup)

# -------------------------------------
# การลบข้อมูล del , การลบข้อมูลแบบ list
