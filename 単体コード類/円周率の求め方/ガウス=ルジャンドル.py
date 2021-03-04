import numpy as np

def new(a,b,t,p):
    a_n = (a+b)/2
    b_n = np.sqrt(a*b)
    t_n = t-p*(a-a_n)**2
    p_n = 2*p

    return [a_n,b_n,t_n,p_n]

a = 1.0
b = np.sqrt(2)/2
t = 1/4
p = 1.0

pi_0 = (a+b)**2/(4*t)
print(pi_0)

for i in range(2):
    a,b,t,p = new(a,b,t,p)
    new_pi = (a+b)**2/(4*t)
    print(new_pi)