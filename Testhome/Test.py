import math


def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 0:
        return 1


# left is the left index for the interval
# right is the right index for the interval
# k is the desired index value, where array[k] is the (k+1)th smallest element when left = 0
def median(array, left, right):
    k = len(array) / 2
    while right > left:
        # use select recursively to sample a smaller set of size s
        # the arbitrary constants 600 and 0.5 are used in the original
        # version to minimize execution time
        if right - left > 600:
            n = right - left + 1
            i = k - left + 1
            z = math.log(n)
            s = 0.5 * math.exp(2 * z / 3)
            sd = 0.5 * math.sqrt(z * s * (n - s) / n) * sign(i - n / 2)
            newLeft = int(max(left, k - i * s / n + sd))
            newRight = int(min(right, k + (n - i) * s / n + sd))
            median(array, newLeft, newRight)
        # partition the elements between left and right around t
        t = array[k]
        i = left
        j = right
        array[left], array[k] = array[k], array[left]
        if array[right] > t:
            array[right], array[left] = array[left], array[right]
        while i < j:
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1
            while array[i] < t:
                i = i + 1
            while array[j] > t:
                j = j - 1
        if array[left] == t:
            array[left], array[j] = array[j], array[left]
        else:
            j = j + 1
            array[j], array[right] = array[right], array[j]
        # adjust left and right towards the boundaries of the subset
        # containing the (k - left + 1)th smallest element
        if j <= k:
            left = j + 1
        if k <= j:
            right = j - 1


m = input()
ar = map(int, raw_input().split())
median(ar, 0, len(ar) - 1)
print ar[m / 2]
