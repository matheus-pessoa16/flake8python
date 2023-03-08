import abc
from typing import List

from constants import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ''

    def reset_fila(self) -> None:
        if self.codigo > TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self) -> None:
        self.reset_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...

    def insere_cliente(self) -> None:
        self.fila.append(self.senha_atual)
