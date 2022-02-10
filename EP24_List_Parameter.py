# List Parameter

def displayFruit(item): 
    for i in range(len(item)):
        print( "ผลไม้ชิ้นที่ " , i + 1 , " = " , item[i] )


fruit=["มะม่วง","มะละกอ"] # ชนิดข้อมูลเป็น list
vet=("ชะอม","ผักกาด","คะน้า") # ชนิดข้อมูลแบบ tuple

# displayFruit(fruit)
displayFruit(vet)