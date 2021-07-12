import re
p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 >care, cafe, case | caffe는 안됨 
# ^ (^de) : 문자열의 시작 > desk destination  | fade안됨
# $ (se$) : 문자열의 끝 > case, base | face

def print_match(m):
    if m:
        print("m.group() : ", m.group()) # 일치하는 문자열 반환 매치되지 않으면 에러 발생
        print("m.group() : ", m.string) #입력받은 문자열 출력
        print("m.start() : ", m.start()) #일치하는 문자열의 시작인덱스
        print("m.end() : ", m.end()) #일치하는 문자열의 끝인덱스
        print("m.span() : ", m.span()) #일치하는 문자열의 시작/끝인덱스
    else:
        print("not matched")

m = p.match("goodcare") #match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)


m = p.search("good care") #search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)


lst = p.findall("careless care cake") #일치하는 모든 것을 리스트형태로 반환
print(lst)
