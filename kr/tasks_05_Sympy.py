# -*- coding: utf-8 -*-
'''sympy.solve'''

# from sympy import *
import numpy as np
from sympy import *
import codecs
import sys

import scipy_temp as doc_temp  

file_format = 'ode_%d.tex'

desc4 = r'Решите уравнение $$%s$$' # 
ans4 = r'Ответ: $$%s$$' # 

x = symbols('x', rational=True)
y = Function('y')(x)
f = Function('f')
C, C1, C2 = symbols("C C_1 C_2")

# Филиппов
tv5 = [ 
  # var 1 
  {
    'eq': Eq(x*y.diff(x) - 2*y, 2*x**4), # 136
    'ans': Eq(y, x**2*(C1 + x**2))
  },
  # var 2 
  {
    'eq': Eq(x*y.diff(x) + x**2 +x*y - y, 0),  # 301
    'ans': Eq(y, x*(C1*exp(-x) - 1))
  },
  # var 3 
  {
    'eq': Eq(2*x*y.diff(x) + y**2, 1),   # 302
    'ans': Eq(y, (C1 + x)/(-C1 + x))
  },
  # var 4 
  {
    # 'eq': Eq((x*y.diff(x) + y)**2, x**2*y.diff(x))  # 304 NotImplementedError: The given ODE -x**2*Derivative(y(x), x) + (x*Derivative(y(x), x) + y(x))**2 cannot be solved by the lie group method
    'eq': Eq(y.diff(x)*x**2 + x*y, -1), # 140
    'ans': Eq(y, (C1 - log(x))/x)
  },
  # var 5 
  {
    'eq': Eq(y - y.diff(x), y**2 + x*y.diff(x)), # 305
    'ans': Eq(y, C1*(x + 1)/(C1*x + C1 - 1))
  },
  # var 6 
  {
    # 'eq': Eq((x+2*y**3)*y.diff(x), y) # 306
    # [Eq(y, 6**(1/3)*(-2*3**(1/3)*C1/(-9*x + sqrt(3)*sqrt(-4*C1**3 + 27*x**2))**(1/3) - 2**(1/3)*(-9*x + sqrt(3)*sqrt(-4*C1**3 + 27*x**2))**(1/3))/6),
    #  Eq(y, 2**(1/3)*(-2*C1/((-3**(1/3) - 3**(5/6)*I)*(-9*x + sqrt(3)*sqrt(-4*C1**3 + 27*x**2))**(1/3)) + 6**(1/3)*(-9*x + sqrt(3)*sqrt(-4*C1**3 + 27*x**2))**(1/3)/12 + 2**(1/3)*3**(5/6)*I*(-9*x + sqrt(3)*sqrt(-4*C1**3 + 27*x**2))**(1/3)/12)),
    # Eq(y, 2**(1/3)*(-2*C1/((-3**(1/3) + 3**(5/6)*I)*(-9*x + sqrt(3)*sqrt(-4*C1**3 + 27*x**2))**(1/3)) + 6**(1/3)*(-9*x + sqrt(3)*sqrt(-4*C1**3 + 27*x**2))**(1/3)/12 - 2**(1/3)*3**(5/6)*I*(-9*x + sqrt(3)*sqrt(-4*C1**3 + 27*x**2))**(1/3)/12))]
    'eq': Eq(y, x*(y.diff(x) - x*cos(x))), # 141
    'ans': Eq(y, x*(C1 + sin(x)))
  },
  # var 7
  {
    # 'eq': Eq((y.diff(x))**3- y.diff(x)*exp(2*x), 0) # 307
    # находится только решение Eq(y, C1) и не находится y=C+e^x, y=C-e^x
    'eq': Eq((x*y.diff(x) - 1)*log(x), 2*y), # 143
    'ans': Eq(y, (C1*log(x) - 1)*log(x))
  },
  # var 8 
  {
    # 'eq': Eq(x**2*y.diff(x), y*(x+y)) # 308
    # решение находится в виде, которое неудобно для проверки
    # Eq(y, x/(C1 - log(x)))
    'eq': Eq(x*y.diff(x) + (x+1)*y, 3*x**2*exp(-x)), # 144
    'ans': Eq(y, (C1 + x**3)*exp(-x)/x)
  },
  # var 9 
  {
    'eq': Eq(x**2*y.diff(x) - 2*x*y, 3*y), # 312
    'ans': Eq(y, C1*x**2*exp(-3/x))
  },
  # var 10
  {
    # 'eq': Eq(x + y*y.diff(x), y**2*(1+y.diff(x)**2) ) # 313
    # 'ans': [Eq(y, -sqrt(4*x - 4*(C1 + x)**2 + 1)/2),
 # Eq(y, sqrt(4*x - 4*(C1 + x)**2 + 1)/2)]
    'eq': Eq(y.diff(x)*sin(2*x), 2*(y+cos(x))), # 178
    'ans':Eq(y, C1*tan(x) - 2*sin(x)/sin(2*x))

 },
  # var 11
  {
    # 'eq': Eq(y, (x*y.diff(x)+2*y)**2 ) # 314 Exception
    # 'eq': Eq((2*exp(y)-x)*y.diff(x), 1) # 146
    # 'ans': Eq(y, x*exp(-C1)/2 - x**3*exp(-3*C1)/48 + 3*x**5*exp(-5*C1)/1280 + C1 + O(x**6))
    # 'eq': Eq( (sin(y)**2 + x* ctg(y))*y.diff(x), 1) # 147 долго
    # 'eq' : Eq( y.diff(x), y/(3*x - y**2)) # 149
    # Eq(y, -143*x**5/C1**9 - 30*x**4/C1**7 - 7*x**3/C1**5 - 2*x**2/C1**3 - x/C1 + C1 + O(x**6)) - разложение в ряд
    'eq': Eq( y.diff()+2*y, y**2*exp(x)), # 151
    'ans': Eq(y, exp(-2*x)/(C1 + exp(-x))) 
  },
  # var 12
  {
    # 'eq': Eq(y.diff(x), 1/(x-y**2) ) # 315
    # 'ans': Eq(y, x**5*(-4*C1*(83*C1 + 33) - 2*C1*(-C1*(-236*C1 - 105) + 167*C1 + 66) - 213*C1 - 60/C1**11)/60 + C1 - C1*x - 3*C1*x**2/2 + C1*x**3*(C1 - 4)/3 + 5*C1*x**4*(C1 - 3)/12 + O(x**6))
    # 'eq': Eq( x*y**2*y.diff(x), x**2+y**3) # 154 complex solution
    # 'ans': [Eq(y, (C1*x - 3)**(1/3)*Abs(x)**(2/3)),
           # Eq(y, (-1 - sqrt(3)*I)*(C1*x - 3)**(1/3)*Abs(x)**(2/3)/2),
           # Eq(y, (-1 + sqrt(3)*I)*(C1*x - 3)**(1/3)*Abs(x)**(2/3)/2)]
    # 'eq': Eq( x*y**2*y.diff(x), x+y**2) # 155 NotImplementedError 
    # 'eq': Eq(x**2*y.diff() + x*y + x**2*y**2, 4) # 167 вроде не сходится с ответом
    # 'ans': Eq(y, 2*(C1*x**3 + 1/x)/(C1*x**4 - 1))
    
    # 'eq': Eq(y.diff(x)+2*y*exp(x)-y**2, exp(2*x)+exp(x)) # 171 разложение в ряд
    # 'ans': Eq(y, 2*x + x**2*(C1 - 1)/2 + x**3*(-2*C1 + 5)/6 + x**4*(13*C1 - 7)/24 + x**5*(C1*(C1 + 9) + 3*C1 + 61)/120 + C1 + O(x**6))
    
    'eq': Eq(y.diff(x, x) - 2*y.diff(x) + y, sin(x)),
    'ans': Eq(y, (C1 + C2*x)*exp(x) + cos(x)/2)
  }
  
]


def print_solve(var, tex_file):
  t = tv5[var]
  print(doc_temp.new_task, file=tex_file)
  print(desc4 % latex(t['eq']), file=tex_file)
  if 'ans' in t:
    res = t['ans']
  else:
    res = dsolve(eq)
  print(ans4 % latex(res), file=tex_file)

if __name__ == '__main__':
  tn = len(tv5)
  # tn = 1
  for i in range(tn):
    print('variant %d'%i)
    with codecs.open(file_format % (i+1), 'w', encoding="utf-8") as f:
      print_solve(i, f)
    print('... done')