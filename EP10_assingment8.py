# จับคู่สินค้าและราคา  การใช้ Zip

fruit=["มะม่วง","มะยม","มะนาว","มะเฟือง"]
price=[50,30,15,10]

# ใช้ฟังชั่น zip คือการดึงข้อมูลตามจำนวนรอบจนครบจำนวนข้อมูล 
'''
มะม่วง 50 
มะยม 30 
มะนาว 15 
'''
# แตกต่างจาก assignment7

for x,y in zip(fruit,price): 
    print("สินค้า = ",x,"ราคา = ",y)
