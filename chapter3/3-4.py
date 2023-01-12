# 미등록 형태소 출력 예시
from konlpy.tag import Komoran

komoran = Komoran()
text = "우리 챗봇은 엔엘피를 좋아해."
pos = komoran.pos(text)
print(pos)
# >> [('우리', 'NP'), ('챗봇은', 'NA'), ('엔', 'NNB'), ('엘', 'NNP'), ('피', 'NNG'), ('를', 'JKO'), ('좋아하', 'VV'), ('아', 'EF'), ('.', 'SF')]
# 엔엘피 -> ('엔', 'NNB'), ('엘', 'NNP'), ('피', 'NNG')