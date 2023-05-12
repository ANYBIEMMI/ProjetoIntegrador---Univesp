from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PIA(db.Model):
    __tablename__ = "pias"

    id = db.Column('id', db.Integer, primary_key=True,)
    id_paciente = db.Column(db.String(150))
    serviço_indicado = db.Column(db.String(150))
    orgao_responsavel = db.Column(db.String(150))
    competencia_territorial = db.Column(db.String(150))
    responsavel_informaçoes = db.Column(db.String(150))
    acao_encaminhamento = db.Column(db.String(150))
    equipe_responsavel = db.Column(db.String(150))
    funcao = db.Column(db.String(150))
    nome_serviço = db.Column(db.String(150))
    email = db.Column(db.String(150))
    telefone = db.Column(db.String(150))
    endereço = db.Column(db.String(150))

    def __init__(self, id_paciente, serviço_indicado, orgao_responsavel, competencia_territorial,
                 responsavel_informaçoes, acao_encaminhamento, equipe_responsavel, funcao, nome_serviço, email,
                 telefone, endereço):
        self.id_paciente = id_paciente
        self.serviço_indicado = serviço_indicado
        self.orgao_responsavel = orgao_responsavel
        self.competencia_territorial = competencia_territorial
        self.responsavel_informaçoes = responsavel_informaçoes
        self.acao_encaminhamento = acao_encaminhamento
        self.equipe_responsavel = equipe_responsavel
        self.funcao = funcao
        self.nome_serviço = nome_serviço
        self.email = email
        self.telefone = telefone
        self.endereço = endereço



class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    dtNasc = db.Column(db.String(150))
    nomeMae = db.Column(db.String(150))
    nomePai = db.Column(db.String(150))
    dataIngresso = db.Column(db.String(150))
    servicoOrigem = db.Column(db.String(150))
    recebeBeneficio = db.Column(db.String(150))
    cep = db.Column(db.String(150))
    rua = db.Column(db.String(150))
    numero = db.Column(db.String(150))
    complemento = db.Column(db.String(150))

    def __init__(self, nome, dtNasc, nomeMae, nomePai, dataIngresso, servicoOrigem, recebeBeneficio, cep, rua,
                 numero, complemento):

        self.nome = nome
        self.dtNasc = dtNasc
        self.nomeMae = nomeMae
        self.nomePai = nomePai
        self.dataIngresso = dataIngresso
        self.servicoOrigem = servicoOrigem
        self.recebeBeneficio = recebeBeneficio
        self.cep = cep
        self.rua = numero
        self.complemento = complemento

    def __repr__(self):
        return "hello"

