from FactoryFila import FactoryFila

filateste = FactoryFila().pega_fila('prioritaria')
filateste.atualiza_fila()
filateste.atualiza_fila()
print(filateste.chama_cliente(1))
print(filateste.chama_cliente(2))
