from FilaPrioritaria import FilaPrioritaria


class TestFilaPrioritaria:

    def test_when_call_gerasenhaatual_should_display_senhaatual(self):

        desired = 'PR0'

        filateste = FilaPrioritaria()
        filateste.gera_senha_atual()

        assert filateste.senha_atual == desired

    def test_when_resetfila_and_codigo_lt_100_should_return_next(self):

        desired = 1

        filateste = FilaPrioritaria()
        filateste.reset_fila()

        assert filateste.codigo == desired

    def test_when_resetfila_and_codigo_gt_100_should_return_0(self):
        desired = 0

        filateste = FilaPrioritaria()
        filateste.codigo = 101
        filateste.reset_fila()

        assert filateste.codigo == desired

    def test_when_atualizafila_fila_should_return_senha_atual(self):
        desired = 'PR1'

        filateste = FilaPrioritaria()
        filateste.atualiza_fila()

        assert filateste.fila.pop(0) == desired

    def test_when_chamacliente_should_return_message_and_senha(self):

        desired = 'Cliente atual: PR1, dirija-se ao caixa 1'

        filateste = FilaPrioritaria()
        filateste.atualiza_fila()
        result = filateste.chama_cliente(1)

        assert result == desired

    def test_when_estatistica_default_should_return_simple_dict(self):
        desired = {'1-06/03/2023': 2}

        filateste = FilaPrioritaria()
        filateste.atualiza_fila()
        filateste.chama_cliente(1)

        result = filateste.estatistica(
            dia='06/03/2023', agencia=1, flag='default')

        assert result == desired

    def test_when_estatistica_detail_should_return_dict(self):
        desired = {}

        desired['dia'] = '06/03/2023'
        desired['agencia'] = 1
        desired['clientes_atendidos'] = ['PR1', 'PR1', 'PR1']
        desired['quatidade_clientes_atendidos'] = 3

        filateste = FilaPrioritaria()
        filateste.atualiza_fila()
        filateste.chama_cliente(1)

        result = filateste.estatistica(
            dia='06/03/2023', agencia=1, flag='detail')

        assert result == desired
