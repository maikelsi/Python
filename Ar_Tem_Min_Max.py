class ControleArCondicionado:
    def __init__(self, cor, largura, altura, peso, marca, modelo, tipo_de_pilha):
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.peso = peso
        self.marca = marca
        self.modelo = modelo
        self.tipo_de_pilha = tipo_de_pilha
        self.ligado = False
        self.temperatura = 20  # Inicialmente a temperatura é 20 graus

    def liga_desliga(self):
        self.ligado = not self.ligado
        
        if self.ligado:
            self.temperatura = 20  # Define a temperatura para 20 graus ao ligar
            return "Ar condicionado ligado. Temperatura definida para 20 graus."
        else:
            return "Ar condicionado desligado"

    def aumenta_temperatura(self):
        if self.ligado:
            if self.temperatura < 30:
                self.temperatura += 1
                print(f"Temperatura aumentada para {self.temperatura} graus")
            else:
                print("Temperatura já está no máximo de 30 graus")
        else:
            print("Ar condicionado desligado")

    def diminui_temperatura(self):
        if self.ligado:
            if self.temperatura > 16:
                self.temperatura -= 1
                print(f"Temperatura diminuída para {self.temperatura} graus")
            else:
                print("Temperatura já está no mínimo de 16 graus")
        else:
            print("Ar condicionado desligado")

# Estanciando a classe do Objeto
controle = ControleArCondicionado("branco", 20, 20, 10, "LG", "ABC", "AAA")

# Executando uma das funções dele
print(controle.liga_desliga())

# Criando uma rotina de repetição com entrada do usuário
print("Digite 1 para Ligar ou Desligar o Ar Condicionado")
print("Digite 2 para aumentar a temperatura")
print("Digite 3 para diminuir a temperatura")
print("Digite 'sair' para encerrar o programa")

while True:
    comando = input().strip().lower()
    
    if comando == "sair":
        break
    if comando == "1":
        print(controle.liga_desliga())
    elif comando == "2":
        controle.aumenta_temperatura()
    elif comando == "3":
        controle.diminui_temperatura()
    else:
        print("Comando inválido")