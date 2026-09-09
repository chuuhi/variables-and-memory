def challenge_01():
    # 1 local
    # #1. Is the outer_value variable assigned here the global outer_value, or a local outer_value? How can we be sure?
    outer_value = 42

    print(f"The value from outside is: {outer_value}")

def challenge_02():
    # 2 global
    print(f"The value from outside is: {outer_value}")

def challenge_03():
    # 3 local
    inner_value = 42
    print(f"The value from outside is: {inner_value}")

    

def challenge_04():
    outer_value = 42
    print(f"The value from outside is: {outer_value}")

    

outer_value = 1729