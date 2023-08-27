s = "abcabcbb"
print(s)
lener = len(s)
print(lener)
stwo=""
counter = 0
arr_main = []
for i in range(0,lener):
    stwo = s[i]
    dulener = len(stwo)
    if stwo[-1]==s[i]:
        arr_main.append(stwo)
    elif s[i] in stwo:
        arr_main.append(stwo)
    elif s[i] not in stwo:
        stwo = stwo + s[i]
max_index = arr_main.index(max(arr_main))
print(max_index)
print(arr_main[max_index])
print(arr_main)