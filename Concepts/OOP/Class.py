# Class
# In Python

name = "marine"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
print("hp {0}, damage {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드/ 시즈 모드.
tank_name = "tank"
tank_hp = 150
tank_damage = 35

print("{0} tank_name 유닛이 생성되었습니다".format(tank_name))
print("tank_hp {0}, tank_damge {1}\n".format(tank_hp, tank_damage))

tank2_name = "tank"
tank2_hp = 150
tank2_damage = 35

print("{0} tank2_name 유닛이 생성되었습니다".format(tank2_name))
print("tank2_hp {0}, tank2_damge {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)
