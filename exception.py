#try: código para ficar de olho se vai dar problema
#except: se deu problema
#else: se deu tudo certo
#finally:


from typing import final


try:
    letras = ["a", "b", "c"]
    print(letras[3])
except IndexError:
    print("Esse elemento não existe na lista")


try:
    valor = int(input("Digite o valor desejado "))
    print(valor)
except ValueError:
    print("Por favor digite somente números")
else:
    print("Usuario digitou corretamente")
    resultado = valor + 2
    print(valor,"+ 2 =", resultado)
finally:
    print("Finalizou")