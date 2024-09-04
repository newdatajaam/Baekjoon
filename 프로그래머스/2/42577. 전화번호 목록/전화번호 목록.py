def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
    return answer

# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book, key= lambda x: len(x))
    
#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[j][:len(phone_book[i])] == phone_book[i]:
#                 return False
#     return True

# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book, key=lambda x : len(x))

#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             l = len(phone_book[i])
#             if phone_book[i] == phone_book[j][0:l]:
#                 answer = False
    
#     return answer