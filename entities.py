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
    # ord(), char() used to get integer from unicode and vice versa
    LaoYin = 0      # 9675 ○
    ShaoYin = 1     # 9679 ●●
    ShaoYang = 2    # 9679 ●
    LaoYang = 3     # 9747 ☓

    def dong(self):
        if not self.is_dong_able():
            return self
        else:
            return Yao.ShaoYang if self is Yao.LaoYin else Yao.ShaoYin
            
    def is_dong_able(self):
        return self is Yao.LaoYang or self is Yao.LaoYin
    
    def val(self):
        return int(self._value_ >= 2)
    

class BaGua(Enum):
    Qian = 8, '乾'
    Dui = 7, '兑'
    Li = 6, '离'
    Zhen = 5, '震'
    Xun = 4, '巽'
    Kan = 3, '坎'
    Gen = 2, '艮'
    Kun = 1, '坤'
    
    def __init__(self, val, dname):
        self._value_= val
        self.display_name = dname
    
    def display(self):
        # value and Yao mapping relation is top down
        bit_arr = reversed('{0:03b}'.format(self._value_-1))
        yang_str = '-'*8
        yin_str = '-'*3+' '*2+'-'*3
        desc = "\n".join(yang_str if int(v)==1 else yin_str for v in bit_arr)
        return desc

    @classmethod
    def Init(cls, gua):
        val = 0
        for bit in reversed(gua):
            val = (val << 1) | bit
        for m in cls:
            if m._value_ == val+1:
                return m
        return None

# the symbol stores the integer mapping to Unicode 4 Yijing Symbols
# the sequence of the symbols is based on the Manifested Hexagrams 
# Ref https://www.unicode.org/charts/PDF/U4DC0.pdf
class Hexagrams(Enum):
    Kun1 = 1, 19905, '坤为地', '坤'
    Bo = 2, 19926, '山地剥', '剥'
    Bi3 = 3, 19911, '水地比', '比'
    Guan = 4, 19923, '风地观', '观'
    Yu = 5, 19919, '雷地豫', '豫'
    Jin = 6, 19938, '火地晋', '晋'
    Cui = 7, 19948, '泽地萃', '萃'
    Pi = 8, 19915, '天地否', '否'
    Qian1 = 9, 19918, '地山谦', '谦'
    Gen = 10, 19955, '艮为山', '艮'
    Jian3 = 11, 19942, '水山蹇', '蹇'
    Jian4 = 12, 19956, '风山渐', '渐'
    XiaoGuo = 13, 19965, '雷山小过', '小过'
    Lu = 14, 19959, '火山旅', '旅'
    Xian = 15, 19934, '泽山咸', '咸'
    Dun = 16, 19936, '天山遁', '遁'
    Shi = 17, 19910, '地水师', '师'
    Meng = 18, 19907, '山水蒙', '蒙'
    Kan = 19, 19932, '坎为水', '坎'
    Huan = 20, 19962, '风水涣', '涣'
    Xie = 21, 19943, '雷水解', '解'
    WeiJi = 22, 19967, '火水未济', '未济'
    Kun4 = 23, 19950, '泽水困', '困'
    Song = 24, 19909, '天水讼', '讼'
    Sheng = 25, 19949, '地风升', '升'
    Gu = 26, 19921, '山风蛊', '蛊'
    Jing = 27, 19951, '水风井', '井'
    Xun = 28, 19960, '巽为风', '巽'
    Heng = 29, 19935, '雷风恒', '恒'
    Ding = 30, 19953, '火风鼎', '鼎'
    DaGuo = 31, 19931, '泽风大过', '大过'
    Gou = 32, 19947, '天风媾', '媾'
    Fu = 33, 19927, '地雷复', '复'
    Yi2 = 34, 19930, '山雷颐', '颐'
    Zhun = 35, 19906, '水雷屯', '屯'
    Yi4 = 36, 19945, '风雷益', '益'
    Zhen = 37, 19954, '震为雷', '震'
    ShiHe = 38, 19924, '火雷噬嗑', '噬嗑'
    Sui = 39, 19920, '泽雷随', '随'
    WuWang = 40, 19928, '天雷无妄', '无妄'
    MingYi = 41, 19939, '地火明夷', '明夷'
    Bi4 = 42, 19925, '山火贲', '贲'
    JiJi = 43, 19966, '水火既济', '既济'
    JiaRen = 44, 19940, '风火家人', '家人'
    Feng = 45, 19958, '雷火丰', '丰'
    Li = 46, 19933, '离为火', '离'
    Ge = 47, 19952, '泽火革', '革'
    TongRen = 48, 19916, '天火同人', '同人'
    Lin = 49, 19922, '地泽临', '临'
    Sun = 50, 19944, '山泽损', '损'
    Jie = 51, 19963, '水泽节', '节'
    ZhongFu = 52, 19964, '风泽中孚', '中孚'
    GuiMei = 53, 19957, '雷泽归妹', '归妹'
    Kui = 54, 19941, '火泽睽', '睽'
    Dui = 55, 19961, '兑为泽', '兑'
    Lv = 56, 19913, '天泽履', '履'
    Tai = 57, 19914, '地天泰', '泰'
    DaXu = 58, 19929, '山天大畜', '大畜'
    Xu = 59, 19908, '水天需', '需'
    XiaoXu = 60, 19912, '风天小畜', '小畜'
    DaZhuang = 61, 19937, '雷天大壮', '大壮'
    DaYou = 62, 19917, '火天大有', '大有'
    Guai = 63, 19946, '泽天夬', '夬'
    Qian2 = 64, 19904, '乾为天', '乾'

    def __init__(self, val, ucode, fname, sname):
        self._value_= val
        self.unicode = ucode
        self.full_name = fname
        self.short_name = sname
    
    def display(self):
        desc = '{fname}：{symbol}'.format(
            fname = self.full_name, symbol = chr(self.unicode))
        return desc

    @classmethod
    def Init(cls, gua):
        val = 0
        for bit in reversed(gua):
            val = (val << 1) | bit
        for m in cls:
            if m._value_ == val+1:
                return m
        return None

class ZhuangGua:
    _gua = []
    _bian_gua = []
    _bian = False
    def __init__(self, matrix):
        if matrix is not None:
            if len(matrix)== 6:
                for row in matrix:
                    if len(row) == 3:
                        yao = Yao(row.count(1))
                        if yao.is_dong_able():
                            self._bian = True
                        # using the reversed order to pai gua
                        self._gua.insert(0, yao.val())
                        self._bian_gua.insert(0, yao.dong().val())
                    else:
                        raise TypeError()
            else:
                raise TypeError()
        else:
            raise TypeError()

    def _pai(self, gua):
        print(gua)
        wai_gua = BaGua.Init(gua[0:3])
        nei_gua = BaGua.Init(gua[3:6])
        hexagram = Hexagrams.Init(gua)
        print(hexagram.display())
        print(wai_gua.display())
        print(nei_gua.display())
    
    def pai_gua(self):
        self._pai(self._gua)
        if self._bian:
            self._pai(self._bian_gua)


matrix1 = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
matrix = [[1,1,0],[1,1,1],[1,1,1],[1,1,1],[0,0,1],[0,0,1]]
zg = ZhuangGua(matrix)
zg.pai_gua()

print(Element.Wood.ke_wo().name)
print(Element.Wood.wo_ke().name)
print(Element.Wood.sheng_wo().name)
print(Element.Wood.wo_sheng().name)

print(Yao.ShaoYin)
print(Yao.ShaoYin.val())

print(Yao.ShaoYin.dong())
print(Yao.LaoYin.dong().name)
print(Yao.LaoYin.dong().val())


