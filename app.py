from flask import Flask, render_template, request, redirect, abort
from models import db, Paciente,PIA,Familiar

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pacientes.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pias.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///familiares.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createPaciente.html')

    if request.method == 'POST':
        nome = request.form['nome']
        dtNasc = request.form['dtNasc']
        nomeMae = request.form['nomeMae']
        nomePai = request.form['nomePai']
        dataIngresso = request.form['dataIngresso']
        servicoOrigem = request.form['servicoOrigem']
        recebeBeneficio = request.form['recebeBeneficio']
        cep= request.form['cep']
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']
        pacientes = Paciente(

        nome=nome,
        dtNasc = dtNasc,
        nomeMae = nomeMae,
        nomePai = nomePai,
        dataIngresso = dataIngresso,
        servicoOrigem = servicoOrigem,
        recebeBeneficio = recebeBeneficio,
        cep = cep,
        rua =rua,
        numero =numero,
        complemento =complemento
        )
        db.session.add(pacientes)
        db.session.commit()
        return redirect('/')

@app.route('/')
def RetrieveList():
    pacientes = Paciente.query.all()
    return render_template('listPacientes.html',pacientes = pacientes)


@app.route('/<int:id>')
def RetrieveStudent(id):
    pacientes = Paciente.query.filter_by(id=id).first()
    if pacientes:
        return render_template('infoPaciente.html', pacientes = pacientes)
    return f"Employee with id ={id} Doenst exist"



@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    pacientes = Paciente.query.filter_by(id=id).first()

    if request.method == 'POST':
        if pacientes:
            db.session.delete(pacientes)
            db.session.commit()

        nome = request.form['nome']
        dtNasc = request.form['dtNasc']
        nomeMae = request.form['nomeMae']
        nomePai = request.form['nomePai']
        dataIngresso = request.form['dataIngresso']
        servicoOrigem = request.form['servicoOrigem']
        recebeBeneficio = request.form['recebeBeneficio']
        cep = request.form['cep']
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']
        pacientes = Paciente(

            nome=nome,
            dtNasc=dtNasc,
            nomeMae=nomeMae,
            nomePai=nomePai,
            dataIngresso=dataIngresso,
            servicoOrigem=servicoOrigem,
            recebeBeneficio=recebeBeneficio,
            cep=cep,
            rua=rua,
            numero=numero,
            complemento=complemento
        )
        db.session.add(pacientes)
        db.session.commit()
        return redirect('/')
        return f"Student with id = {id} Does nit exist"

    return render_template('atualizarPaciente.html', pacientes=pacientes)

@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    pacientes = Paciente.query.filter_by(id=id).first()
    if request.method == 'POST':
        if pacientes:
            db.session.delete(pacientes)
            db.session.commit()
            return redirect('/')
        abort(404)
     #return redirect('/')
    return render_template('deletePaciente.html')

####### PIAS   ######

@app.route('/createPIA', methods=['GET', 'POST'])
def createPIA():
    if request.method == 'GET':
        return render_template('createPIA.html')

    if request.method == 'POST':
        id_paciente = request.form['id_paciente']
        serviço_indicado = request.form['serviço_indicado']
        orgao_responsavel = request.form['orgao_responsavel']
        competencia_territorial = request.form['competencia_territorial']
        responsavel_informaçoes = request.form['responsavel_informaçoes']
        acao_encaminhamento = request.form['acao_encaminhamento']
        equipe_responsavel = request.form['equipe_responsavel']
        funcao= request.form['funcao']
        nome_serviço = request.form['nome_serviço']
        email = request.form['email']
        telefone = request.form['telefone']
        endereço = request.form['endereço']
        pias = PIA(
        id_paciente=id_paciente,
        serviço_indicado = serviço_indicado,
        orgao_responsavel = orgao_responsavel,
        competencia_territorial = competencia_territorial,
        responsavel_informaçoes = responsavel_informaçoes,
        acao_encaminhamento = acao_encaminhamento,
        equipe_responsavel = equipe_responsavel,
        funcao = funcao,
        nome_serviço =nome_serviço,
        email =email,
        telefone =telefone,
        endereço =endereço

        )
        db.session.add(pias)
        db.session.commit()
        return redirect('/listPia')


@app.route('/listPia')
def RetrieveListPia():
    pias = PIA.query.all()
    return render_template('listPIA.html',pias = pias)

@app.route('/pia/<int:id>')
def RetrievePia(id):
    pias = PIA.query.filter_by(id=id).first()
    if pias:
        return render_template('infoPia.html', pias = pias)
    return f" ={id} Doenst exist"




@app.route('/<int:id>/pia/edit', methods=['GET', 'POST'])
def updatePia(id):
    pias = PIA.query.filter_by(id=id).first()

    if request.method == 'POST':
        if pias:
            db.session.delete(pias)
            db.session.commit()

        id_paciente = request.form['id_paciente']
        serviço_indicado = request.form['serviço_indicado']
        orgao_responsavel = request.form['orgao_responsavel']
        competencia_territorial = request.form['competencia_territorial']
        responsavel_informaçoes = request.form['responsavel_informaçoes']
        acao_encaminhamento = request.form['acao_encaminhamento']
        equipe_responsavel = request.form['equipe_responsavel']
        funcao = request.form['funcao']
        nome_serviço = request.form['nome_serviço']
        email = request.form['email']
        telefone = request.form['telefone']
        endereço = request.form['endereço']
        pias = PIA(
            id_paciente=id_paciente,
            serviço_indicado=serviço_indicado,
            orgao_responsavel=orgao_responsavel,
            competencia_territorial=competencia_territorial,
            responsavel_informaçoes=responsavel_informaçoes,
            acao_encaminhamento=acao_encaminhamento,
            equipe_responsavel=equipe_responsavel,
            funcao=funcao,
            nome_serviço=nome_serviço,
            email=email,
            telefone=telefone,
            endereço=endereço

        )
        db.session.add(pias)
        db.session.commit()
        return redirect('/listPia')
        return f"S = {id} Does nit exist"

    return render_template('atualizarPia.html', pias=pias)


@app.route('/<int:id>/pia/delete', methods=['GET','POST'])
def deletePia(id):
    pias = PIA.query.filter_by(id=id).first()
    if request.method == 'POST':
        if pias:
            db.session.delete(pias)
            db.session.commit()
            return redirect('/listPia')
        abort(404)
     #return redirect('/')
    return render_template('deletePIA.html')


########################FAMILIARES############################

@app.route('/createFamiliar', methods=['GET', 'POST'])
def createFamiliar():
    if request.method == 'GET':
        return render_template('createFamiliar.html')

    if request.method == 'POST':
        id_paciente = request.form['id_paciente']
        nome = request.form['nome']
        dtNasc = request.form['dtNasc']
        parentesco = request.form['parentesco']
        telefone = request.form['telefone']
        celular = request.form['celular']
        responsavel_legal = request.form['responsavel_legal']
        nacionalidade = request.form['nacionalidade']
        naturalidade = request.form['naturalidade']
        cpf = request.form['cpf']
        rg = request.form['rg']
        ocupaçao = request.form['ocupaçao']
        serviço_frequentado = request.form['serviço_frequentado']
        demanda = request.form['demanda']
        cep = request.form['cep']
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']


        familiares = Familiar(

        id_paciente=id_paciente,
      nome = nome,
      dtNasc = dtNasc,
       parentesco = parentesco,
       telefone = telefone,
        celular = celular,
      responsavel_legal = responsavel_legal,
       nacionalidade = nacionalidade,
       naturalidade = naturalidade,
       cpf = cpf,
        rg = rg,
        ocupaçao = ocupaçao,
        serviço_frequentado = serviço_frequentado,
        demanda = demanda,
        cep = cep,
     rua = rua,
      numero = numero,
     complemento = complemento,

        )
        db.session.add(familiares)
        db.session.commit()
        return redirect('/')



@app.route('/listFamiliares')
def RetrieveListFamiliares():
    familiares = Familiar.query.all()
    return render_template('listFamiliares.html',familiares= familiares)

@app.route('/familiar/<int:id>')
def RetrieveFamiliar(id):
    familiares = Familiar.query.filter_by(id=id).first()
    if familiares:
        return render_template('infoFamiliar.html', familiares = familiares)
    return f" ={id} Doenst exist"

@app.route('/<int:id>/familiar/edit', methods=['GET', 'POST'])
def updateFamiliar(id):
    familiares = Familiar.query.filter_by(id=id).first()

    if request.method == 'POST':
        if familiares:
            db.session.delete(familiares)
            db.session.commit()

        id_paciente = request.form['id_paciente']
        nome = request.form['nome']
        dtNasc = request.form['dtNasc']
        parentesco = request.form['parentesco']
        telefone = request.form['telefone']
        celular = request.form['celular']
        responsavel_legal = request.form['responsavel_legal']
        nacionalidade = request.form['nacionalidade']
        naturalidade = request.form['naturalidade']
        cpf = request.form['cpf']
        rg = request.form['rg']
        ocupaçao = request.form['ocupaçao']
        serviço_frequentado = request.form['serviço_frequentado']
        demanda = request.form['demanda']
        cep = request.form['cep']
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']

        familiares = Familiar(
            id_paciente=id_paciente,
            nome=nome,
            dtNasc=dtNasc,
            parentesco=parentesco,
            telefone=telefone,
            celular=celular,
            responsavel_legal=responsavel_legal,
            nacionalidade=nacionalidade,
            naturalidade=naturalidade,
            cpf=cpf,
            rg=rg,
            ocupaçao=ocupaçao,
            serviço_frequentado=serviço_frequentado,
            demanda=demanda,
            cep=cep,
            rua=rua,
            numero=numero,
            complemento=complemento,

        )
        db.session.add(familiares)
        db.session.commit()
        return redirect('/listFamiliares')
        return f"S = {id} Does nit exist"

    return render_template('atualizarFamiliar.html', familiares=familiares)




@app.route('/<int:id>/familiar/delete', methods=['GET','POST'])
def deleteFamiliar(id):
    familiares = Familiar.query.filter_by(id=id).first()
    if request.method == 'POST':
        if familiares:
            db.session.delete(familiares)
            db.session.commit()
            return redirect('/listFamiliares')
        abort(404)
     #return redirect('/')
    return render_template('deleteFamiliar.html')
app.run(host='localhost', port=5000)