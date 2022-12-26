import random
inputs=['A', 'B', 'C']
class Bus:
   sitting=0
   standing=0
   def seat_allot(self):
        if self.sitting<25:
           self.sitting+=1
           print('sitting space is alotted in bus')
        elif self.standing<15:
            self.standing+=1
            print('standing space is allotted in bus')
        else: print('sorry,no space available in bus')
class Car_1:
      seats=0
      ID='101'
      def seat_allot(self):
          if self.seats<5:
              self.seats+=1
              print(f'you are alloted seat in car of ID: {self.ID}')
          else: print(f'sorry,no seats are available in car of ID: {self.ID}')
class Car_2(Car_1):
      ID='102'
Bus=Bus()
Car_1=Car_1()
Car_2=Car_2()
while 1:
 user=input('please enter what you want?')
 if user=='B':
    Bus.seat_allot()
 elif user=='A':
     if Car_1.seats<5:
        Car_1.seat_allot()
     elif Car_2.seats<5:
        Car_2.seat_allot()
     else:print('sorry no seats available in both the cars')
 elif user=='C':
     num=random.random()
     if num<=0.6:
        if Bus.standing>0:
           Bus.standing-=1
           print('a passenger is removed from Bus')
        elif Bus.sitting>0:
             Bus.sitting-=1
             print('a passenger is removed from Bus')
        else:print('sorry no passenger can be removed ')
     if num>0.6 and num<=0.8:
         if Car_1.seats>0:
             Car_1.seats-=1
             print('a passenger is removed from car of ID 101')
         else:print('sorry no passenger can be removed')
     if num>0.8:
         if Car_2.seats>0:
             Car_2.seats-=1
             print('a passenger is removed from car of ID 102')
         else:print('sorry no passenger can be removed')
 else:quit()
