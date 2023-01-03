n = 10

for element in range(n, -n, -1):
    print(element, end = " ")
    if n < 0:
        break

# 10 9 8 7 6 5 4 3 2 1 0 
# 다시 해석 10 9 8 7 6 5 4 3 2 1 0 - 1 -2 -3 -4 -5 -6 -7 -8 -9
# 만약 if n 대신 element이라면 0 보다 작아지면 멈추니까 -1이 최종
# 10 9 8 7 6 5 4 3 2 1 0 -1