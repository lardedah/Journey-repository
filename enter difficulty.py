def max_health(mode):
    if mode == "easy":  #.lower()
        return 100
    elif mode == "medium":  #.lower()
        return 75
    else:
        return 35

mode = input ("enter difficulty: ")
x = mode
print (max_health(x))