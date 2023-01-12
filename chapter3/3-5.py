# 미등록 품사 사용자 포멧을 이용한 형태소 분석
from konlpy.tag import Komoran

komoran = Komoran(userdic='./user_dic.tsv')
text = "우리 챗봇은 엔엘피를 좋아해."
pos = komoran.pos(text)
print(pos)

text = "나는 내일, 어제의 너와 만난다"
pos = komoran.pos(text)
print(pos)

text = "시샵"
pos = komoran.pos(text)
print(pos)