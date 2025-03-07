from math import trunc

for i in range(2, 100):
    nines = int("9" * (i-1))
    divide = nines/i
    truncate = str(divide)[0:i-1]
    stripped = truncate.lstrip("0").lstrip(".").lstrip("0")
    print(stripped)

# for i in range(1, 100):
#     try:
#         print(str(int(round(int("9"*(i-1))/i, 0))/(10**(i-1))).lstrip("0").lstrip(".").lstrip("0"))
#     except:
#         print(i)
