import time
from xml.etree.ElementTree import tostring
import requests

# functon นับเวลาถอยหลัง
def countdownTime() :
    t = int(input("คุณต้องการซักกี่นาที : "))*60
    while t:
        min = t//60
        sec = t%60
        timer = '{:02d}:{:02d}'.format(min,sec)
        print("เริ่มซักผ้า กรุณารอสักครู่..."+timer,end='\r')
        time.sleep(1)
        t -= 1
        
        if min == 0 and sec == 59:
            #  Tokent Line ที่ต้องการรับการแจ้งเตือน
            token = 'u5UzcaxUFsmfqvcsEczqNTkEEXQm4Y1In87QWJeUt1b'
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {token}'
            }
            url = 'https://notify-api.line.me/api/notify'
            message =  'เหลือเวลาอีก 1 นาที'
            requests.post(url=url, headers=headers, data={'message': message})

# ส่วนการทำงาน
while True :
    array = []
    print("\nเมนู")
    print("1.เลือกเครื่องซักผ้า")
    print("2.ออกจากโปรแกรม")
    select = int(input("กรุณาเลือกเมนู :"))

    while select != 1 and select != 2 :
            print("\nคุณเลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่\n")
            print("1.เลือกเครื่องซักผ้า")
            print("2.ออกจากโปรแกรม")
            select = int(input("กรุณาเลือกเมนู :")) 
            
    if select == 1 :
        print("\nตำแหน่งของเครื่องซักผ้า\n")
        for sa in range(1):
            for a in range(1,4):
                print("[ A%d ]"%(a),end=' ')
            print('')
            for b in range(1,4):
                print("[ B%d ]"%(b),end=' ')
            print('')
            for c in range(1,4):
                print("[ C%d ]"%(c),end=' ')
            print('')
            
        print("\nสถานะ : ว่างทุกเครื่อง\n")
        row = str(input("กรุณาเลือกแถวของเครื่องซักผ้า :"))
        col = int(input("กรุณาเลือกหมายเลขของเครื่องซักผ้า :"))
        print('\n')

        while (row != 'A' and row != 'a' and row != 'B' and row != 'b' and row != 'C' and row != 'c') or (col != 1 and col != 2 and col != 3) :
            row = str(input("ข้อมูลไม่ถูกต้อง!! กรุณาเลือกแถวของเครื่องซักผ้าอีกครั้ง :"))
            col = int(input("ข้อมูลไม่ถูกต้อง!! กรุณาเลือกหมายเลขของเครื่องซักผ้า :"))
            print('\n')

    # ถ้าลูกค้าเลือกแถว A
        if row == 'A' or row == 'a':
            for a in range(1,4) :
                if a == col :
                    print("[ XX ]",end=' ')
                    array.append("A%d"%(a))
                else :
                    print("[ A%d ]"%(a),end=' ')
            print('')
            for b in range(1,4) :
                print("[ B%d ]"%(b),end=' ')
            print('')
            for c in range(1,4) :
                print("[ C%d ]"%(c),end=' ')
            print('')
            
            array = array[0]
            print("\nสถานะ : เครื่อง " + array + " ไม่ว่าง\n")
            print("\nคุณเลือกเครื่องซักผ้า "+ array +" ราคา 40 บาท")
            coin = int(input("กรุณาหยอดเหรียญ 10 ทั้งหมด 4 เหรียญ : "))
            if coin == 10 :
                for i in range(3):
                    if coin == 10 :
                        coin = int(input("กรุณาหยอดเหรียญ 10 อีก %d เหรียญ : "%(3-i)))
                countdownTime()

            else : 
                while coin != 10:
                    coin = int(input("กรุณาหยอดเหรียญ 10 : "))
                    if coin == 10 :
                        for i in range(3):
                            coin = int(input("กรุณาหยอดเหรียญ 10 อีก %d เหรียญ : "%(3-i)))
                        countdownTime()               

    # ถ้าลูกค้าเลือกแถว B         
        elif row == 'B' or row == 'b':
            for a in range(1,4):
                print("[ B%d ]"%(a),end=' ')
            print('')
            for b in range(1,4):
                if b == col :
                    print("[ XX ]",end=' ')
                    array.append("B%d"%(b))
                else :
                    print("[ A%d ]"%(b),end=' ')
            print('')
            for c in range(1,4):
                print("[ C%d ]"%(c),end=' ')
            print('')
            
            array = array[0]
            print("\nสถานะ : เครื่อง " + array + " ไม่ว่าง\n")
            print("\nคุณเลือกเครื่องซักผ้า "+ array +" ราคา 40 บาท")
            coin = int(input("กรุณาหยอดเหรียญ 10 ทั้งหมด 4 เหรียญ : "))
            if coin == 10 :
                for i in range(3):
                    coin = int(input("กรุณาหยอดเหรียญ 10 อีก %d เหรียญ : "%(3-i)))
                countdownTime()
                
            else : 
                while coin != 10:
                    coin = int(input("กรุณาหยอดเหรียญ 10 : "))
                    if coin == 10 :
                        for i in range(3):
                            coin = int(input("กรุณาหยอดเหรียญ 10 อีก %d เหรียญ : "%(3-i)))
                        countdownTime()
            
    # ถ้าลูกค้าเลือกแถว C   
        elif row == 'C' or row == 'c':
            for a in range(1,4):
                print("[ B%d ]"%(a),end=' ')
            print('')
            for b in range(1,4):
                print("[ C%d ]"%(b),end=' ')
            print('')
            for c in range(1,4):
                if c == col :
                    print("[ XX ]",end=' ')
                    array.append("C%d"%(c))
                else :
                    print("[ A%d ]"%(c),end=' ')
            print('')

            array = array[0]
            print("\nสถานะ : เครื่อง " + array + " ไม่ว่าง\n")
            print("\nคุณเลือกเครื่องซักผ้า "+ array +" ราคา 40 บาท")
            coin = int(input("กรุณาหยอดเหรียญ 10 ทั้งหมด 4 เหรียญ : "))
            if coin == 10 :
                for i in range(3):
                    coin = int(input("กรุณาหยอดเหรียญ 10 อีก %d เหรียญ : "%(3-i)))
                countdownTime()
                
            else : 
                while coin != 10:
                    coin = int(input("กรุณาหยอดเหรียญ 10 : "))
                    if coin == 10 :
                        for i in range(3):
                            coin = int(input("กรุณาหยอดเหรียญ 10 อีก %d เหรียญ : "%(3-i)))
                        countdownTime()
                        
    elif select == 2 :
        print("ขอบคุณที่ใช้บริการ")
        exit()
