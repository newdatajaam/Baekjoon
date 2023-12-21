import re

def solution(files):
    answer = []
    my_files = []
# enumerate하는 이유: 개별 파일의 원본 정수 인덱스도 필요, 파일명
    for idx,s in enumerate(files): 
        # 1-1) 정규식으로 숫자파트 추출
        number = re.findall(r"\d+",s)
        real_number = int(number[0])
        # 1-2) head 추출
        head = s[:s.index(number[0])]
        head = head.lower()
        # 1-3) 필요한 정보를 모아서 추가
        my_files.append([head,real_number,idx])

		# 2) 문제대로 정렬을 수행 
    my_files.sort(key = lambda x: (x[0],x[1],x[2]))

		# 3) 출제자가 원하는 스타일로 정리해서 출력
	    # for j in my_files: # j : [h,n,org_idx]
	    #     answer.append( files[j[2]])
    answer = [ files[j[2]] for j in my_files ]

    return answer 