# ฟังก์ชั่น เรียก ฟังก์ชั่น

def equal(x,y,z):
    # ฟังก์ชั่น เรียก ฟังก์ชั่น
    a=compareMax(x,y) # เทียบตัวเลขรอบแรก
    m=compareMax(a,z) # เทียบตัวเลขรอบสอง
    return m


def compareMax(x,y):
    if x>y:
        return x
    else:
        return y




max=equal(10,20,30)
print("ค่ามากสุด : ",max)