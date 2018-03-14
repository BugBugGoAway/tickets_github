# -*- coding: UTF-8 -*-


# 汉诺塔 a b c表示3个柱子，n表示柱子上的盘子
def hannuota(n, a , b , c):
    if n == 1:
        print(a + "==>" + c)
    # elif n == 2:
    #     print(a, "==>", b)
    #     print(a, "==>", c)
    #     print(b, "==>", c)
    else:
        hannuota(n-1, a, c, b)
        hannuota(1, a, b, c)
        hannuota(n-1, b, a, c)


 # 使用生成器打印斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        # 以上语法糖写法等价于以下3行代码
        # temp = a
        # a = b
        # b = temp + b
        n = n + 1
    return 'done'


# 生成器打印杨辉三角
def yanghui_triangles(max):
    line = 1
    self = []
    pre = []
    while line <= max:
        yield self
        self.clear()
        n = 1
        while n <= line:
            if n == 1 or n == line:
                temp = 1
            else:
                temp = pre[n-2]+pre[n-1]
            n = n+1
            self.append(temp)
        print(self)
        pre.clear()
        pre = self.copy()
        line = line + 1


fb = fib(10)

yh = yanghui_triangles(10)

for f in fb:
    print(f)

for t in yh:
    print(t)

hannuota(3,"A","B","C")






