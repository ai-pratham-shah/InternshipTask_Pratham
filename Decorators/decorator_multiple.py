def decorator1(pattern):
    def wrapper():
        result = pattern()
        return result
    return wrapper
def decorator2(pattern):
    def wrapper(*args):
        pattern(*args)
        print(args[0])
        pattern(*args)
    return wrapper
@decorator1
def static_string():
    stringg = "aktiv"
    return stringg
@decorator2
def pattern(stringg):
    print("* * * * *")
    print("% % % % %")
stringg = user_input()
pattern(stringg)
