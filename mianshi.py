"""
斐波那契数列
"""


def fac(n):
    """ 
    递归调用
    """
    if not n:
        return 0
    return fac(n-1) + fac(n-2)



if __name__ == "__main__":
    fac(20)
