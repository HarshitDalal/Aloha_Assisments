def fun():
    var = "Harry"  # Local Scope
    print(f'local var : {var}')


fun()
# Getting error
# print(var)


var1 = "Tom"


def fun1():
    var1 = "Jarry"
    print(f'Local Var1 : {var1}')


fun1()
print(f'Global Var1 : {var1}')


def fun2():
    global var2
    var2 = 'Tom'
    print(f'local var from fun2 : {var2}')


fun2()
print(f'Extract var from fun2 : {var2}')

var3 = "Tom"


def fun3():
    global var3
    var3 = 'Jarry'
    print(f'Local var : {var3}')


fun3()
print(f'Global var : {var3}')

