from machine import Pin
import time, utime


c4 = Pin(15, Pin.OUT)
c2 = Pin(14, Pin.OUT)
c3 = Pin(13, Pin.OUT)
c1 = Pin(12, Pin.OUT)

digits = [c1, c2, c3, c4]

a = Pin(0, Pin.OUT)
b = Pin(1, Pin.OUT)
c = Pin(2, Pin.OUT)
d = Pin(3, Pin.OUT)
e = Pin(4, Pin.OUT)
f = Pin(5, Pin.OUT)
g = Pin(6, Pin.OUT)
h = Pin(7, Pin.OUT)

all = [a, b, c, d, e, f, g]

chars = {
    "0": [a, b, c, d, e, f],
    "1": [b, c],
    "2": [a, b, d, e, g],
    "3": [a, b, c, d, g],
    "4": [b, c, f, g],
    "5": [a, c, d, f, g],
    "6": [a, c, d, e, f, g],
    "7": [a, b, c],
    "8": [a, b, c, d, e, f, g],
    "9": [a, b, c, d, f, g],
    ".": [h],
     "a": [a, b, c, d, e, g],
     "b": [c, d, e, f, g],
     "c": [a, d, e, f],
     "d": [a, b, c, d, g],
     "e": [a, b, d, e, f, g],
     "f": [a, e, f, g],
     "h": [c, e, f, g],
     "i": [b],
     "j": [a, b, c],
     "l": [d, e, f],
     "n": [c, e, g],
     "o": [b, c, d, g],
     "p": [a, b, e, f, g],
     "q": [a, b, c, f, g],
     "r": [e, g],
     "t": [d, e, f, g],
     "u": [b, c, d],
     "y": [a, b, c, e, g],
     "_": [c],
     "-": [g]
     }


def digit_on(number: int):
    global digits
    for d in range(len(digits)):
        if d == number:
            digits[d].off()
        else:
            digits[d].on()


def display_char(ch, dot=False):
    global chars
    global h
    for cx in all:
        if cx in chars[ch]:
            cx.on()
        else:
            cx.off()
        if dot:
            h.on()
        else:
            h.off()


if __name__ == "__main__":
    c4.off()
    c2.off()
    c3.off()
    c1.off()

    while True:
        current_time = utime.localtime()
        ft = "{:02d}{:02d}".format(current_time[1], current_time[2])
        for i in range(0, 4):
            di = ft[i]
            digit_on(i)
            display_char(di, i == 1)
            time.sleep(0.003)
