def processRut(rut):
    rut = rut.replace(".","").upper()
    return rut

def checkRut(rut):
    try:
        id, dv = rut.split("-")
        id = list(map(int,reversed(id)))
        serial = [2,3,4,5,6,7]
        s = 0
        for i in range(len(id)):
            s += id[i]*serial[i%6]
        s = 11 - (s%11)
        if s == 11:
            s = "0"
        elif s == 10:
            s = "K"
        else:
            s = str(s)
        return dv == s

    except Exception:
        return False