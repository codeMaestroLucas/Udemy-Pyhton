"""
<<<Herança Simples>>>
Ex.:
Classes A, B, C

C(B)  B(A)  A

    A
    |
    B
    |
    C
"""
class A:
    att_a: str = 'attr a'
    
    def meth(self):
        print('A')
    
        
class B(A):
    att_b: str = 'attr b'
    
    def meth(self):
        print('B')
    
        
class C(B):
    att_c: str = 'attr c'
    
    def meth(self):
        print('C')
    
    def super_meth(self):
        
        super(B, self).meth()
        super().meth()
        # super(C, self).meth() >> Msm coisa
        # OBS: O Super da classe A é o <object>
        
        print('C')

        
if __name__ == '__main__':
    c = C()
    print(c.att_a)
    print(c.att_b)
    print(c.att_c)

    c.meth()
    
    c.super_meth()
    
    print(C.mro()) # >> Method Resolution Order