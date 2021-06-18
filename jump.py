def jump(n):
    if n <= 2:
        return n
    return jump(n-2) + jump(n-1)

    
if __name__ == "__main__":
    print(jump(4))