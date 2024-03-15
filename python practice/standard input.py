#sep, separate function
#print("Python", "Java", "JavaScript", sep=" vs ")

#print("Python", "Java", sep=",", end="?")
#print("무엇이 더 재밌을까요?")
#end = output = 2줄이 아니라 1줄로 출력

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
    #print(sub, score)
    # print(subject.ljust(8), str(score).rjust(4), sep=":")
#print(n.ljust(no.) --> left organise,(공간확보)


#은행 대기 순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))
#     #zfill(3) = 3개만큼의 공간 확보, 값을 집어넣음, 없을시 0으로 처리하는 func
#     # 1 ==> 001

#입력된 값을 변수로 input
# answer = input("아무 값이나 입력하세요 : ")
# answer = 10
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")
# 사용자 입력을 통해서 값을 받게된다면 항상 문자열 형태로 저장됨

# ---- 8-2 다양한 출력 포맷
#빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총 10자리 공간 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로_로 채움
# print("{0:_<10}".format(500))
# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
# # print("{0:+,}".format(100000000000))
# # print("{0:+,}".format(-100000000000))
# # 3자리마다 콤마를 찍어주기, 부호도 붙이기, 자릿수 확보하기
# #돈많으면 기분이 행복하니까 빈자리는 ^로 채워주기

# print("{0:^<+30,}".format(100000000000))
#소수점 출력
# print("{0:f}".format(5/3))
#소수점 특정 자릿수 까지만 표시 (소수점 3번째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

#8.3 파일 입출력
#파일을 열어서 불러옴/ 쓸수도 있음
#W = write로 쓰기위해 작성하는 것으로
#encoding = "utf8" - 한글 문자를 썼을 때 이상하게 출력되는 경우가 있을 수 있음
#파일을 열었으면 닫아햐함
#1
# score_file = open("score.txt", "w", encoding = "utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
#파일을 형성함

#2
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("＼n코딩 : 100")
# score_file.close()

#파일 읽기 ("read")
# score_file = open("score.txt", "r", encoding = "utf8")
#파일 속 모든 내용을 읽는 도구
# print(score_file.read())
# score_file.close()

#한 줄만 읽기
# score_file = open("score.txt", 'r', encoding = "utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커ㅓ서는 다음 줄로 이동
# print(score_file.readline(), end = " ")
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#반복문을 통해 파일 불러오기
# score_file = open("score.txt", "r", encoding = "utf8" )
# while True:
#     line = score_file.readline()
#     if not line:
#         break #반복문 탈출
#     print(line, end= "")
# score_file.close()

#list에 값을 넣어서 처리하기
# score_file = open("score.txt", "r", encoding = "utf8" )
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end = "")
# score_file.close()
# #리스트에서 한줄씩 가져와서 실행하는 기능

#__8.4 pickle
#pickle - 데이터를 파일형태로 저장
#데이터를 pickle이라는 도구를 사용하여 파일을 형성하고, 저장, 내용을 load를 저장, 변수에 저장해서 계속 쓸 수 있는 유용한 library
#wb writing binary
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이":30, "취미":["축구","골프", "달리기"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기 데이터 형태로
# print(profile)
# profile_file.close()

#__8.5 with function
# import pickle
# #현재 실행중인 코드를 닫을 필요 없음
# #이미 생성한 파일을 여는 입력문
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

#단 2줄만에 파일 형성할 수 있음
#매번  close입력문을 통해 마무리 짓지 않아도 되는 장점이 있음
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
#
# with open("study.txt", 'r', encoding='utf8') as study_file:
#     print(study_file.read())

#8-6 퀴즈
# Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다:
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
#
# - X 주차 주간보고
# 부서 :
# 이름 :
# 업무 요약 :
#
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건: 파일명은 '1주차.txt', '2주차.txt', ...과 같이 만듭니다


# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")


