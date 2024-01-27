from sympy import *
'''
def newton() :
    g1_ = 1
    g2_ = 1
    n, m = [float(x) for x in input("Enter a , b : ").split()]
    x0 = Matrix([[n],[m]])
    a, b, c, r,o, k,f,z,e,s = [float(x) for x in input("Enter ax² + bx + c + ry² + oy + k + fxy + zx²y + ey²x + sy²x² : ").split()]

    while g1_ != 0 or g2_ != 0 : 
        n = x0[0]
        m = x0[1]

        g1 = f"{2*a}x + {b} + {f}y + {2 * z}xy + {e}y² + {2 * s}xy²" 
        g2 = f"{2 * r}y + {o} + {f}x + {z}x² + {2 * e }xy + {2 * s}x²y"  

        #print(f"\n\ngrad(x0) = ({g1} ; {g2})")

        g1_ = 2*a * n + b + f * m + 2 * z * n * m + e * m**2 + 2 * s * n * m**2 
        g2_ = 2 * r * m + o + f * n + 2 * (n**2) + 2 *e * n * m + 2 * s * (n**2) * m
        
        g = Matrix([[g1_],[g2_]])
        
        s1 = f"{2 * a} + {2 * z}y + {2 * s}y²"
        s2 = f"{f} + {2 * z}x + {2 * e}y + {4 * s}xy"
        s3 = f"{2 * z}x + {2 * e}y + {4 * s}xy +{f}"
        s4 = f"{2 * r} + {2 * e}x + {2 * s}x²"

        s1_ = 2 * a + 2 * z * m + 2 * s * m**2
        s2_ = f + 2 * z * n + 2 * e * m + 4 * s * n* m
        s3_ = 2 * z *n + 2 * e * m + 4 * s * n * m +f
        s4_ = 2 * r  + 2 * e * n + 2 * s * n**2

        mat = Matrix([[s1_, s3_], [s2_, s4_]])

        i = mat.inv()
        
        x1=x0 - i * g

        g1_ = 2*a * x1[0] + b + f * x1[1] + 2 * z * x1[0] * x1[1] + e * x1[1]**2 + 2 * s * x1[0] * x1[1]**2 
        g2_ = 2 * r * x1[1] + o + f * x1[0] + z * (x1[0]**2) + 2 *e * x1[0] * x1[1] + 2 * s * (x1[0]**2) * x1[1]
        
        if g1_ == 0 and g2_ == 0 :
            print(g1_)
            print(g2_)
            print("OK")
            break ;
        else :
            print("WE ARE REPEATING......")
            x0 = x1

'''
def gradient_constant() :
    g1_ = 1
    g2_ = 1
    n, m = [float(x) for x in input("Enter a , b : ").split()]
    x0 = Matrix([[n],[m]])
    a, b, c, r,o, k,f,z,e,s = [float(x) for x in input("Enter ax² + bx + c + ry² + oy + k + fxy + zx²y + ey²x + sy²x² : ").split()]
    alpha = float(input("Donnez Alpha : "))
    while g1_ != 0 or g2_ != 0 : 
        n = x0[0]
        m = x0[1]

        g1_ = 2*a * n + b + f * m + 2 * z * n * m + e * m**2 + 2 * s * n * m**2 
        g2_ = 2 * r * m + o + f * n + 2 * (n**2) + 2 *e * n * m + 2 * s * (n**2) * m

        d0 = -1 * Matrix([[g1_], [g2_]])

        x1 = x0 - alpha * d0
        
        g1_ = x1[0]
        g2_ = x1[1] 

        if g1_ == 0 and g2_ == 0 :
            print(g1_)
            print(g2_)
            print("OK")
            break ;
        else :
            print("WE ARE REPEATING......")
            x0 = x1


gradient_constant()