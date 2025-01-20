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
    string = "aktiv"
    return string
@decorator2
def pattern(string):
    print("* * * * *")
    print("% % % % %")
string = static_string()
pattern(string)

