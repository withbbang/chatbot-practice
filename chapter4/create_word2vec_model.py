from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

# 네이버 영화 리뷰 데이터 읽어옴
def read_review_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:] # header 제거
    return data

# 측정 시작
start = time.time()

# 리뷰 파일 읽어오기
print('1) 말뭉치 데이터 읽기 시작')
review_data = read_review_data('./ratings.txt')
print(len(review_data)) # 리뷰 데이터 전체 개수
print('1) 말뭉치 데이터 읽기 완료: ', time.time() - start)

# 문장단위로 명사만 추출해 학습 입력 데이터로 만듬
print('2) 형태소에서 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료: ', time.time() - start)

# word2vec 모델 학습
print('3) word2vec 모델 학습 시작')
model = Word2Vec(sentences=docs, vector_size=200, window=4, min_count=2, sg=1)
# 하이퍼파라미터 설정: 사용자가 직접 세팅하여 품질을 높임
# sentences: Word2Vec모델 학습을 위한 문장 데이터. 모델의 입력값
# vector_size: 임베딩 벡터 차원의 크기
# window: 주변 단어 참조 윈도우 크기
# min_count: 단어 최소 빈도 수 제한(설정된 빈도 수 이하의 단어들은 학습하지 않음)
# sg: 0(COBW 모델 - window 주변 단어들로 타겟 단어 추측(속도 빠름)), 1(skip-gram모델 - 타겟 단어로 window 주변 단어들 추측(속도 느림))
print('3) word2vec 모델 학습 완료: ', time.time() - start)

# 모델 저장
print('4) 학습된 모델 저장 시작')
model.save('nvmc.model')
print('4) 학습된 모델 저장 완료: ', time.time() - start)

# 학습된 말뭉치 개수, 코퍼스 내 전체 단어 개수
print("corpus_count : ", model.corpus_count)
print("corpus_total_words : ", model.corpus_total_words)