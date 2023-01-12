from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
text = "오늘 날씨는 구름이 많아요."

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)

# 단어 사전 구축 및 단어별 인덱스 부여
dics = {}
for word in nouns:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)

# 원-핫 인코딩
nb_classes = len(dics) # 차원의 크기
targets = list(dics.values()) # 객체의 값들 -> 배열화
print(targets)
one_hot_targets = np.eye(nb_classes)[targets] # 차원 크기만큼 단위행열 반환
print(one_hot_targets)