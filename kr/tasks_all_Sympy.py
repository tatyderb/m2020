# -*- coding: utf-8 -*-

from sympy import * 
import codecs

import scipy_temp as doc_temp 
import tasks_01_Sympy as tv1 
import tasks_02_Sympy as tv2
import tasks_03_Sympy as tv3
import tasks_04_Sympy as tv4
import tasks_05_Sympy as tv5
import tasks_06_Sympy as tv6

text_filename = 'task_00_Sympy.tex'

def make_tex() :
    with codecs.open(text_filename, "w", encoding="utf-8") as tex_file:
        # print(doc_temp.document_begin, file=tex_file)
      var_n = len( tv4.tv4)
      # var_n = 2
      for var in range(var_n) :

        print(doc_temp.new_variant, file=tex_file)
        print(doc_temp.input % (tv1.file_format % (var+1)), file=tex_file)
        print(doc_temp.input % (tv2.file_format % (var+1)), file=tex_file)
        print(doc_temp.input % (tv3.file_format % (var+1)), file=tex_file)
        print(doc_temp.input % (tv4.file_format % (var+1)), file=tex_file)
        print(doc_temp.input % (tv5.file_format % (var+1)), file=tex_file)
        print(doc_temp.input % (tv6.file_format % (var+1)), file=tex_file)
        
      #print(doc_temp.input % 'ode_bounds.tex', file=tex_file)
      print(doc_temp.input % 'ode_text.tex', file=tex_file)
        
     
        
if __name__ == '__main__':   
    make_tex()