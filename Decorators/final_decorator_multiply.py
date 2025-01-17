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
stringg = static_string()
pattern(stringg)
import time
start_time = time.time()
print("Start time:", start_time)
end_time = time.time()
print("End time:", end_time)
print("Execution time:", end_time-start_time)
