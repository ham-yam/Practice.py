# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
#     return balance + money
#
# def withdraw(balance, money): #출금
#     if balance >= money: #잔액이 출그보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance
# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission
#
# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))



#기본값 설정
# def profile(name, age, main_lang):
#     print("이름: {0}|t나이 : {1}|t주 사용언어: {2}"|
#         .format(name, age, main_lang))
# profile("유", 20, "파이썬")
# profile("김", 25, "자바")
#
# def profile(name, age=17, main_lang= "파이썬"):
#      print("이름: {0}\t 나이 : {1}\t 주 사용언어: {2}" \
#         .format(name, age, main_lang))
# profile("유")
# profile("김")

#키워드값 입력된 값의 순서가 달라도 정해진 순서에 따라 정렬
# def profile (name, age, main_lang):
#     print(name, age, main_lang)
#
# profile(name = "유", main_lang = "python", age = 20)
# profile(age = 22, name = "김", main_lang = "JAVA")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

#가변인자 함수를 이용한 입력값 추가 혹은 제거
# def profile(name, age, *language):
#      print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
#      for lang in language:
#          print(lang,end=" ")
# print()
#
# profile("유", 20, "Python", "Java", "C++", "C", "C#","JavaScript")
# profile("김", 25, "kotlin", "swoft")

#w지역변수, 전역변수(모든 공간에서 부를 수 있는 변수)
# gun = 10
#
# def checkpoint(soldiers): #경계근무
#     global gun #전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
#
# print("전체 총 : {0}". format(gun))
# #checkpoint(2) #2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총: {0}".format(gun))


#Q_ finding avg. weight

# 표준 체중: 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남: 키(m) x 키(m) x 22
# 여: 키(m) x 키(m) x 21
#
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.
#
# def std_weight(height, gender): # 키 = m단위(실수), gender = "남자/여자"
#     if gender == '남자':
#         return height * height * 22
#     else:
#         return height * height * 21
#
# height = 175 #cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))