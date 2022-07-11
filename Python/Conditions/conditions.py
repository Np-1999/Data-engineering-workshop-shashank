x,y,z = 0, -1, 8
# if-else ladder
if x>y and x==0:
    print (f"boolean condition {x}<{y} and {x} ==0")
elif y>8 or x==0:
    print("Y is greater than 8")
else:
    print("Z is huge")

# Switch case is implemented using dictionary in python

def SwitchExample(argument):
    switcher = {
        0: "This is case zero",
        1: "This is case one",
        2: "This is case two"
    }
    return switcher.get(argument, "default case")

print(SwitchExample(0))