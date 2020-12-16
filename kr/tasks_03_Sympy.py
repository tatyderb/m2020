# -*- coding: utf-8 -*-
'''sympy.solve'''

from sympy import *
import codecs
import scipy_temp as doc_temp  
import sys

file_format = 'solve_%d.tex'

desc1 = r'Найдите действительные корни уравнения $$%s$$' # Integral( f, dx)

x = symbols('x', rational=True)

# Задачи 152-... из файла C:\X41\stud\crec\самостоятельные\01_simplify\simplify.odt

tv3 = [ 
  # var 1 
  {
    'eq': Eq(sqrt(x+4),sqrt(2*x-1)),
  },
  # var 2 
  {
    'eq': Eq(root(2*x+3, 3), 1)
  },
  # var 3 
  {
    'eq': Eq(root(1-x, 3), 2)
  },
  # var 4 
  {
    'eq': Eq(root(3*x**2-3, 3), root(8*x, 3))
  },
  # var 5 
  {
    'eq': Eq(x+1, sqrt(1-x))
  },
  # var 6 
  {
    'eq': Eq(x, 1+sqrt(x+11))
  },
  # var 7
  {
    'eq': Eq(sqrt(x+3), sqrt(5-x))
  },
  # var 8 
  {
    'eq': Eq(sqrt(x**2-x-3), 3)
  },
  # var 9 
  {
    'eq': Eq(sqrt(x)-x, -12)
  },
  # var 10
  {
    'eq': Eq(x+sqrt(x), 2*(x-1))
  },
  # var 11
  {
    'eq': Eq(sqrt(x-1), x-3)
  },
  # var 12
  {
    'eq': Eq(sqrt(6+x-x**2), 1-x) 
  }
  
]

def print_solve(var, tex_file):
  eq = tv3[var]['eq']
  print(doc_temp.new_task, file=tex_file)
  print(desc1 % (latex(eq)), file=tex_file)
  res = solve(eq, x)
  print(doc_temp.desc_ans % latex(res), file=tex_file)

def generate_equation(var, tex_file):
  # (x + (var+1)*(+-1))*(x**2 + 1) = 0 - find only the relatives roots!!!
  
  s = var+1
  f = (x+s*(-1)**(s%2))*(x**2 + 1)
  feq = f.expand()
  # print(feq)
  eq = Eq(feq, 0)
  
  print(doc_temp.new_task, file=tex_file)
  print(desc1 % (latex(eq)), file=tex_file)
  print(doc_temp.desc_ans % latex(s*(-1)**(s%2+1)), file=tex_file)

if __name__ == '__main__':
  tn = len(tv3)
  # tn = 1
  for i in range(tn):
    print('variant %d'%i)
    with codecs.open(file_format % (i+1), 'w', encoding="utf-8") as f:
      print_solve(i, f)
      generate_equation(i, f )
    print('... done')