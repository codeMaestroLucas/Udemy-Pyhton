"""
<<< Herança Múltipla >>>
Herança múltipla é quando uma classe herda de mais de uma classe.
Ex.:
Classes A, B, C, D

D(B, C)  C(A)  B(A)  A
A ordem de herança importa: D(B, C) != D(C, B)

      A
     / \
    B   C
     \ /
      D
O python precisa decidir qual o caminho que super(D, self) vai usar. Por isso é necessário definir um MRO para a classe em Heranças Múltiplas.
"""
