# Shineware에서 개발한 형태소 분석기
from konlpy.tag import Komoran

# 코모란 형태소 분석기 객체 생성
komoran = Komoran()
text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = komoran.morphs(text)
print('형태소 추출')
print(morphs)

# 형태소와 품사 태그 추출
pos = komoran.pos(text)
print('형태소와 품사 태그 추출')
print(pos)

# 명사만 추출
nouns = komoran.nouns(text)
print('명사만 추출')
print(nouns)

# 오탈자에 강함, 사용자 추가 형태소 관리가 용이함