
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:44:39 2018

@author: 
"""
import numpy as np
import sympy as sym
sym.init_printing(forecolor="White")
from sympy.plotting import plot
import matplotlib.pyplot as plt
import functools



#入力列を変数，数値に分けてsplitする関数
#IN  文字列 ex.("x y z w")
#OUT list(str,int,float混合)
def split(list_):
    for i,X in enumerate(list_):
        try:
            list_[i]=float(X)
            if list_[i]%1 ==0:
                list_[i]=int(X)                
        except ValueError:
            list_[i]= sym.Symbol(X)#変数宣言
    return list_


#指定の変数を列ベクトル(sympy.Matrix)にする関数
#IN  変数のlist，スペース区切りの文字列 ex.("x y z w")
#OUT 列ベクトル(sympy.Matrix)
def vertical_vector(symbol):
    #分割
    list_=symbol.split(",")
    #数字を分離
    split(list_)
    vertical_vector = (sym.Matrix(list_))
    display(vertical_vector)
    return vertical_vector

#指定の変数を行列(sympy.Matrix)にする関数
#IN  変数のlist，スペースおよびコンマ区切りの文字列(乗数のみ引数に取ります) ex.("x y z w")
#OUT 行ベクトル(sympy.Matrix)
def num_matrix(symbol):
    #分割
    list_=symbol.split(",")
    XY_LENGTH=len(list_)**0.5
    if XY_LENGTH %1 !=0:
        raise IndexError("要素数は平方にしてください．\n許される引数の例は('x,y,z,w')や('1,2,3,4,5,6,x,y,z')です ")
    #数字を分離
    list_=split(list_)
    list_=sym.Matrix(list_).reshape(int(XY_LENGTH),int(XY_LENGTH))
    display(list_)
    return list_

#指定の変数を下付の行列(sympy.Matrix)にする関数
#IN  行数，列数，置く文字
#OUT 行列(sympy.Matrix)
def subscript_matrix(size,size2,*,symbol="r"):
    P=sym.Matrix(sym.symbols(f"{symbol}(1:{size+1})(1:{size2+1})")).reshape(size,size2)
    return P
