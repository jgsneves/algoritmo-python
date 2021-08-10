class CertidaoNascimento:
    def __init__(self, numero, data_registro, orgao_registro, nome_pai, nome_mae, nome):
        self.numero = numero
        self.data_registro = data_registro
        self.orgao_registro = orgao_registro
        self.nome_pai = nome_pai
        self.nome_mare = nome_mae
        self.nome = nome
    
class CertidaoCasamento:
    def __init__(self, numero, data_registro, orgao_registro, nome_solteiro, nome_casado, nome_conjuge):
        self.numero = numero
        self.data_registro = data_registro
        self.orgao_registro = orgao_registro
        self.nome_solteiro = nome_solteiro
        self.nome_casado = nome_casado
        self.nome_conjuge = nome_conjuge

class CPF:
    def __init__(self, numero, data_registro):
        self.numero = numero
        self.data_registro = data_registro
    
class RG:
    def __init__(self, numero, data_registro, orgao_cadastro):
        self.numero = numero
        self.data_registro = data_registro
        self.orgao_cadastro = orgao_cadastro
    
class Pessoa:
    def __init__(self, certidao_nascimento, cpf, rg):
        self.certidao_nascimento = certidao_nascimento
        self.cpf = cpf
        self.rg = rg
        self.certidao_casamento = None
        
    def casarPessoa(self, certidao_casamento_nova):
        if self.certidao_casamento == None:
            self.certidao_casamento = certidao_casamento_nova
        else:
            print('Não foi possível casar esta pessoa! Ela já é casada!')
        
    def retornarNomeDaPessoa(self):
        if self.certidao_casamento == None:
            return self.certidao_nascimento.nome
        else:
            return self.certidao_casamento.nome_casado
    
# as classes foram definidas acima. A partir daqui é um script

certidao_nascimento_joao = CertidaoNascimento(
    2302, 
    '09/08/2021', 
    'SSPBA', 
    'José', 
    'Maria', 
    'João Souza'
)

cpf_joao = CPF(312983189, '09/08/2021')
rg_joao = RG(321983, '09/08/2021', 'SSPBA')
    
joao = Pessoa(certidao_nascimento_joao, cpf_joao, rg_joao)

certidao_casamento_joao = CertidaoCasamento(
    39821731,
    '20/01/2030',
    'Cartório de Registro de Pessoas da Graça',
    'João Souza',
    'João Souza Silva',
    'Maria Silva'
)

joao.casarPessoa(certidao_casamento_joao)

seguno_casamento = CertidaoCasamento(
    3542542,
    '20/12/2030',
    'Cartório de Registro de Pessoas da Graça',
    'João Souza',
    'João Souza Figueredo',
    'Paula Figueredo'
)

joao.casarPessoa(seguno_casamento)

print(joao.retornarNomeDaPessoa())