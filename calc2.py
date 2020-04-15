import J_plus
import H_multi
import M_minus


if __name__=='__main__':
    print("enter num1, num2")
    a,b=map(int, input().split())
    print("H_multi: ",H_multi.multi(a,b))
    print("J_Plus: ",J_plus.plus(a,b))
    print("M_minus: ",M_minus.minus(a,b))
