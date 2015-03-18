__author__ = 'Wang Yc'
def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1
def strStr(haystack, needle):
    """find needle in haystack,
    Return the index of the first occurrence of needle in haystack"""
    for i in range(len(haystack)+1):
        for j in range(len(needle)+1):
            #print "i = ",i, "j = ",j
            if j == len(needle):
                return i
            if i + j == len(haystack):
                return -1
            if needle[j] != haystack[i + j]:
                break
def find_boyer_moore(T, P):
    m = len(T)
    n = len(P)
    if n == 0:  # trivial search for empty string
        return 0
    last = {}
    for k in range(n):
        last[P[k]] = k
    # align end of pattern at index m-1 of text
    i = n - 1
    k = n - 1
    while i < m:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1) # last(T[i]) is -1 if not found
            i += n - min(k, j + 1)
            k = n - 1
    return -1

def compute_kmp_fail(P):
    """Utility that computes and returns KMP fail list."""
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return fail
def find_kmp(T, P):
    n = len(T)
    m = len(P)
    if m == 0:
        return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return -1
s = "abab"
print compute_kmp_fail(s)
haystack = "mississippi"
needle = "si"
print find_brute(haystack, needle)
print strStr(haystack, needle)
print find_boyer_moore(haystack, needle)
print find_kmp(haystack, needle)