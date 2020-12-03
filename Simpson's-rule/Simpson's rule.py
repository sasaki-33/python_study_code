import math

def simpson(a):
    i = 0
    kekka = 0
    h = 1/(2*a)
    
    def kansuu(b):
        c = 0
        if b == 0:
            c = 1
        else:
            c = math.sqrt(1-((b*h)**2))
        return c
    
    while i < a :
        kekka = kekka + kansuu(2*i) + 4*kansuu(2*i+1) + kansuu(2*i+2)
        i += 1
    
    final_a = (kekka*h)/3
    final_b = math.floor(final_a*(10**9))
    return final_b

Nx = 2
Ny = Nx + 2

while simpson(Nx) != simpson(Ny) :
    Nx = Ny
    Ny = Ny + 2

print('一致した分割数は{}である。'.format(Nx))
rule = simpson(Nx)/(10**9)
print('題意を満たす積分値は{}である。'.format(rule))