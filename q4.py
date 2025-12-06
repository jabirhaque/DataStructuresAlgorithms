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
        backtrack(current+[1], prefix+1, k-1, result)
        backtrack(current+[0], prefix, k-1, result)
        if prefix>0: backtrack(current+[-1], prefix-1, k-1, result)
        return

    result = []
    backtrack([], 0, k, result)
    return result