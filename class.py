#classes e métodos

# método de classe sem sentido
class DidaticaTech: #boas práticas = iniciar palavras da classe com letra maiuscula
      def incrementa(self, v, i): #deve colocar self quando se estiver fazendo uma função dentro de uma classe
          valor = v
          incremento = i
          resultado = valor - incremento
          return resultado


a = DidaticaTech()
b = a.incrementa(10,1) 
print(b) #9
#print(a.valor) # ERRRO

############
#método de classe + correto

class DidaticaTech2: 
      def incrementa2(self, v, i): # self vira o objeto a 
          self.valor = v # self vira a.valor 
          self.incremento = i #self vira a.incremento
          self.resultado = self.valor - self.incremento
          return self.resultado
 

a = DidaticaTech2() #instanciei a classe DidaticaTech2 ao objeto a, ou seja, apartir disso dizemos que o self é o próprio objeto a
b = a.incrementa2(8,1) 
print(b) #7
print(a.valor) #8



####
class calculadora1:
    def soma(self, val1, val2):
        return val1 + val2

    def subtrai(self, val1, val2):
        return val1 - val2

    def multiplicacao(self, val1, val2):
        return val1 * val2

    def divisao(self, val1, val2):
        return val1 / val2

calc = calculadora1()
print(calc.soma(4,5))
print(calc.soma(10, 7))

print(calc.multiplicacao(4,6))
print(calc.multiplicacao(4,8))