n = 1
s = 0
while n <= 100:
    s += n
    if s >= 1000:
        break
    n += 1

print("1부터 ",n,"까지의 합이 처음으로 1000을 넘습니다. 그 값은",s,"입니다.")
print("1000넘기 직전의 값은",(s-n),"입니다")