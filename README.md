# sympy_MATRIX
sympyを利用した行列の簡易生成

python3


行列を定義する関数．
n×m行の変数，定数入り混じった行列が簡単に定義，計算できます．

例：
A=num_matrix("1,2,3,4")
B=num_matrix("5,6,x1,x2")

print(sym.latex(A*B))

<a href="https://www.codecogs.com/eqnedit.php?latex=\left[\begin{matrix}2&space;x_{1}&space;&plus;&space;5&space;&&space;2&space;x_{2}&space;&plus;&space;6\\4&space;x_{1}&space;&plus;&space;15&space;&&space;4&space;x_{2}&space;&plus;&space;18\end{matrix}\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left[\begin{matrix}2&space;x_{1}&space;&plus;&space;5&space;&&space;2&space;x_{2}&space;&plus;&space;6\\4&space;x_{1}&space;&plus;&space;15&space;&&space;4&space;x_{2}&space;&plus;&space;18\end{matrix}\right]" title="\left[\begin{matrix}2 x_{1} + 5 & 2 x_{2} + 6\\4 x_{1} + 15 & 4 x_{2} + 18\end{matrix}\right]" /></a>

