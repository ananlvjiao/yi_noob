from enum import Enum, unique

@unique
class Element(Enum):
    Wood = 0
    Fire = 1
    Earth = 2
    Metal = 3
    Water = 4

    # which elem overcome me
    def ke_wo(self):
        return Element((self.value-2)%5)
    # which elem generate me
    def sheng_wo(self):
        return Element((self.value-1)%5)

    # which elem I overcome
    def wo_ke(self):
        return Element((self.value+2)%5)
    # which elem I generate
    def wo_sheng(self):
        return Element((self.value+1)%5)

class Yao(Enum):
    ShaoYang = 1
    ShaoYin = 0
    LaoYang = 3
    LaoYin = 2

    def dong(self):
        if not self.is_dong_able():
            return self
        else:
            return Yao.ShaoYang if self is Yao.LaoYin else Yao.ShaoYin
            
    def is_dong_able(self):
        return self is Yao.LaoYang or self is Yao.LaoYin
    
    def val(self):
        return self.value%2


print(Element.Wood.ke_wo().name)
print(Element.Wood.wo_ke().name)
print(Element.Wood.sheng_wo().name)
print(Element.Wood.wo_sheng().name)

print(Yao.ShaoYin)
print(Yao.ShaoYin.val())

print(Yao.ShaoYin.dong())
print(Yao.LaoYin.dong().name)
print(Yao.LaoYin.dong().val())

