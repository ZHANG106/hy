from collections import OrderedDict

fish = list(map(int, input().split(" ")))
m = fish[1]
fish = fish[2:]
fish.sort()
dic_fish = OrderedDict()
for i in fish:
    if dic_fish.get(i):
        dic_fish[i] += 1
    else:
        dic_fish.update({i: 1})

for i in range(m):
    fkeys = list(dic_fish.keys())
    if dic_fish[fkeys[0]] == 1:
        if dic_fish.get(fkeys[0] + fkeys[1]):
            dic_fish[fkeys[0] + fkeys[1]] += 1
        else:
            dic_fish[fkeys[0] + fkeys[1]] = 1
        dic_fish.pop(fkeys[0])
        if dic_fish[fkeys[1]] == 1:
            dic_fish.pop(fkeys[1])
        else:
            dic_fish[fkeys[1]] -= 1
    else:
        if dic_fish.get(fkeys[0] + fkeys[1]):
            dic_fish[fkeys[0] + fkeys[1]] += 1
        else:
            dic_fish[fkeys[0] + fkeys[1]] = 1
        dic_fish[fkeys[0]] -=1
        if dic_fish[fkeys[1]] == 1:
            dic_fish.pop(fkeys[1])
        else:
            dic_fish[fkeys[1]] -= 1
    ps = sorted(dic_fish.items(),key=lambda x:x[0])
    dic_fish = {i:j for i,j in ps}

fkeys = list(dic_fish.keys())
print(fkeys[0])