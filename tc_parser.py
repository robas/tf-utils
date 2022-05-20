TCR0 = "0"


def filterTC(tcs, tc):
    result = []
    currentTCR = {}
    toAppendTC = {}
    i = 0

# Olhar essa merda, e refazer!
    while i < len(tcs):
        currentTCR = dict(tcs[i])

        if currentTCR.get("Transaction Code") != tc:
            if toAppendTC:
                result.append(toAppendTC)
                toAppendTC = {}
            i = i + 1
            continue

        if currentTCR.get("Transaction Component Sequence Number") == TCR0:
            if toAppendTC:
                result.append(toAppendTC)
                toAppendTC = {}
            toAppendTC = currentTCR
        else:
            toAppendTC = mergeDicts(toAppendTC, currentTCR)
        i = i + 1

    if toAppendTC:
        result.append(toAppendTC)

    # for obj in tcs:
    #    d = dict(obj)
    #    if d.get("Transaction Code") == tc:
    #        result.append(d)
    return result


def getTCR(tcs, i):
    if i < len(tcs):
        return tcs[i]
    else:
        return None


def getTCFields(record, fields):
    result = []
    record = dict(record)
    for field in fields:
        # print(record.get(field))
        value = record.get(field)
        if value == None:
            result.append("NOT FOUND")
        else:
            result.append(value)
    return result


def mergeDicts(x, y):
    z = x.copy()
    z.update(y)
    return z
