# -*- coding: utf-8 -*-
'''sympy.solve'''

# from sympy import *
import numpy as np
from sympy import *
import codecs
import sys

import scipy_temp as doc_temp  

file_format = 'matrix_%d.tex'

desc4 = r'Найдите матрицу Х из уравнения \[%s\]' # 
ans4 = r'Ответ: \[X=%s\]' # 

x = symbols('x', rational=True)

def AXB(A, B, C=None):
# solve matrix equation AX=B,
# return equeation as latex
# return X
  s = latex(A) + r'\cdot X='+ latex(B)
  X = A.inv()*B
  return s, X

def XAB(A, B, C=None):
# solve matrix equation XA=B,
# return equeation as latex
# return X
  s = r'X \cdot' + latex(A) + '='+ latex(B)
  X = B*A.inv()
  return s, X

def AXAB(A, B, C=None):
# solve matrix equation AXA=B,
# return equeation as latex
# return X
  s = latex(A) + r'X \cdot' + latex(A) + '='+ latex(B)
  X = A.inv()*B*A.inv()
  return s, X

tv4 = [ 
  # Беклемышев, 15.56
  # var 1 
  {
    'A': Matrix([[2, 5],[1, 3]]),
    'B': Matrix([[2, 1],[1, 1]]),
    'eq': AXB
  },
  # var 2 
  {
    'A': Matrix([[2, 5],[1, 3]]),
    'B': Matrix([[2, 1],[1, 1]]),
    'eq': XAB
  },
  # var 3 
  {
    'A': Matrix([[2, 1],[1, 1]]),
    'B': Matrix([[10],[17]]),
    'eq': AXB
  },
  # var 4 
  {
    'A': Matrix([[1, 2, 0],[2, 5, -2], [0, -2, 5]]),
    'B': Matrix([[1,0, 0],[0, 1, 1],[0, 1, 0]]),
    'eq': AXB
  },
  # var 5 
  {
    'A': Matrix([[2, 2, -1],[2, -1, 2], [-1, 2, 2]]),
    'B': Matrix([[5, 5, 2],[5, 8, -1]]),
    'eq': XAB
  },
  # var 6 
  {
    'A': Matrix([[1, 2, 0],[2, 5, -2], [0, -2, 5]]),
    'B': Matrix([[1,0, 0],[0, 1, 1],[0, 1, 0]]),
    'eq': AXB
  },
  # var 7
  { # Бутузов стр 20, гл.I, пример
    'A': Matrix([[1, 1],[1, 2]]),
    'B': Matrix([[-1, 0],[3, 5]]),
    'eq': AXB
  },
  # var 8 
  {
    # Бутузов стр 20, 19а
    'A': Matrix([[1, 3],[1, 4]]),
    'B': Matrix([[1, -1],[-1, 1]]),
    'eq': AXB
  },
  # var 9 
  {
    # Бутузов стр 20, 19б
    'A': Matrix([[1, 1, -1],[2, 1, 0], [1, -1, 1]]),
    'B': Matrix([[1, -1, 3],[4, 3, 2]]),
    'eq': XAB
  },
  # var 10
  {
    # Бутузов стр 20, 19в
    'A': Matrix([[1, 1, -1],[2, 1, 0], [1, -1, 1]]),
    'B': Matrix([[1],[2],[3]]),
    'eq': AXB
  },
  # var 11
  {
    # Бутузов стр 20, 19г
    'A': Matrix([[-1, 0],[1, -1]]),
    'B': Matrix([[1, 2],[3, 4]]),
    'eq': AXAB
  },
  # var 12
  {
    # Беклемышев 15.65 13)
    'A': Matrix([[2, 2, -1],[2, -1, 2], [-1, 2, 2]]),
    'B': Matrix([[7],[1],[1]]),
    'eq': AXB
  }
  
]


def print_solve(var, tex_file):
  t = tv4[var]
  print(doc_temp.new_task, file=tex_file)
  f = t['eq']
  tex_eq, X = f(t['A'], t['B'])
  print(desc4 % tex_eq, file=tex_file)
  # print(tex_eq, file=tex_file)
  print(ans4 % latex(X), file=tex_file)
  # print( latex(X), file=tex_file)

if __name__ == '__main__':
  tn = len(tv4)
  # tn = 1
  for i in range(tn):
    print('variant %d'%i)
    with codecs.open(file_format % (i+1), 'w', encoding="utf-8") as f:
      print_solve(i, f)
    print('... done')