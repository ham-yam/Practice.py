# weather = input('오늘 날씨는 어때요?')
# if weather == '비'or weather =='눈':
#     print('우산을 챙겨라')
# elif weather == '미세먼지':
#     print('마스크를 챙겨라')
# else:
#     print("준비물 필요 없음")

# #기온입력값에 따른 대답
# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워여. 나가지 마요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <=temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워.나가지마")

#대기번호 short cut
# print('대기번호 : 1')
# print('대기번호 : 3')
# print('대기번호 : 3')
# print('대기번호 : 4')
#
# for waiting_no in [0,1,2,3,4]:
# for waiting_no in range(1,6): #1,2,3,4,5
#     print('대기번호 : {0}'.format(waiting_no))

# #응용 - 카페 대기번호
# starbucks = ['Iron', 'Thor', "groot"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

#while
# customer = 'Thor'
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index = 0:
#         print("커피가 폐기처분되었습니다.")

#호출과 무한루프
# customer = "Iron"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

#조건이 만족할떄까지 반복
# customer = "Thor"
# person = 'unknown'
#
# while person != customer:
#     print("{0}, 커피가 준비되었습니다".format(customer))
#     person = input("이름이?")

#continue, repeating
# absent = [2, 5] #결석
# no_book = [7] #책을 깜빡함
# for student in range(1, 11): #1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#출석 번호가 1,2,3,4, 앞에 100을 붙이기ㅗ 함 --> 101~104..
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# #학생 name = 길이로 변환
# students = ["sam","Groot","Gill","Dannael"]
# students = [len(i) for i in students]
# print(students)

#학생이름을 대문자로 변환
# students = ["sam","Groot","Gill","Dannael"]
# students = [i.upper() for i in students]
# print(students)

#Q - Cocoa 서비스를 이용하는 택시 기사
# 50 명의 승객과 매칭기회가 왔을 떄, 총 탑승 승객 수를 구하는 프로그램을 작성해라
#
# 조건1: 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해짐
# 조건2: 당신은 소요시간 5~ 15분 사이의 승객만 매칭해야 함
#
# [O] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [O] 3번째 손님 (소요시간: 5분)
# ...
# [] 50번째 손님 (소요시간 : 16분)
#
# 총 탑승 승객 : 2분
# solution
# from random import *
# cnt = 0 #총 탑승 승객수
# for i in range(1,51): # 1~50 이라는 수(승객)
#     time = randrange(5, 51) #5~50분 소요시간
#     if 5 <= time <= 15:# 5~15분 이내의 손님, 탑승 승객수 증가 처리
#         print("[O] {0}번째 손님 (소요시간: {1}분)".format(i, time))
#         cnt += 1
#     else: #매칭 실패한 경우
#         print("[] {0}번째 손님 (소요시간: {1}분)".format(i, time))
#
# print("총 탑승 승객 : {0}분".format(cnt))