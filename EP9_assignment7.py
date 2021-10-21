# จับคู่คำทักทาย / บุลคล จับคู่ข้อมูล

'''
แบ่งกลุ่มคำทักทาย ** hi,hello
กับกลุ่มของบุคคล ** โทนี่,โทนวย

ต้องการ 

hi โทนี่ , hi โทนวย
'''

greeting=["Hi","Hello","Good bye"]
people=["โทนี่","โทนวย","โทนาฟ"]
result=[]

# แบบปกติ
for x in greeting: # หยิบข้อมูลใน greeting วนไป
    for y in people: # หยิบข้อมูลใน people วนไป
        result.append(x+y) # ใช้คำสั่ง .append ยัดข้อมูลลงไปใน ตัวแปร result
print(result)

# แบบย่อ 
result=[x+y for x in greeting for y in people] # ควรทำความเข้าใจก่อน
print(result)