class Person:
    def __init__(self, param_name):
        print('i am created!', self) # self는 내부 함수 생성시 인자에 자기 자신을 넘겨주게 됨.
        self.name = param_name

    def talk(self):
        print('안녕하세요, 제 이름은', self.name, '입니다.')


person_1 = Person('유재석') # i am created! <__main__.Person object at 0x000002056B10F5B0>
print(person_1.name) # 유재석
print(person_1) # <__main__.Person object at 0x000002056B10F5B0>
person_1.talk() # 안녕하세요, 제 이름은 유재석 입니다.
person_2 = Person('박명수') # i am created! <__main__.Person object at 0x000002056B170850>
print(person_2.name) # 박명수
print(person_2) # <__main__.Person object at 0x000002056B170850>
person_2.talk() # 안녕하세요, 제 이름은 박명수 입니다.
