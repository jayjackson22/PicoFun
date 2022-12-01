import utime as time
def printtime():
    return ('{:02d}:{:02d}:{:02d} '.format(time.localtime()[3], time.localtime()[4], time.localtime()[5]), end='')