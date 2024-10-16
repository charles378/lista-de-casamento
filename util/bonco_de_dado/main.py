from database import db, Usuario, Anuncio

db.connect()  # para fazer a chamada da ação

db.create_tables([Usuario, Anuncio])  # para criar a tablela caso ela nao exista e criar uma lista [Usuario, Anuncio]

# adicionar valores na tablela
usuari = Usuario.create(nome="programadorPython", email="teste@teste.com", senha="123456")
print('Novo usuari:', usuari.id, usuari.nome, usuari.email)

# adicionar valores na tablela
Usuario.create(nome="Guilherme", email="gui@teste.com", senha="123456")
Usuario.create(nome="joao", email="joao@teste.com", senha="123456")
Usuario.create(nome="maria", email="maria@teste.com", senha="123456")

# para listar a tablela
lista_usuario = Usuario.select()
print('listando usuari:')
for u in lista_usuario:
     print('-', u.id, u.nome, u.email)

# # busca pelo ID do usuari
# usuario1 = Usuario.get(Usuario.id == 1)
# print(f'usuari pelo ID-{usuario1.id} nome {usuario1.nome}')

# # busca pelo email do usuari
# usuari = Usuario.get(Usuario.email == "joao@teste.com")
# print(f'usuario pelo ID-{usuari.id} nome {usuari.nome} emeil {usuari.email}')

# # modificar os dados da tabela pelo email
# maria = Usuario.get(Usuario.email == "maria@teste.com")
# maria.nome = 'Maria python'
# maria.save()  # o comando save() e pra salva a auteracao que nos fizemos
# print('maria atualizada: ', maria.nome)

# # testando se ta salvando so um email
# print('\033[32mTentando criar um usuario com e_mail duplicado\033[m')
# try:
#     usuario_duplicado = Usuario.create(nome='Duplicado', email="teste@teste.com", senha='123456')
# except:
#     print('e-mail existente!')

# # deletando um usuario pelo e-mail
# usuario_deletado = Usuario.get(Usuario.email == "teste@teste.com")
# usuario_deletado.delete_instance()

# try:
#     Usuario.get(Usuario.email == "teste@teste.com") # buscado se o usuario foi apagado da lista
# except:
#     print('Usuario deletado')

# # usando chave estrajeira do anuncio
# maria = Usuario.get(Usuario.email == "maria@teste.com")
# anuncio = Anuncio.create(
#     usuario=maria,
#     titulo='video de banco de dado',
#     descricao='O projeto secria criar um video sobre banco de dado e ORM com python',
#     valor=500.0)
# print('novo anuncio:', anuncio.id, anuncio.titulo)

# Anuncio.create(usuario=maria,titulo='anuncio 1',descricao='deixa o like',valor=1500.0)
# Anuncio.create(usuario=maria,titulo='anuncio 2',descricao='fasa um comentario',valor=5500.0)
# Anuncio.create(usuario=maria,titulo='anuncio 3',descricao='se increva',valor=100.0)

# # listando o anuncio pelo usuario
# print('anuncios da maria')
# anuncio_maria = Anuncio.select().join(Usuario).where(Usuario.email == "maria@teste.com")
# for a in anuncio_maria:
#     print('-', a.id, a.titulo, a.valor)

# # deletar todos os anuncio
# Anuncio.delete().execute()

# print('quantidade de anuncio', Anuncio.select().count())