from typing import Union

from FilaNormal import FilaNormal
from FilaPrioritaria import FilaPrioritaria
from constants import FILA_NORMAL, FILA_PRIORITARIA


class FactoryFila:

    def pega_fila(self, tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Fila não existe')
