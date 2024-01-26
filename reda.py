from sympy import *

n, m = [int(x) for x in input("Enter a , b : ").split()]
x0 = Matrix([[n],[m]])

def newton() :
    a, b, c, r,o, k,f,z,e,s = [int(x) for x in input("Enter ax² + bx + c + ny² + my + k + fxy + zx²y + ey²x + sy²x² : ").split()]

    g1 = f"{2*a}x + {b} + {f}y + {2 * z}xy + {e}y² + {2 * s}xy²" 
    g2 = f"{2 * r}y + {o} + {f}y + {2 * z}x + {2 * e}xy + {2 * s}x²y"  

    print(f"\n\ngrad(x0) = ({g1} ; {g2})")

    g1_ = 2*a * n + b + f * m + 2 * z * n * m + e * m**2 + 2 * s * n * m**2 
    g2_ = 2 * r * m + o + f * m + 2 * z * n + 2 *e * n * m + 2 * s * n**2 * m

    s1 = f"{2 * a} + {2 * z}y + {2 * s}y²"
    s2 = f"{f} + {2 * z}x + {2 * e}y + {4 * s}xy"
    s3 = f"{2 * z} + {2 * e}y + {4 * s}xy"
    s4 = f"{2 * r} + {f} + {2 * e}x + {2 * s}x²"

    s1_ = 2 * a + 2 * z * m + 2 * s * m**2
    s2_ = f + 2 * z * n + 2 * e * m + 4 * s * n* m
    s3_ = 2 * z + 2 * e * m + 4 * s * n * m
    s4_ = 2 * r + f + 2 * e * n + 2 * s * n**2

    mat = Matrix([[s1_, s3_], [s2_, s4_]])
    print("\n")
    pprint(mat)

    print("\n")
    pprint(mat.inv())

newton()
