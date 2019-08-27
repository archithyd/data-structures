def mix_up(a, b):
    x=a[1]
    y=b[1]
    s=list(a)
    r=list(b)
    s[1]=y
    r[1]=x
    a=''.join(s)
    b=''.join(r)
    c=a
    a=b
    b=c
 
    return (a,b)   

print(mix_up("archit","sharma"))