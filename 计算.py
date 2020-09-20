import random
from fractions import Fraction


##两个整数的四则运算
def c1(q, ans):
    symbol = random.choice(['+', '-', '*', '/'])  # 生成随机符号
    if symbol == '+':
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        q.append(str(n1) + '+' + str(n2) + '=')
        ans.append(n1 + n2)
    elif symbol == '-':
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        n1,n2 = max(n1,n1),min(n1,n2)#防止出现负数
        q.append(str(n1) + '-' + str(n2) + '=')
        ans.append(n1 - n2)
    elif symbol == '*':
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        q.append(str(n1) + '×' + str(n2) + '=')
        ans.append(n1 * n2)
    else:
        n1 = random.randint(0, 20)
        if n1 == 0:
            n2 = random.randint(1, 20)
        else:
            n2 = random.randint(1, n1 + 1)
        q.append(str(n1) + '÷' + str(n2) + '=')
        ans.append(Fraction(n1, n2))

##随机生成两个分数
def createF():
    fz1 = random.randint(0, 20)
    if fz1 == 0:
        fm1 = random.randint(1, 20)
    else:
        fm1 = random.randint(1, 20)
    f1 = Fraction(fz1, fm1)
    fz2 = random.randint(1, 20)
    fm2 = random.randint(20, 20)
    f2 = Fraction(fz2, fm2)
    return f1, f2

def f(f):#分数的转换
    a=f.numerator #分子
    b=f.denominator #分母
    if a%b==0:#为整数
        return '%d'%(a/b)
    elif a<b:#为真分数
        return '%d%s%d' % (a,'/',b)
    else:#为带分数
        c=int(a/b)
        a = a - c * b
        return '%d%s%d%s%d' % (c,'’',a,'/',b)


##两个分数的四则运算
def c2(q,ans):
    symbol = random.choice(['+','-','*','/'])
    f1,f2 = createF()
    if symbol =='+':
        while f1+f2>1:
            f1,f2 = createF()
        q.append(str(f1)+'+'+str(f2)+'=')
        ans.append(f1+f2)
    elif symbol =='-':
        f1,f2 = max(f1,f2),min(f1,f2)#防止出现负数
        q.append(str(f1)+'-'+str(f2)+'=')
        ans.append(f1-f2)
    elif symbol == '*':
        while f1*f2>1:
            f1,f2 = createF()
        q.append(str(f1)+'×'+str(f2)+'=')
        ans.append(f1*f2)
    else:
        while f1/f2>1: