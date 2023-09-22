class Carga:
    def __init__(self, nome, energia):
        self.nome = nome
        self.energia = energia
        self.conectada = False

    def conectar(self):
        self.conectada = True

    def desconectar(self):
        self.conectada = False
