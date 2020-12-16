'''ODE краевая задача'''
"""
https://www.stewartcalculus.com/data/CALCULUS%20Concepts%20and%20Contexts/upfiles/3c3-2ndOrderLinearEqns_Stu.pdf
p 5, examples, p7, ex 17-24, 24 ...
"""

# -*- coding: utf-8 -*-
'''sympy.dsolve'''

# from sympy import *
from sympy import *
import codecs
import sys

import scipy_temp as doc_temp  

file_format = 'ode2_%d.tex'

desc4 = r'Найдите решение уравнение, удовлетворяющее краевым условиям  $$%s$$' # 
ans4 = r'Ответ: $$%s$$' # 

t = symbols('t', rational=True)
y = Function('y')(t)

# Филиппов
tv6 = [ 
  # var 1, p 5, example 5 
  {
    'tex': "y''+y'-6y = 0; y(0) = 1; y'(0) = 0",
    'eq': Eq(y.diff(t, 2)+y.diff(t)-6*y, 0), 
    'f0':0, # y
    't0':0,
    'y0':1,
    'f1':1, # y'
    't1':0,
    'y1':0,
    'ans': None
  },
  # var 2 , p 5, example 6
  {
    'tex': "y''+ y = 0; y(0) = 2; y'(0) = 3",
    'eq': Eq(y.diff(t, 2)+y, 0), 
    'f0':0, # y
    't0':0,
    'y0':2,
    'f1':1, # y'
    't1':0,
    'y1':3,
    'ans': None
  },
  # var 3 , p 5, example 7
  {
    'tex': "y''+ 2y'+ y = 0; y(0) = 1; y(1) = 3",
    'eq': Eq(y.diff(t, 2)+2*y.diff(t) + y, 0), 
    'f0':0, # y
    't0':0,
    'y0':1,
    'f1':0, # y'
    't1':1,
    'y1':3,
    'ans': None
  },
  # var 4, ex 17
  {
    'tex': "2 y''+ 5 y'+ 3 y = 0; y(0) = 3; y'(0) = -4",
    'eq': Eq(2*y.diff(t, 2)+5*y.diff(t) + 3*y, 0), 
    'f0':0, # y
    't0':0,
    'y0':3,
    'f1':1, # y'
    't1':0,
    'y1':-4,
    'ans': None
  },
  # var 5, ex 18
  {
    'tex': "y''+ 3 y = 0; y(0) = 1; y'(0) = 3",
    'eq': Eq(y.diff(t, 2)+ 3*y, 0), 
    'f0':0, # y
    't0':0,
    'y0':1,
    'f1':1, # y'
    't1':0,
    'y1':3,
    'ans': None
  },
  # var 6, F 755
  {
    'tex': "y''+ y = 1; y(0) = 0; y(\pi) = 0",
    'eq': Eq(y.diff(t, 2)+y, 1), 
    'f0':0, # y
    't0':0,
    'y0':0,
    'f1':0, # y'
    't1':pi,
    'y1':0,
    'ans': None
  },
  # var 7, F 756 (ОПЕЧАТКА, хорошее решение в тех условиях не получается, сделала y'(pi)=0
  {
    'tex': "y''+ y = 2 t - \pi; y(0) = 0; y'(\pi) = 0",
    'eq': Eq(y.diff(t, 2)+y, 2*t - pi), 
    'f0':0, # y
    't0':0,
    'y0':0,
    'f1':1, # y'
    't1':pi,
    'y1':0,
    'ans': None
  },
  # var 8, F 757
  {
    'tex': "y'' - y' - 2 y = 0; y'(0) = 2; y(\infty) = 0",
    'eq': Eq(y.diff(t, 2)-y.diff(t) -2* y, 0), 
    'f0':1, # y
    't0':0,
    'y0':2,
    'f1':0, # y'
    't1':oo,
    'y1':0,
    'ans': None
  },
  # var 9, p 7, ex 19
  {
    'tex': "4y''- 4y'+ y = 0; y(0) = 1; y'(0) = -1.5",
    'eq': Eq(4*y.diff(t, 2)-4*y.diff(t) + y, 0), 
    'f0':0, # y
    't0':0,
    'y0':1,
    'f1':0, # y'
    't1':1,
    'y1':-1.5,
    'ans': None
  },
  # var 10, p 7 ex 20
  {
    'tex': "2 y''+ 5y' -3 y = 0; y(0) = 1; y'(0) = 4",
    'eq': Eq(2*y.diff(t, 2)+5*y.diff(t) -3*y, 0), 
    'f0':0, # y
    't0':0,
    'y0':1,
    'f1':1, # y'
    't1':0,
    'y1':4,
    'ans': None
  },
  # var 11, p7 ex 21
  {
    'tex': "y''+ 16 y = 0; y(\pi/4) = -3; y'(\pi/4) = 4",
    'eq': Eq(y.diff(t, 2)+16* y, 0), 
    'f0':0, # y
    't0':pi/4,
    'y0':-3,
    'f1':1, # y'
    't1':pi/4,
    'y1':4,
    'ans': None
  },
  # var 12, p 7 ex 22
  {
    'tex': "y''- 2y' + 5 y = 0; y(\pi) = 0; y'(\pi) = 2",
    'eq': Eq(y.diff(t, 2)-2*y.diff(t) +5*y, 0), 
    'f0':0, # y
    't0':pi,
    'y0':0,
    'f1':1, # y'
    't1':pi,
    'y1':2,
    'ans': None
  },
  
]


def print_solve(var, tex_file):
  t = tv6[var]
  print(doc_temp.new_task, file=tex_file)
  #print(desc4 % latex(t['eq']), file=tex_file)
  print(desc4 % t['tex'], file=tex_file)
  if 'ans' in t:
    res = t['ans']
  else:
    res = dsolve(eq)
  print(ans4 % latex(res), file=tex_file)
  
def c_equation(rhs, fi, ti, yi):
    if fi == 0:
        f = rhs
    else:
        f = rhs.diff(t, fi)
    ceq = Eq(f.subs({t:ti}), yi)
    return ceq
    
def find_answer(task):
    eq = task['eq']
    print(eq)
    sol = dsolve(eq)
    print(sol)
    ceq1 = c_equation(sol.rhs, task['f0'], task['t0'], task['y0'])
    print(ceq1)
    ceq2 = c_equation(sol.rhs, task['f1'], task['t1'], task['y1'])
    print(ceq2)
    csol = solve([ceq1, ceq2])
    print(csol)
    yres = sol.rhs.subs(csol)
    print(yres)
    task['ans']=latex(yres)

if __name__ == '__main__':
  tn = len(tv6)
  # tn = 1
  for i in range(tn):
    print('variant %d'%(i+1))
    with codecs.open(file_format % (i+1), 'w', encoding="utf-8") as f:
        find_answer(tv6[i])
        print_solve(i, f)
    print('... done')