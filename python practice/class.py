#9.1 class
# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40 #유닛의 체력
# damage = 5 #유닛의 공격력
#
#
# print("{}유닛이 생성되었습니다".format(name))
# print("체력{0}, 공격력 {1}|n".format(hp, damage))
#
# #탱크 : 공격 유닛, 탱크. 포를 쏠 수 있다. 일반/ 시즈 모드
#
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{}유닛이 생성되었습니다".format(tank_name))
# print("체력{0}, 공격력 {1}＼n".format(tank_hp, tank_damage))
#
# def attack(name, location, damage):
#     print("{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}]".format ( |
#           name, location, damage))
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
#
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
#
# print("{}유닛이 생성되었습니다".format(tank2_name))
# print("체력{0}, 공격력 {1}＼n".format(tank2_hp, tank2_damage))
#
# def attack(name, location, damage):
#     print("{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}]".format ( ＼
#           name, location, damage))
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
#
# #일일이 1~n 까지 입력이 힘듦
#     #class = 붕어빵 틀같이 비유, 서로 연관이 있는 함수와 변수의 집합
#하나의 class를 통해 여러 변수를 생성해 낼 수 있었다

#일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))



''' class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)'''


# 9.2 __init__
''' 마린, 탱크와 같이 class에서 만들어지는 변수들을 객체라 부름
unit class의 instance라고도 불림
Unit(self, name, hp, damage):
# --> Unit에서 self를 제외한 정보들을 똑같이 입력해야 객체를 만들 수 있음
marine3 = Unit("마린", 40) #첫번째 줄에서 필요한 정보가 누락됨'''
'''
#9.3 멤버변수 (class내에서 정의된 변수, 실제 응용 가능)

#레이스: 공중유닛, 비행, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}". format(wraith1.name, wraith1.damage))

#마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith1.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))
#class 외부에서 원하는 변수에 대한 확장, 확장을 한 개체에서만 적용, 다른 객체에는 적용X
'''
#9.4 메소드
'''class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, location):
        print("{0}:{1} 방향으로 적군을 공격 합니다.[공격력{2}]"
        .format(self.name, location, self.damage))  #자기자신에 정의된 값, loc = 전달받은 값사용
    def damaged(self, damage):
        print("{0}:{1}데미지를 입엇습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
#파이어뱃: 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25) '''

#9.5 상속

#일반 유닛
# unit, attackunitㅇ에 겹치는것 ==> 상속받아서 사용하는 것
'''class Unit:
    def __init__(self, name, hp):
        Unit.__init__(self, name, hp)
        self.name = name
        self.hp = hp

#공격 유닛
class AttackUnit(Unit): #()안에 상속받고싶은 class를 입력
    def __init__(self, name, hp, damage):
        self.damage = damage'''

#9.6 다중상속










'''    

#드랍쉽 : 공중유신, 수송기. 마린/ 파이어뱃/ 탱크등을 수송. 공격X
#날 수 있는 기능을 가진 클래스
class Flyable:
def __init__(self, flying_speed):
self.flying_speed = flying_speed

def fly(self, name, location):
print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
.format(name,location, self.flying_speed))
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): #다중상속 적용
def __init__(self, name, hp, damage, flying_speed):
AttackUnit.__init__(self, name, hp, damage)
Flyable.__init__(self, flying_speed)
#발키리 : 공중 공격유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

'''





