TCR0 = "0"


def filterTC(tcs, tc):
    result = []
    currentTCR = {}
    toAppendTC = {}
    i = 0

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
    for k in y:
        v = y[k]
        if k in x:
            tcr = y.get("Transaction Component Sequence Number")
            x[k+tcr] = v
        else:
            x[k] = v
    #z = x.copy()
    # z.update(y)
    return x
