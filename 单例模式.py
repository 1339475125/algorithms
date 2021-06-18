

class Test:
    __instance = None

    def  __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


test = Test(13, "wangruihuan")
