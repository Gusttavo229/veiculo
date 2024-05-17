#calss carro 

###class Carro:
 #   def __init__(self, modelo, cor,ano):
  #      self.modelo = modelo
  #      self.cor = cor
   #     self.ano = ano
    #    self.velocidade = 0

    #def acelerar(self, velocidade):
     #   self.velocidade = velocidade
      #  self.velocidade = velocidade
       # print(f'O carro agora está a (self.velocidade) km/h.')

    #def frear(self, velocidade):
     #   if self.velocidade >= velocidade:
      #      self.velocidade -= velocidade 
       #     print(f'O carro agora está a (self.velocidade) km/h após frear.')  
class Veiculo:
    def __init__(self,cor,modelo):
        self.cor = cor
        self.modelo = modelo

class Carro(Veiculo):
    def cor(self):
        cor = 'vermelho'
        return cor
    
    def modelo(self):
        modelo = 'palio'
        return modelo

class Bicicleta(Veiculo):
    def cor(self):
        cor = 'Azul'
        return cor

    def modelo(self):
        modelo = 'Caloi'
        return modelo

carro = Carro()
print(carro.cor())




               
    
        