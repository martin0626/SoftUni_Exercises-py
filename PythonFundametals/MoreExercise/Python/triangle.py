a = float (input())
step = float (input())

def on_step (num, on):
    result = a**step
    return result

print (on_step(a,step))

