class Submarine:
    '''
    ------------------
    Test Documentation
    นี่คือโปรแกรมเรือดำน้ำ
    ------------------
    '''

    def __init__(self, price,budget): # ฟังชันมีค่าเริ่มต้น
        self.captain = "Prawit"
        self.sub_name = "Uncle I"
        self.price =  price #million
        self.kilo = 0
        self.budget = budget #ต้นทุนที่ใช้ไปกับเรือดำน้ำ
        self.totalcost = 0

    def Misslie(self):
        print("We ae Department of Missile")

    def Calcommision(self):
        '''
            ------------------
            ฟังชั่นคำนวนค่าคอมมิชชั่นกี่บาทในการขายเรือ
            ------------------
            '''
        pc = 10 # 10%
        percent = self.price * (10/100)
        print("Loong! You got: {} Million Baht".format(percent))

    def Goto(self,enemypoint,distance):#คำนวนระยะทางที่ไป enemypoint(จุดศัตรู) distance(จำนวนกี่โลที่ไป)
        print(f"Let's go to {enemypoint} Distance: {distance} KM ") # f คือตัวย่อ เอาตัวแปรที่ฟังชั่นมาใส่ใน {} ได้เลย
        self.kilo = self.kilo + distance
        self.Fuel() # คำนวน class ElectricSubmarine(Submarine)

    def Fuel(self): # ฟังชันคำนวนกินน้ำมัน เชื้อเพลิง
        deisel = 20 # 20 baht/litre
        cal_fuel_cost = self.kilo * deisel # self.kilo=7,000
        print("Current Fuel Cost: {:,d} Baht".format(cal_fuel_cost))
        self.totalcost += cal_fuel_cost

    @property # ฟิกค่าไว้ ถ้ามี @property ต้องมี return
    def BudgeRemaining(self):
        remining = self.budget - self.totalcost
        print("Budget Remaining: {:,.2f} Baht".format(remining))
        return remining # ส่งค่ากลับ

class ElectricSubmarine(Submarine):

    def __init__(self,price=10000,budget=400000):
        self.sub_name = 'Uncle III'
        self.battery_distance = 100000
        # Submarine can go out 100000 km/100 percent
        super().__init__(price,budget)

    def Battery(self):
        allbatter = 100
        print("เดินทาง: {} กิโล".format(self.kilo))
        calculate = (self.kilo / self.battery_distance) * 100
        print("calculate(คำนวน)",calculate)
        print("We have Battery Remaining: {}%".format(allbatter-calculate))

    def Fuel(self):  # ฟังชันคำนวนกินน้ำมัน เชื้อเพลิง
        kilowatcost = 20  # 20 baht/litre
        cal_fuel_cost = self.kilo * kilowatcost  # self.kilo=7,000
        print("Current Power Cost: {:,d} Baht".format(cal_fuel_cost))
        self.totalcost += cal_fuel_cost

if __name__ == '__main__':
# if __name__ == '__main__': คือให้โปรแกรมรันส่วนนี้เท่านั้น

    tesla = ElectricSubmarine(40000,2000000)
    print(tesla.captain)
    print(tesla.budget)
    tesla.Goto("Japan",10000)
    print(tesla.BudgeRemaining)
    tesla.Battery()

    print("\n----------------")

    kongtabbok = Submarine(40000,2000000)
    print(kongtabbok.captain)
    print(kongtabbok.budget)
    kongtabbok.Goto("Japan",10000)
    print(kongtabbok.BudgeRemaining)


'''
kongtabreuw = Submarine(654723) #กองทัพเรือ
print("Captain:",kongtabreuw.captain)
print("Submarine_name:",kongtabreuw.sub_name)
print("\n----------------")
print("kongtabreuw:",kongtabreuw.kilo)
kongtabreuw.Goto("China", 7000)
print("kongtabreuw go China:",kongtabreuw.kilo)
kongtabreuw.Fuel()
current_budget = kongtabreuw.BudgeRemaining #หนวยเงิน
print("Current Budget: ",current_budget )

kongtabreuw.Calcommision()
################################3
print("\n-------Sub no2---------")
kongtabbok = Submarine(70000)
print("Before...")
print(kongtabbok.captain)
print("Afer...")
kongtabbok.captain = "Srivare" # เปลี่ยนตัวค่าอยู่ในคลาสได้
print(kongtabbok.captain)
'''