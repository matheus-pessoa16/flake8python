from FilaNormal import FilaNormal


class TestFilaNormal:

    def test_when_call_gerasenhaatual_should_display_senhaatual(self):

        desired = 'NM0'

        filateste = FilaNormal()
        filateste.gera_senha_atual()

        assert filateste.senha_atual == desired

    def test_when_resetfila_and_codigo_lt_100_should_return_next(self):

        desired = 1

        filateste = FilaNormal()
        filateste.reset_fila()

        assert filateste.codigo == desired

    def test_when_resetfila_and_codigo_gt_100_should_return_0(self):
        desired = 0

        filateste = FilaNormal()
        filateste.codigo = 101
        filateste.reset_fila()

        assert filateste.codigo == desired

    def test_when_atualizafila_fila_should_return_senha_atual(self):
        desired = 'NM1'

        filateste = FilaNormal()
        filateste.atualiza_fila()

        assert filateste.fila.pop(0) == desired

    def test_when_chamacliente_should_return_message_and_senha(self):

        desired = 'Cliente atual: NM1, dirija-se ao caixa 1'

        filateste = FilaNormal()
        filateste.atualiza_fila()
        result = filateste.chama_cliente(1)

        assert result == desired
