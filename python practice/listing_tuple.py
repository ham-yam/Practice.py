# # menu = ("돈까스", "치즈까스")
# # print(menu[0])
# # print(menu[1])
# #
# # #menu.add("생선까스")
# #
# # (name, age, hobby) = ("김",20, "코딩")
# # print(name,age,hobby)
# #
# # #집합(set)
# # #중복 안됨, 순서x
#
# my_set = {1,2,3,3,3}
# print(my_set)
#
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박병서"])
#
# #교집합 (java & python을 모두 할 수 있는 개발자
# print(java & python)
# print(java.intersection(python))
#
# #합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
# print(java| python)
# print(java.union(python))
#
# #차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
#
# #python할 줄 아는 사람이 늘어남
# python.add("김태로")
# print(python)
#
# #java를 잊었다
# java.remove("김태로")
# print(java)

# #자료구조의 변경
# #커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu = tuple(menu)
# print(menu, type(menu))
#
# print(menu, type(menu))
# menu = set(menu)
#

# Quiz) 학교에서 파이썬 코딩대회를 주최
# 참석률을 높이기위해 댓글 이벤트 진행
# 댓글 작성자들중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됨
# 추첨 프로그램을 작성해라
#
# 조건1: 편의상 댓글은 20명이 작성, 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용
#
# (출력예제)
# --당첨자 발표--
# 치킨 당첨자:1
# 커피 당첨자ㅣ [2,3,4]
# --축하합니다--
# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


from random import *
users = range(1,21)# 1부터 20까지 숫자를 생성
#print(type(users))
users = list(users)

#print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4ㅈ명중 1명은 치킨, 3명은 커피
print(" --당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")
