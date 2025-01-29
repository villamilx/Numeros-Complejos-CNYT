import math

def Suma(c1, c2):
    po = round(c1[0] + c2[0], 2)
    so = round(c1[1] + c2[1], 2)
    return (po, so)

def multiplicacion(c1, c2):
    po = round(c1[0] * c2[0] - c1[1] * c2[1], 2)
    so = round(c1[0] * c2[1] + c1[1] * c2[0], 2)
    return (po, so)

def division(c1, c2):
    denominator = (c2[0]**2 + c2[1]**2)
    if denominator == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    po = round(((c1[0] * c2[0])+(c1[1] * c2[1])) / denominator, 2 )
    so = round(((c1[1] * c2[0])-(c1[0] * c2[1])) / denominator, 2 )
    return (po, so)

def resta(n1, n2):
    po = round(n1[0] - n2[0], 2)
    so = round(n1[1] - n2[1], 2)
    return (po, so)

def modulo(n):
    num = round((n[0]**2 + n[1]**2)**0.5, 2)
    return num

def conjugado(n):
    return (round(n[0], 2), round(n[1] * -1, 2))

def Fase(n):
    if n[1] == 0:
        if n[0] > 0:
            angulo = 0
        elif n[0] < 0:
            angulo = math.pi
        else:
            raise ZeroDivisionError("Can't divide by zero")
    elif n[0] == 0:
        angulo = math.pi / 2 if n[1] > 0 else -math.pi / 2
    else:
        angulo = math.atan2(n[1], n[0])
    return round(angulo, 2)

def CardToPolar(coord):
    x, y = coord[0], coord[1]
    r = round(((x**2) + (y**2))**0.5, 2)
    t = Fase(coord)
    return [r, t]

def PolarToCard(coord):
    r = coord[0]
    theta = coord[1]
    pr = r * math.cos(theta)
    pi = r * math.sin(theta)
    return (round(pr, 2), round(pi, 2))
