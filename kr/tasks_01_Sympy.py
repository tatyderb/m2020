# -*- coding: utf-8 -*-
'''limits'''
# https://github.com/sympy/sympy/blob/master/sympy/series/tests/test_demidovich.py

from sympy import *
import scipy_temp as doc_temp  
import sys
import codecs

file_format = 'limit_%d.tex'
desc = r'Вычислите предел при $%s$ стремящемся к $%s$ функции $$%s$$' # x, to, f

x, n = symbols('x n')

tv1 = [ 
  # 1
  {
    'f' : 1000*x/(x**2+1),
    'x' : x,
    'to': oo
  },
  {
    'f' : sin(x)/x,
    'x' : x,
    'to': 2
  }, 
  # 2
  {
    'f' : sin(x)/x,
    'x' : x,
    'to': 0
  }, 
  {
    'f' : (sqrt(x+sqrt(x+sqrt(x))))/sqrt(x+1),
    'x' : x,
    'to': oo
  }, 
  # 3
  {
    'f' : sqrt(n+1) -sqrt(n),   # 1
    'x' : n,
    'to': oo
  }, 
  {
    'f' : sin(3*x)/x,
    'x' : x,
    'to': 0
  }, 
  # 4
  {
    'f' : (2**(x+1)+3**(x+1))/(2**x+3**x),
    'x' : x,
    'to': oo
  },
  {
    'f' : sin(5*x)/sin(2*x),
    'x' : x,
    'to': 0
  }, 
  # 5
  {
    'f' : n/2**n,
    'x' : n,
    'to': oo
  },
  {
    'f' : sin(pi*x)/sin(3*pi*x),
    'x' : x,
    'to': 0
  }, 
  # 6
  {
    'f' : 2**n/factorial(n),
    'x' : n,
    'to': oo
  },
  {
    'f' : x*sin(pi/x),
    'x' : x,
    'to': oo
  }, 
  # 7
  {
    'f' : (x+1)*(x+2)*(x+3)/x**3,
    'x' : x,
    'to': oo
  },
  {
    'f' : (1-cos(x))/x**2,
    'x' : x,
    'to': 0
  }, 
  # 8
  {
    'f' : (2*x**2-x+3)/(x**3-8*x+5),
    'x' : x,
    'to': oo
  },
  {
    'f' : x*sin(1/x),
    'x' : x,
    'to': oo
  }, 
  # 9
  {
    'f' : (2**(x + 1) + 3**(x + 1))/(2**x + 3**x), # == 3  # 175
    'x' : x,
    'to': oo
  },
  {
    'f' : sqrt(x + 1) - sqrt(x) , # == 0  # 179
    'x' : x,
    'to': oo
  }, 
  # 10
  {
    'f' : (x + 1)*(x + 2)*(x + 3)/x**3, # == 1  # 172
    'x' : x,
    'to': oo
  },
  {
    'f' : x/root(x**3 + 10, 3), #  x, oo) == 1  # Primjer 2
    'x' : x,
    'to': oo
  }, 
  # 11
  {
    'f' : (2*x - 3)*(3*x + 5)*(4*x - 6)/(3*x**3 + x - 1), #  == 8  # Primjer 1
    'x' : x,
    'to': oo
  },
  {
    'f' : (2*x**2 - 3*x - 4)/sqrt(x**4 + 1), #  oo) == 2  # 186
    'x' : x,
    'to': oo
  }, 
  # 12
  {
    'f' : (x + 1)**2/(x**2 + 1), # oo) == 1  # 181
    'x' : x,
    'to': oo
  },
  {
    'f' : (2*x + 3)/(x + root(x, 3)),  #  oo) == 2  # 187
    'x' : x,
    'to': oo
  }, 
  # 13
  {
    'f' : 1000*x/(x**2 - 1), #  oo) == 0  # 182
    'x' : x,
    'to': oo
  },
  {
    'f' : x**2/(10 + x*sqrt(x)),  # oo) == oo  # 188
    'x' : x,
    'to': oo
  }, 
  # 14
  {
    'f' : (x**2 - 5*x + 1)/(3*x + 7), # oo) == oo  # 183
    'x' : x,
    'to': oo
  },
  {
    'f' : root(x**2 + 1, 3)/(x + 1), #  oo) == 0  # 189
    'x' : x,
    'to': oo
  }, 
  # 15
  {
    'f' : (2*x**2 - x + 3)/(x**3 - 8*x + 5), # oo) == 0  # 184
    'x' : x,
    'to': oo
  },
  {
    'f' : sqrt(x)/sqrt(x + sqrt(x + sqrt(x))), # oo) == 1  # 190
    'x' : x,
    'to': 2
  }, 
  # 16
  {
    'f' : (1/(1 - x) - 3/(1 - x**3)), #  1) == -1  # 198
    'x' : x,
    'to': 1
  },
  {
    'f' : sqrt(x**2 - 5*x + 6) - x, #  oo) == -Rational(5)/2  # 213
    'x' : x,
    'to': oo
  } 
    
]

def print_limit(var, tex_file):
  d = tv1[var]
  print(doc_temp.new_task, file=tex_file)
  print(desc % (d['x'], latex(d['to']), latex(d['f'])), file=tex_file)
  f = limit(d['f'], d['x'], d['to'])
  print(doc_temp.desc_ans % latex(f), file=tex_file)

if __name__ == '__main__':
  tn = len(tv1)
  # tn = 2
  for i in range(tn//2):
    print('variant %d'%i)
    with codecs.open(file_format % (i+1), 'w', encoding="utf-8") as f:
      print_limit(2*i, f)
      print_limit(2*i+1, f)
    print('... done')
