import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())

print(soup.a) #처음으로 발견한 a tag
print(soup.a.attrs) #속성보여줌
print(soup.a["href"]) # a element의 href속성 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"})) #class="Nbtn_upload"인 a tag에 해당하는 첫번째 element 가져옴
print(soup.find(attrs={"class":"Nbtn_upload"}))

print(soup.find("li", attrs={"class":"rank01"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a) #soup.a랑 같음
print(rank1.a.get_text()) 
print(rank1.next_sibling) # tag사이 개행있을수 있음
print(rank1.next_sibling.next_sibling)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

print(rank1.parent)

rank1.find_next_sibling("li") #개행정보 무시,괄호안의 조건을 만족시키는거 찾음

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())


형제들을 한번에 여러개 가져옴
print(rank1.find_next_siblings("li"))
print(rank1.find_next_siblings("li")[0])

webtoon = soup.find("a",text="연애혁명-358. 딜레마존 (4)") #soup은 전체
print(webtoon)
