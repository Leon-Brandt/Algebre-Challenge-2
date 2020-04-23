#Solving Algorithm for Linear Equations

def solve_equation(a,b):

    for i in range(1,100):
        for y in range(1,100):
            if a * i  +  b * y == 0:
                return(i,y)
            if a * i * -1  +  b * y == 0:
                return(-i,y)
            if a * i  +  b * y * -1 == 0:
                return(i,-y)
            if a * i * -1  +  b * y * -1 == 0:
                return(-i,-y)


print(solve_equation(6,4))





