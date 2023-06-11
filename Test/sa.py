def find_sum(a,b):
    try:
        print(a+c)
    except ValueError:
        print("function name error")
    finally:
        print("Sum finally")


try:
    find_sum(12,21)
except NameError:
    print("Invocation name errror")
finally:
    print("Invokation finaalky")