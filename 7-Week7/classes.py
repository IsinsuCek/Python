from dataclasses import dataclass

"""class Person:
    boy = 170
    kilo = 60
    meslek = 'developer'
    def set_meslek(self, new_skill):
        pass
"""
"""Person().meslek = 'barista'

sist = Person()
sist.boy = 180
print(sist.boy)
print(sist.kilo)

print('class changed')
brot = Person()
print(brot.boy)
print(brot.kilo)
brot.set_meslek('scientist')
print(brot.meslek)
"""
"""
class Person:
    def __init__(self, boy, kilo, meslek):
        self.boy = boy
        self.kilo = kilo
        self.meslek = meslek
        self.skill_list = []
        #print('initiliazed the person class')
    
    def set_skill(self, new_skill):
        self.skill_list.append(new_skill)
    
    def meslek_degistir(self, yeni_meslek):
        self.meslek = yeni_meslek

class Dev:
    def  do_something(self, obj):
        print('a function called with {}'.format(obj))

A = Person(120, 50, 'science')
#A.set_skill('science')
print(A.meslek)
print(A.kilo)
A.set_skill('asd')

B = Person(140, 70, 'dev')
print(B.meslek)
print(B.kilo)"""

class FILO:
    def __init__(self, l =[]):
        self.l = l

    def add_element(self, element):
        self.l.append(element)

    def remove_element(self):
        return self.l.pop(-1)

fl = FILO()
fl.add_element(2)
fl.add_element(5)
fl.add_element(6)
fl.add_element(1)

print(fl.remove_element())

class HeapClass:
    def __init__(self, l = []):
        self.l = l.sort() 

    def pop_highest(self):
        return self.l.pop(-1)
    
    def push(self, element):
        self.l.append(element)
        self.l.sort()