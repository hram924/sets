def elementlist(string):
    s = 0
    f = len(string)-1
    if string[0] == 
    
    
def sets(word,i):
    isto = "Word #" + str(i) + ": Set"
    isnot = "Word #" + str(i) + ": No Set"
    if word[0] == "{" and word[-1] == "}":
        if elementlist(word[1:-2]) == "No":
            print(isnot)
        else:
            print(isto)
    else:
        print(isnot)

tests = int(input())
i = 1
for i in range(tests):
    sets(input(), i + 1)
