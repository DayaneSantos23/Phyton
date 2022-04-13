# É como o conjunto da matemática (união, intercessão, etc)
#Um set não pode conter um elemento duplicado desse elemento


s = {"ad", "ab", "ac"}
u = {"A", "B", "C", "D"}
t = {"C", "D", "E"}

novo = s.union(t) #união
print(novo) #{'E', 'ab', 'C', 'ac', 'ad', 'D'}

novo2 = u - t # diferença: o que é comum somente ao u (só tem no u)
print(novo2) #{'A', 'B'}

novo3 = u & t # intercessão: o que é comum aos dois
print(novo3) #{'D', 'C'}


novo4 = u ^ t # O que não é comum aos dois
print(novo4) 

for i in u: #interação: para cada elemnto que você tem em u ele guarda em i e imprime o i 
    print(i)


##### Estudo de caso
func = {"Fernando", "Robert", "Jacob", "luana", "Dayane", "Maycon", "Maria", "Henrique"}
FuncNoite = {"Fernando", "Robert", "Jacob"}
FuncDia = { "Dayane", "Maycon", "Maria", "Henrique"}
FuncCarro = {"Jacob", "luana", "Dayane", "Maycon"}

func_CarroNoite = FuncCarro & FuncNoite
print("Funcionários que tem carro e trabalham a noite:")
for i in func_CarroNoite: 
    print(i)

func_CarroDia = FuncCarro & FuncDia
print("\n""Funcionários que tem carro e trabalham de dia:")
for u in func_CarroDia: 
    print(u)

func_SemCarro = func - FuncCarro
print("\n""Funcionários que não tem carro")

for x in func_SemCarro: 
    print(x)


#### Outra maneira

func = ["Fernando", "Robert", "Jacob", "luana", "Dayane", "Maycon", "Maria", "Henrique"]
FuncNoite = ["Fernando", "Robert", "Jacob"]
FuncDia = ["Dayane", "Maycon", "Maria", "Henrique"]
FuncCarro = ["Jacob", "luana", "Dayane", "Maycon"]

fun_ = set(func)
Fun_noite = set(FuncNoite)
Func_dia = set(FuncDia)
Func_carro = set(FuncCarro)


funcCarroNoite = Func_carro & Fun_noite
print("Funcionários que tem carro e trabalham a noite:", funcCarroNoite)

funcCarroDia = Func_carro & Func_dia
print("\n""Funcionários que tem carro e trabalham de dia:", funcCarroDia)

funcSemCarro = fun_ - Func_carro
print("\n""Funcionários que não tem carro:", funcSemCarro)





