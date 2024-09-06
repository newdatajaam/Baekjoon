def solution(sizes):
    max_w, max_h = 0,0
    
    for card in sizes:
        w, h = min(card), max(card)
        max_w = max(max_w, w)
        max_h = max(max_h, h)
            
    return max_w * max_h


# def solution(sizes):
#     max_w, max_h = 0,0
    
#     for card in sizes:
#         w, h = min(card), max(card)
#         if max_w < w:
#             max_w = w
#         if max_h < h:
#             max_h = h
            
#     return max_w * max_h