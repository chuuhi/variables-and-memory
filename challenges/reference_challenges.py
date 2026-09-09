def challenge_01():
    apples = 1729
    oranges = 42
    papaya = apples
    # 1 apples and papaya = same id
    apples = apples + oranges
    # 2 after reassignment, apples id changes, papaya same as old id

def challenge_02():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]
    # 3

def challenge_03():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]

    challenge_03_helper(bananas)

def challenge_03_helper(kiwis):
    mangos = 315
    kiwis.append(mangos)
    # 4