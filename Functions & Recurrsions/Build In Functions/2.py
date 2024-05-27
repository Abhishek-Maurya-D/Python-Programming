# default parameter

def cal_prod(a,b=2):
    print(a*b)
    return a*b

cal_prod(1)


def cal_prod(a=1,b=2):
    print(a*b)
    return a*b

cal_prod()


# def cal_prod(a=1,b):
#     print(a*b)
#     return a*b

# cal_prod(2)