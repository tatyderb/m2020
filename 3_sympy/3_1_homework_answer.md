# Домашняя работа по sympy

1 вариант на всех. В конце курса будет контрольная работа по sympy.


```python

```

## C.1

Раскройте скобки $a(a+3)(a-3)(a+2)$. Вычислите значение при $a=2$


```python

```




$\displaystyle a \left(a - 3\right) \left(a + 2\right) \left(a + 3\right)$




```python

```




$\displaystyle a^{4} + 2 a^{3} - 9 a^{2} - 18 a$



## C.2

Разложите на множители $a^{4} + 2 a^{3} - 9 a^{2} - 18 a$


```python

```




$\displaystyle a \left(a - 3\right) \left(a + 2\right) \left(a + 3\right)$



## C.3

Найдите функцию $f(g(h(x,y),z),t)$. Вычислите ее значение при $x=1,y=2,z=5,t=2.1$, если 
$$f(a,b)=\sin(10a+b)$$
$$g(a,b)=be^{-a}$$
$$h(a,b)=a+b$$


```python

```




$\displaystyle \sin{\left(t + 10 z e^{- x - y} \right)}$




```python

```




$\displaystyle \sin{\left(2.1 + \frac{50}{e^{3}} \right)}$




```python

```




$\displaystyle -0.992440668403706$



## C.4

Решить уравнение. Проверить найденные корни.
$$\sqrt{x+1}=3$$


```python

```




$\displaystyle \sqrt{x + 1} = 3$




```python

```




    [{x: 8}]




```python

```




$\displaystyle \text{True}$



# C.5

Решить уравнение. Проверить найденные корни.
$$\sqrt[3]{2x+3}=1$$


```python

```




$\displaystyle \sqrt[3]{2 x + 3} = 1$




```python

```




    [-1]



## С.6

Решить уравнение. Проверить найденные корни.
$$\sqrt{4 x + 2 \sqrt{2 x^{2} + 4}} = x+ 2$$


```python

```




$\displaystyle \sqrt{4 x + 2 \sqrt{2 x^{2} + 4}} = x + 2$




```python

```




    [0]



## C.7

Найдите **действительные** корни уравнения $$x^3 + 2x^2 + x = -2$$


```python

```




$\displaystyle x^{3} + 2 x^{2} + x = -2$




```python

```




    [-2]



## C.8

Решить уравнение относительно х. Проверить найденные корни.
$$\sqrt{x - 2} \sqrt{x + 1} = a $$



```python

```




$\displaystyle \sqrt{x - 2} \sqrt{x + 1} = a$




```python

```




    [{x: 1/2 - sqrt(4*a**2 + 9)/2}, {x: sqrt(4*a**2 + 9)/2 + 1/2}]



## C.9

Решить систему уравнений. 
$$\begin{cases}
2x_1 +x_2=10\\
x_1+x_2=17
\end{cases}$$


```python

```




$\displaystyle 2 x + y = 10$




```python

```




$\displaystyle x + y = 17$




```python

```




    {x: -7, y: 24}



# Пределы, интегралы, суммы

## C2.1

Найти предел функции $$\frac{x^{2} - 1}{2 x^{2} - x - 1}$$ при х стремящемся к:

* 0
* 1
* $\infty$


```python

```




$\displaystyle \frac{x^{2} - 1}{2 x^{2} - x - 1}$




```python

```




$\displaystyle 1$




```python

```




$\displaystyle \frac{2}{3}$




```python

```




$\displaystyle \frac{1}{2}$



## C2.2

$$lim_{x \to +\infty} \frac{\sqrt{x+\sqrt{x+\sqrt{x}}}}{\sqrt{x+1}}$$


```python

```




$\displaystyle \frac{\sqrt{x + \sqrt{\sqrt{x} + x}}}{\sqrt{x + 1}}$




```python

```




$\displaystyle 1$



## C2.3

Найти интеграл $$\int x^2\, dx$$


```python

```




$\displaystyle \frac{x^{3}}{3}$



## C2.4

Найти интеграл $$\int \frac{(2x+3)dx}{(x-2)(x+5)}$$


```python

```




$\displaystyle \log{\left(x^{2} + 3 x - 10 \right)}$



## С2.5

Найдите интеграл $$\int_{1}^{2} x\, dx$$


```python

```




$\displaystyle \frac{3}{2}$



## C2.6

Вычислите интеграл $$\int_{0}^{1} \frac{x dx}{x^2+x+1}$$ 


```python

```




$\displaystyle - \frac{\sqrt{3} \pi}{18} + \frac{\log{\left(3 \right)}}{2}$



## C3.1

Найдите с помощью sympy матрицу Х из уравнения

$$\begin{pmatrix}1 & 2\\
2 & 5
\end{pmatrix} 
X = 
\begin{pmatrix}4 & -6\\
2&1
\end{pmatrix}$$



```python

```


```python

```




$\displaystyle \left[\begin{matrix}16 & -32\\-6 & 13\end{matrix}\right]$




```python

```




    True



## C3.2 (Бутузов14а) Решить уравнение

Детерминант матрицы равен 0
$$\begin{vmatrix}3 & x & -4\\
2 & -1 & 3 \\
x+10 & 1 & 1
\end{vmatrix} = 0$$



```python

```




$\displaystyle \left[\begin{matrix}3 & x & -4\\2 & -1 & 3\\x + 10 & 1 & 1\end{matrix}\right]$




```python

```




$\displaystyle 3 x \left(x + 10\right) - 6 x - 60$




```python

```




    [-10, 2]




```python

```
