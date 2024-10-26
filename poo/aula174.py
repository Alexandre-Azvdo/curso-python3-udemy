# Context Manager com classes
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quyando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exist__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with serão suprimidas.

# EX:
caminho_arquivo = 'C:\\Users\\PC\\Documents\\Cursos-TI\\Udemy\\curso-python3\\projetos\\venv\\aulas\\poo\\aula173.txt'
modo = 'w'
# with open(CAMINHO, modo) as arquivo:
#    ...

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo arquivo...')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo...')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)
    
        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        exception_.add_note('########### Minha nota #############')

        # return True # 'Tratei' a exceção



with MyOpen(caminho_arquivo, modo) as arquivo:
    arquivo.write( 'Linha 1\n')
    arquivo.write( 'Linha 2\n', 123)
    arquivo.write( 'Linha 3\n')
    print('WITH', arquivo)
