# -*- coding: utf-8 -*-
'''integrals'''

from sympy import *
import codecs
import scipy_temp as doc_temp  
import sys

file_format = 'integral_%d.tex'

desc1 = r'Найдите интеграл $$\int %s, dx$$' # Integral( f, dx)
desc2 = r'Найдите интеграл $$\int_{%s}^{%s} %s\, dx$$.' # Integral( f, dx)

x = symbols('x')
#n, m = symbols('n m', positive=True, integer=True)

tv2 = [ 
  # var 1 
  {
    'int': x**2,
    'dint': [1, 2, x**2, Rational(7,3)]
  },
  # var 2 
  {
    'int': 1/(1-cos(x)),  # 1669
    'dint': [0, pi, exp(x)*(cos(x)), -exp(pi)/2 - 1/2] # 2279
  },
  # var 3 
  {
    # 'int': 1/sqrt(3*x**2-2),  # 1664 acosh
    'int': x/sqrt(1-x**2),  # 1644
    'dint': [0, E, (x*log(x))**2, -Rational(2,27) + 5*exp(3)/27]   # 2270 D
    
  },
  # var 4 
  {
    'int': 1/(5*x-2)**Rational(5,2),  # 1658
    'dint': [-1, 1, x/(x**2+x+1), -sqrt(3)*pi/6 + log(3)/2] # 2269
  },
  # var 5 
  {
    'int': 1/(2-3*x**2),              # 1662
    'dint': [-oo, oo, 1/(x**2+1), pi, atan(x)]     # 2336
  },
  # var 6 
  {
    'int': 1/sqrt(2-3*x**2),          # 1663
    'dint': [0, pi, x*sin(x), pi, -x*cos(x) + sin(x)]         # 2240 D
  },
  # var 7
  {
    'int': 1/(1+cos(x)),              # 1668
    'dint': [0, log(2), x*exp(-x), -log(2)/2 + 1/2, (-x - 1)*exp(-x) ]    # 2239 D
  },
  # var 8 
  {
    'int': 1/(sin(2*x+pi/4))**2,      # 1667
    'dint': [0, 2*pi, x**2*cos(x), 4*pi, x**2*sin(x) + 2*x*cos(x) - 2*sin(x)]    # 2241 D
  },
  # var 9 
  {
    'int': (exp(-x)+exp(-2*x)),        # 1665
    'dint': [-oo, oo, 1/(x**2+x+1)**2, 4*sqrt(3)*pi/9, (2*x + 1)/(3*x**2 + 3*x + 3) + 4*sqrt(3)*atan(2*sqrt(3)*x/3 + sqrt(3)/3)/9]     # 2339
  },
  # var 10
  {
    'int': root(1-2*x+x**2, 5)/(1-x),        # 1660
    'dint': [0, 2*pi, 1/((2+cos(x))*(3+cos(x))), 0]  # 2275
  },
  # var 11
  {
    'int': x**2*root(1+x**3, 3),        # 1675
    'dint': [0, oo, 1/(1+x**3), 2*sqrt(3)*pi/9, log(x + 1)/3 - log(x**2 - x + 1)/6 + sqrt(3)*atan(2*sqrt(3)*x/3 - sqrt(3)/3)/3] # 2340 D
  },
  # var 12
  {
    'int': x/(4+x**4),                  # 1678
    'dint': [0, oo, (x**2+1)/(x**4+1), sqrt(2)*pi/2, sqrt(2)*(2*atan(sqrt(2)*x/2) + 2*atan(sqrt(2)*x**3/2 + sqrt(2)*x/2))/4]         # 2341
  }
  
]

# ************************************************
# Решаем заменой переменных:
# Демидович: 2271, 2272
# **    'dint': [1, 9, x*root(1-x,3), 468*(-1)**(1/3)/7]     # 2271 решать заменой переменных t = 1-x, в лоб получаем исключение, ибо нужно сказать, что 1-x>=0

    # 'nint': [0, 1, sin(x/pi)*cos(x-0.15)] # mkvas, list 2
    # 'nint': [0, pi/2, sin(x)*sin(2*x)*sin(3*x)]   # 2277 too long
    # 'nint': [0, 2*pi, 1/((sin(x))**4+(cos(x))**4)] # 2276
    # 'dint': [0, pi/2, (sin(x))**n]     # 2281

def print_integral(var, tex_file):
  f = tv2[var]['int']
  print(doc_temp.new_task, file=tex_file)
  print(desc1 % (latex(f)), file=tex_file)
  res = integrate(f)
  print(doc_temp.desc_ans % latex(res), file=tex_file)

def print_dintegral(var, tex_file):
  d = tv2[var]['dint']
  a0 = d[0]
  a1 = d[1]
  f = d[2]
  print(doc_temp.new_task, file=tex_file)
  print(desc2 % (latex(a0), latex(a1), latex(f)), file=tex_file)
  if len(d) == 4:
    res = d[3]
  else:
    res = integrate(f, (x, a0, a1))
  print(doc_temp.desc_ans % (latex(res)), file=tex_file)

if __name__ == '__main__':
  tn = len(tv2)
  # tn = 2
  for i in range(tn):
    print('variant %d'%i)
    with codecs.open(file_format % (i+1), 'w', encoding="utf-8") as f:
      print_integral(i, f)
      print_dintegral(i, f)
    print('... done')