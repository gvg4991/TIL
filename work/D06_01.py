# def route(num):
# #num=int(input())
#     a=1
#     b=num
#     while round(float(a),6) != round(float(b),6):
#         print(f'{a**2}<{num}<{b**2}')
#         if ((a+b)/2)**2 > num:
#             b=(a+b)/2
#         else:
#             a=(a+b)/2
#     c=round(float(a),6)
#     return c
    
# print(route(81))


###강사님
def my_sqrt(n):
    x,y = 1, n
    result = 1

    # while abs(result**2 - n)>0.000001:
    #     result=(x+y)/2
    #     if result**2 < n:
    #         x=result
    #     else:
    #         y= result
    # return result

    import math
    while not math.isclose(result**2,n):
        result=(x+y)/2
        if result**2 < n:
            x=result
        else:
            y= result
    return result
