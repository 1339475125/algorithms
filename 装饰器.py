


def debug(func):
    def wrapper():
        print("debug")
        return func()
    return wrapper


@debug
def hello():
    print("hello")


hello()