def sar(k):
    if k % 2 == 0:
        result = []
        for i in range(k):
            if i < k/2: result.append(1)
            else: result.append(-1)
        return result
    result = sar(k - 1)
    result.append(0)
    return result

def is_sar(sar):
    if len(sar) == 0: return True
    prefix = []
    prefix.append(sar[0])
    for i in range(1, len(sar)):
        prefix.append(prefix[i-1]+sar[i])
        if prefix[i] < 0: return False
    return prefix[len(sar)-1] == 0

def all_sars(k):
    def backtrack(current, prefix, k, result):
        if k == 0 and prefix == 0:
            result.append(current)
            return
        if prefix > k: return
        copy1 = [item for item in current]
        copy1.append(1)
        backtrack(copy1, prefix+1, k-1, result)
        copy2 = [item for item in current]
        copy2.append(0)
        backtrack(copy2, prefix, k-1, result)
        if (prefix>0):
            copy3 = [item for item in current]
            copy3.append(-1)
            backtrack(copy3, prefix-1, k-1, result)
        return

    result = []
    backtrack([], 0, k, result)
    return result

def check_all_sars(sars):
    for sar in sars:
        if not is_sar(sar): return False
    return True

for i in range(0, 16):
    print(check_all_sars(all_sars(i)))