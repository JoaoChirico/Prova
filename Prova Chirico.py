#Construa um software em Python que implemente uma Pilha de carros e uma Pilha de drones.
#As classes carro e drone herdam da classe veículo os atributos e comuns às duas classes.
#A classe carro é composta dos atributos marca, modelo e portas. O atributo portas é fortemente privado.
#A classe drone é composta dos atributos marca, modelo e quantidade de hélices. O atributo quantidade de hélices é fracamente privado.
#Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.
#Implemente uma tela com um menu (funcionando) que permita ao usuário:
#-> Adicionar e remover carros da Pilha.
#-> Adicionar e remover drones da Pilha.
#-> Imprimir a Pilha de carros e a Pilha de drones.
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprimir_informacoes(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas  # atributo fortemente privado

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Portas:", self.__portas)


class Drone(Veiculo):
    def __init__(self, marca, modelo, quantidade_helices):
        super().__init__(marca, modelo)
        self._quantidade_helices = quantidade_helices  # atributo fracamente privado

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Quantidade de Hélices:", self._quantidade_helices)


class Pilha:
    def __init__(self):
        self.__pilha = []

    def adicionar(self, item):
        self.__pilha.append(item)

    def remover(self):
        if not self.vazia():
            return self.__pilha.pop()
        else:
            return None

    def vazia(self):
        return len(self.__pilha) == 0

    def imprimir_pilha(self):
        for item in self.__pilha:
            item.imprimir_informacoes()


def exibir_menu():
    print("Menu:")
    print("1. Adicionar Carro")
    print("2. Remover Carro")
    print("3. Adicionar Drone")
    print("4. Remover Drone")
    print("5. Imprimir Pilha de Carros")
    print("6. Imprimir Pilha de Drones")
    print("0. Sair")


pilha_carros = Pilha()
pilha_drones = Pilha()

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        portas = int(input("Digite o número de portas do carro: "))
        carro = Carro(marca, modelo, portas)
        pilha_carros.adicionar(carro)
        print("Carro adicionado com sucesso!")

    elif opcao == "2":
        carro_removido = pilha_carros.remover()
        if carro_removido:
            print("Carro removido:")
            carro_removido.imprimir_informacoes()
        else:
            print("A pilha de carros está vazia.")

    elif opcao == "3":
        marca = input("Digite a marca do drone: ")
        modelo = input("Digite o modelo do drone: ")
        helices = int(input("Digite o número de hélices do drone: "))
        drone = Drone(marca, modelo, helices)
        pilha_drones.adicionar(drone)
        print("Drone adicionado com sucesso!")

    elif opcao == "4":
        drone_removido = pilha_drones.remover()
        if drone_removido:
            print("Drone removido:")
            drone_removido.imprimir_informacoes()
        else:
            print("A pilha de drones está vazia.")

    elif opcao == "5":
        print("Pilha de Carros:")
        pilha_carros.imprimir_pilha()

    elif opcao == "6":
        print("Pilha de Drones")
        pilha_drones.imprimir_pilha()

    elif opcao =="0":
        print("Encerrando Sessão")
        break







