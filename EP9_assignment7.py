# จับคู่คำทักทาย / บุลคล

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
for x in greeting:
    for y in people:
        result.append(x+y)
print(result)