import math

def zetaDieta(C, P, G):
    calAmount = math.ceil(C / 27) * 105
    calAmount += math.ceil(P / 30) * 120
    calAmount += G * 9
    return calAmount

print(zetaDieta(88, 90, 55))