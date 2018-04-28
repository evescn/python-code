import time,threading

data = []

def run(n):
    data.append(n**n)
    return  n**n

t = threading.Thread(target=run,args=[8,])
t.start()
print(t)
print(data)