def decorator1(pattern):
    def wrapper():
        pattern()
        print("Done")
    return wrapper
def decorator2(pattern):
    def wrapper():
        pattern()
        print("Done")
    return wrapper
@decorator1
@decorator2
def pattern():
    print("* * * * *")
    print("% % % % %")
    s="Aktiv"
    print(s)
    print("% % % % %")
    print("* * * * *")
pattern()
