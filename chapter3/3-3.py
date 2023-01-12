# 트위터에서 만든 형태소 분석기(성능 중하)
from konlpy.tag import Okt

# Okt 형태소 분석기 객체 생성
okt = Okt()
text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = okt.morphs(text)
print('형태소 추출')
print(morphs)

# 형태소와 품사 태그 추출
pos = okt.pos(text)
print('형태소와 품사 캐트 추출')
print(pos)

# 명사만 추출
nouns = okt.nouns(text)
print('명사만 추출')
print(nouns)

# 정규화, 어구 추출
text = "오늘 날씨가 좋아욬ㅋㅋ"
print('정규화')
print(okt.normalize(text))
print('어구 추출')
print(okt.phrases(text))

# 매우 빠른 분석 속도, 정규화 기능 존재
# 사용자 추가 형태소 관리 어려움, 구어 분석에 대해 부족