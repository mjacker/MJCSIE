mz=[1, 0, 1, 2, 0, 1, 3]
cerosindex = [index for index, value in enumerate(mz) if value == 0]
cerosindex = cerosindex[::-1]
countzeros = len(cerosindex)
for x in cerosindex:
    mz.append(mz.pop(x))

print(mz)
