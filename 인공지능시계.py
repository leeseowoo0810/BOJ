h, m, s = map(int, input() .split())
t = int(input())

if s + t >= 60:
    m += (s+t)//60
    s += t - 60 * ((s + t) // 60)
    if m >= 60:
        h += m//60
        m = (m*0)+(m%h) 
        if h >= 24:
            h -= 24
else:
    s += s+t
print(f'{h} {m} {s}')   
