import numpy as np
from scipy.integrate import quad,dblquad,nquad
from scipy.optimize import minimize
from scipy.optimize import root
from pylab import *
from scipy.interpolate import interp1d
from scipy import linalg as lg
def main():
    #1--Integral
    print(quad(lambda x:np.exp(-x),0,np.inf)) #jifen  1~wuqiong
    print(dblquad(lambda t,x:np.exp(-x*t)/t**3,
                  0,np.inf,#t de fan wei
                  lambda x:1,lambda x:np.inf)) #erweijifen   x de fanwei
    def f(x,y):
        return x*y
    def bound_y():
        return [0,0.5]
    def bound_x(y):
        return [0,1-2*y]
    print(nquad(f,(bound_x,bound_y))) #n weijifen

    # 2--Optimizer
    def rosen(x):
        return sum(100.0*(x[1:]-x[:1]**2.0)**2.0+(1-x[:1])**2.0)
    x0 = np.array([1.3,0.7,0.8,1.9,1.2])
    res=minimize(rosen,x0,method="nelder-mead",options={"xtol":1e-8,"disp":True})
    print("ROSE MINI:",res.x)
    # def func(x):
    #     return (2*x[0]*x[1]+2*x[0]-x[0]**2-2*x[1]**2)
    # def func_deriv(x):
    #     dfdx0 = (-2*x[0]+2*x[1]+2)
    #     dfdx1 = (2*x[0]-4*x[1])
    #     return np.array([dfdx0,dfdx1])
    # cons=({"type":"eq","fun":lambda x:np.array([x[0]**3-x[1]]),"jac":lambda x:np.array([3.0*(x[0]**2.0,-1.0)])},
    #       {"type": "ineq", "fun": lambda x: np.array([x[1] - 1]), "jac": lambda x: np.array([0.0,1.0])})
    # res = minimize(func,np.array([-1.0,1.0]),jac=func_deriv,constraints=cons,method='SLSQP',options={'disp':True})
    # print("RESTRICT:",res)
    def fun(x):
        return x+2*np.cos(x)
    sol = root(fun,0.1)
    print("ROOT:",sol.x,sol.fun)
    #3--Inter
    x = np.linspace(0,1,10)
    y=np.sin(2*np.pi*x)
    li = interp1d(x,y,kind = "cubic")
    x_new = np.linspace(0,1,50)
    y_new = li(x_new)
    figure()
    plot(x,y,"r")
    plot(x_new,y_new,"k")
    show()
    print(y_new)
    #4--Linear
    arr = np.array([[1,2],[3,4]])
    print("Det:",lg.det(arr))
    print ("Inv:",lg.inv(arr))
    b=np.array([6,14])
    print("Sol:",lg.solve(arr,b))
    print("Eig:",lg.eig(arr))
    print ("LU:",lg.lu(arr))
    print ("QR:",lg.qr(arr))
    print ("SVD:",lg.svd(arr))
    print ("Schur:",lg.schur(arr))
    
if __name__ == "__main__":
    main()