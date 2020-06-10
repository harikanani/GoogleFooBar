def get_biggest_square(max_number):
    n=1
    while(n*n < max_number+1):
        n=n+1
    return n-1

def solution(area):
    if(area > 1000000 or area < 1):
        raise ValueError('Area is outside of bounds')
    list_num=[]
    while(area != 0):
        res=get_biggest_square(area)
        list_num.append(res*res)
        area-=res*res
        
    return list_num

print(solution(12))
print(solution(15324))
