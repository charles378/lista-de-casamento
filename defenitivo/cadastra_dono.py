import flet as ft
from databaze import Casal

def cadastrar_dono(page: ft.Page):
    def salvar_dono(e):
        # Verificar se já existe um dono cadastrado
        if Casal.select().count() > 0:
            p = Casal.select()
            for f in p:
                print(f.id,f.nome, f.email, f.senha)
            info = ft.SnackBar(content=ft.Text("VOCÉ NÃO PODE SE CADASTRAR AQUI!"), bgcolor=ft.colors.RED)
            page.open(info)
            return

        nome = nome_dono.value
        emaill = email.value
        senha = senha_dono.value
        try:    
            if nome and senha and email:
                Casal.create(nome=nome, email=emaill, senha=senha)
                nome_dono.value = ""
                email.value = ""
                senha_dono.value = ""
                info = ft.SnackBar(content=ft.Text("Dono cadastrado com sucesso!"), bgcolor=ft.colors.GREEN)
                page.open(info)
                page.go('/casal')
            else:
                info = ft.SnackBar(content=ft.Text("Por favor, preencha todos os campos!"), bgcolor=ft.colors.RED)
                page.open(info)

        except Exception as ex:
            print(f"Erro: {ex}")
            info = ft.SnackBar(content=ft.Text("e-mail existente!"), bgcolor=ft.colors.RED)
            page.open(info)

    nome_dono = ft.TextField(label='Nome')
    senha_dono = ft.TextField(label='Senha', password=True)
    email = ft.TextField(label='E_mail')
    salvar_button = ft.ElevatedButton(text="Salvar", on_click=salvar_dono)
    cancelar_button = ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=lambda _: page.go('/'))

    return(ft.Column(
        controls=[
            ft.Text("Cadastro do Dono", size=30, color=ft.colors.AMBER),
            nome_dono,
            email,
            senha_dono,
            ft.Row([salvar_button, cancelar_button], alignment=ft.MainAxisAlignment.END)
        ],
        width=400,
        alignment=ft.MainAxisAlignment.CENTER
    ))

# Certifique-se de que o método cadastrar_dono seja chamado corretamente em seu aplicativo Flet
#ft.app(target=cadastrar_dono)
