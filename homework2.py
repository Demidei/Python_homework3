# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

Run=True
SumMoney=0 # Можно хранить сумму в внешнем файле но пока так
Rich=[5000000, 0.1]
Removeprocent=[0.015,30,600]
Percentbonus=[0.03, 3]
Step=50
OperationCount=0 # Можно хранить сумму в внешнем файле но пока так

print(" Добро пожаловать \n", end="")
print(" Сейчас на счете ", SumMoney, "\n", end="")
print(" Если вы хотите пополнить счет введите 1, если вы хотите снять средства со счета, введите 2, если вы хотите выйти введите 3 ", end="")

option= int(input())


while Run==True:
    if option==1:
        print(" Введите сумму на которую хотите пополнить счет, обратите внимание, что можно пополнить счет только на сумму кратную ", Step, " если сумма пополнения не кратна ", Step, " будет зачислена только кратная часть введенной суммы ",  end="")
        # из формулировки не очевидно - отнимать налог на богатство от общей суммы или от суммы пополнения/снятия. Предположим, что от суммы пополнения/снятия, а не от общей суммы, а то мы быстро перестанем быть богатыми/ Технически разница только в том на каком этапе домножать
        temp=int(input())
        # допустим если введено число не кратное 50, то мы просто введем ближайшее кратное 50 число
        if SumMoney>Rich[0]:
            SumMoney=SumMoney+(temp-temp%Step)*(1-Rich[1])
        else:
            SumMoney=SumMoney+(temp-temp%Step)
        print(" Сейчас на счете ", SumMoney, "\n", end="")
        OperationCount+=1
        if OperationCount==Percentbonus[1]:
            SumMoney=SumMoney+SumMoney*Percentbonus[0]
            print( " Начислены проценты. Сейчас на счете  ", SumMoney, "\n", end="")
            OperationCount=0

        print(" Если вы хотите пополнить счет введите 1, если вы хотите снять средства со счета, введите 2, если вы хотите выйти введите 3 ", end="")
        option= int(input())
    elif option==2:
        # Для снятия есть вопрос - можно ли уйти в минус на счете, если снять всю сумму и дополнительно будет снят процент за снятие. Допустим, что у нас есть возможность иметь меньше 0 на счете, так как не сказано обратного. В противном слуае нужно просто будет учитывать процент при снятии
        print(" Введите сумму на которую хотите снять со счета, обратите внимание, что можно снять со счета только на сумму кратную ", Step, " если сумма снятия не кратна ", Step, " будет снята только кратная часть введенной суммы ",  end="")
        temp=int(input())
        if (temp-temp%Step)<=SumMoney:
            if SumMoney>Rich[0]:
                SumMoney=SumMoney-(temp-temp%Step)*(1+Rich[1])
            else:
                SumMoney=SumMoney-(temp-temp%Step)
            if Removeprocent[0]*(temp-temp%Step)<Removeprocent[1]:
                     SumMoney=SumMoney-Removeprocent[1]
            elif Removeprocent[0]*(temp-temp%Step)>Removeprocent[2]:
                     SumMoney=SumMoney-Removeprocent[2]
            else:
                     SumMoney=SumMoney-(Removeprocent[0]*(temp-temp%Step))
            print(" Средства сняты со счета. Сейчас на счете  ", SumMoney, "\n", end="")
            OperationCount+=1
            if OperationCount==Percentbonus[1]:
                SumMoney=SumMoney+SumMoney*Percentbonus[0]
                print(" Начислены проценты. Сейчас на счете  ", SumMoney, "\n", end="")
                OperationCount=0
        else:
             print(" Недостаточно средств на счете. Сейчас на счете  ", SumMoney, "\n", end="")
        print(" Если вы хотите пополнить счет введите 1, если вы хотите снять средства со счета, введите 2, если вы хотите выйти введите 3 ", end="")
        option= int(input())
    elif option==3:
         Run=False
         print(" Благодарим за то, что воспользовались нашим банкоматом!  ",end="")
    else:
         print(" Если вы хотите пополнить счет введите 1, если вы хотите снять средства со счета, введите 2, если вы хотите выйти введите 3 ", end="")
         option= int(input())


# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

print(" Введите целое число  ",end="")
N = int(input())
res=""
if N>9 and N<16:
    if N==10:
        res="A"+res
    elif N==11:
        res="B"+res
    elif N==12:
        res="C"+res
    elif N==13:
        res="D"+res
    elif N==14:
        res="E"+res
    else:
        res="F"+res
    res= res
else    :


    while (N//16)!=0:
       if N%16>9:
         if N%16==10:
              res="A"+res
         elif N%16==11:
                res="B"+res
         elif N%16==12:
               res="C"+res
         elif N%16==13:
               res="D"+res
         elif N%16==14:
               res="E"+res
         else:
                res="F"+res
       else:
         res= str(N%16)+res
       N=N//16
    res=str(N%16)+ res


print(res)

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


# пусть a b - целые числа. Не особенно важно, но допустим

def fractanalysis(S):
    res = []
    res.append(int(S[0:S.find("/")]))
    res.append(int(S[S.find("/")+1: len(S)]))
    return res


def fractconv(f):
    res = []
    for i in range(f[1]):
        if f[0] % (f[1]-i) == 0 and f[1] % (f[1]-i) == 0:
            res.append(int(f[0]/(f[1]-i)))
            res.append(int(f[1]/(f[1]-i)))
            break
    return res


def fractsum(f1, f2):
    res = []
    res.append(f1[0]*f2[1]+f2[0]*f1[1])
    res.append(f1[1]*f2[1])
    return fractconv(res)


def fractmult(f1, f2):
    res = []
    res.append(f1[0]*f2[0])
    res.append(f1[1]*f2[1])
    return fractconv(res)


print(" Введите дробь в формате a/b ", end="")
temp = input()
fract1 = fractanalysis(temp)
print(" Введите дробь в формате a/b ", end="")
temp = input()
fract2 = fractanalysis(temp)
temp = fractsum(fract1, fract2)
print(" Сумма дробей равна ", temp[0], "/", temp[1], "\n", end="")
temp = fractmult(fract1, fract2)
print(" Произведение дробей равно ", temp[0], "/", temp[1], "\n", end="")
