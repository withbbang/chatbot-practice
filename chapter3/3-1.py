# 카이스트가 만든 형태소 분석기
from konlpy.tag import Kkma
# 꼬꼬마 형태소 분석기 객체 생성
kkma = Kkma()
text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = kkma.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = kkma.pos(text)
print(pos)

# 명사만 추출
nouns = kkma.nouns(text)
print(nouns)

# 문장 분리
sentences = "오늘 날씨는 어때요? 내일은 덥다던데."
s = kkma.sentences(sentences)
print(s)

# Kkma
# 성능이 좋고 지원하는 품사가 많음
# 분석 속도가 느리고 사용자 추가 형태소에 대해 불완전하게 동작함