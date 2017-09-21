import time


def consumer(name):
    print("%s准备吃包子了" %name)
    while True:
        baozi = yield
        print("第%s盘包子来了，包子被%s吃了" %(baozi, name))


def producer(name):
    c1 = consumer("evescn")
    c2 = consumer("gmkk")
    c1.__next__()
    c2.__next__()

    print("厨师开始做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子")
        c1.send(i+1)
        c2.send(i+1)

producer("root")
