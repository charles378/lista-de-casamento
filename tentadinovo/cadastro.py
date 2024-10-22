# # import flet as ft
# # from databaze import Convidado

# # def main(page: ft.Page):
# #     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

# #     def cadastrar(page: ft.Page):
# #         def salvar(e):
# #             nome = nome_conv.value
# #             telefone = telefone_conv.value
# #             emaill = email.value
# #             senha = senha_conv.value  # Corrigido para obter o valor da senha

# #             # Instruções de depuração
# #             print(f"Nome: {nome}, Telefone: {telefone}, Email: {emaill}, Senha: {senha}")
# #             print(f"Tipos: {type(nome)}, {type(telefone)}, {type(emaill)}, {type(senha)}")

# #             try:
# #                 if nome and telefone and emaill:
# #                     Convidado.create(nome=nome, telefone=telefone, email=emaill, senha=senha)
# #                     info = ft.SnackBar(content=ft.Text("Salvo com sucesso!"), bgcolor=ft.colors.GREEN)
# #                     page.open(info)
# #                     return page.go('/convidado')
# #             except Exception as ex:
# #                 print(f"Erro: {ex}")
# #                 info = ft.SnackBar(content=ft.Text("e-mail existente!"), bgcolor=ft.colors.RED)
# #                 page.open(info)

# #         nome_conv = ft.TextField(label='Nome')
# #         telefone_conv = ft.TextField(label='Telefone')
# #         email = ft.TextField(label='E_mail')
# #         senha_conv = ft.TextField(label='criar senha')

# #         # Verifique se os controles não são None
# #         print(f"nome_conv: {nome_conv}, telefone_conv: {telefone_conv}, email: {email}, senha_conv: {senha_conv}")

# #         btn_botao = ft.Row(
# #             controls=[
# #                 ft.ElevatedButton('Salvar', on_click=salvar),
# #                 ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=lambda _: page.go('/'))
# #             ]
# #         )

# #         leate = ft.Container(
# #             content=ft.Column(
# #                 controls=[
# #                     ft.Text("Tela de Cadastro", theme_style="headlineMedium"),
# #                     nome_conv,
# #                     telefone_conv,
# #                     email,
# #                     senha_conv,
# #                     btn_botao,
# #                 ],
# #             ),
# #             width=700,
# #             padding=50
# #         )
# #         return leate

# #     def route_change(route):
# #         if route == '/convidado':
# #             return cadastrar(page)
# #         # Adicione outras rotas conforme necessário
# #         return ft.Text("Rota não encontrada")

# #     page.on_route_change = route_change

# # # Inicie o aplicativo Flet
# # ft.app(target=main)



# import flet as ft
# from databaze import Convidado,Casal
# def cadastrar(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     def salvar(e):
#         nome = nome_conv.value
#         telefone = telefone_conv.value
#         emaill = email.value
#         senha = senha_conv.value
#         try:
#             if nome and telefone and emaill:
#                 Convidado.create(nome=nome,telefone=telefone, email=emaill, senha=senha)
#                 info = ft.SnackBar(content=ft.Text("Salvo com sucesso!"), bgcolor=ft.colors.GREEN)
#                 page.open(info)
#                 return page.go('/convidado')
#         except:
#             info = ft.SnackBar(content=ft.Text("e-mail existente!"), bgcolor=ft.colors.RED)
#             page.open(info)

#     nome_conv = ft.TextField(label='Nome')
#     telefone_conv = ft.TextField(label='Telefone')
#     email = ft.TextField(label='E_mail',)
#     senha_conv = ft.TextField(label='criar senha')

#     btn_botao = ft.Row(
#         controls=[
#             ft.ElevatedButton('Salvar', on_click=salvar),
#             ft.TextButton(text='Canselar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=lambda _: page.go('/'))
#             ]
#         )

#     # leate = ft.Container(
#     #     content=ft.Column(
#     #         controls=[
#     #             ft.Text("Tela de Cadrasto", theme_style="headlineMedium"),
#     #             nome_conv,
#     #             telefone_conv,
#     #             email,
#     #             senha_conv,
#     #             btn_botao,
#     #         ],
#     #     ),
#     #     width=700,
#     #     padding=50
#     # )
#     return ft.Container(
#         content=ft.Column(
#             controls=[
#                 ft.Text("Tela de Cadrasto", theme_style="headlineMedium"),
#                 nome_conv,
#                 telefone_conv,
#                 email,
#                 senha_conv,
#                 btn_botao,
#             ],
#         ),
#         width=700,
#         padding=50
#     )
#     page.add(leate)


# ft.app(cadastrar)


# import flet as ft

# def main(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.SYSTEM

#     def toggle_color(e):
#         if page.bgcolor == ft.colors.BLACK:
#             page.bgcolor = ft.colors.WHITE
#         else:
#             page.bgcolor = ft.colors.BLACK
#         page.update()

#     #page.bgcolor = ft.colors.WHITE  # Cor inicial da página

#     toggle_button = ft.ElevatedButton(
#         text="Trocar Cor",
#         on_click=toggle_color
#     )

#     page.add(toggle_button)

# ft.app(target=main)


# import flet as ft

# # Função fictícia para buscar o nome do usuário no banco de dados
# def get_user_name():
#     # Simulação de busca no banco de dados
#     return "Paulo Almeida"

# def main(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.SYSTEM

#     user_name = get_user_name()
#     user_initials = "".join([name[0] for name in user_name.split()[:2]]).upper()

#     def toggle_color(e):
#         if page.bgcolor == ft.colors.BLACK:
#             page.bgcolor = ft.colors.WHITE
#         else:
#             page.bgcolor = ft.colors.BLACK
#         page.update()

#     def show_user_data(e):
#         # Função para buscar e mostrar os dados do usuário
#         user_data = get_user_name()  # Aqui você pode buscar mais dados do usuário
#         ft.dialog(title="Meu Dados", content=ft.Text(f"Nome: {user_data}")).show()

#     def logout(e):
#         # Função para sair
#         ft.dialog(title="Sair", content=ft.Text("Você saiu com sucesso!")).show()

#     app_bar = ft.AppBar(
#         title=ft.Text('Minha Aplicação'),
#         bgcolor=ft.colors.SURFACE_VARIANT,
#         toolbar_height=100,
#         color=ft.colors.AMBER,
#         leading=ft.Icon(ft.icons.HOME),
#         leading_width=100,
#         actions=[
#             ft.IconButton(icon=ft.icons.SUNNY, 
#                           selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
#                           selected=False,
#                           icon_color=ft.colors.WHITE, 
#                           on_click=toggle_color),
#             ft.CircleAvatar(content=ft.Text(user_initials)),
#             ft.PopupMenuButton(
#                 items=[
#                     ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
#                     ft.PopupMenuItem(text='Sair', on_click=logout),
#                 ]
#             )
#         ]
#     )

#     page.appbar = app_bar
#     page.bgcolor = ft.colors.WHITE  # Cor inicial da página
#     page.add(ft.Text("Conteúdo da página"))

# ft.app(target=main)

# import flet as ft

# # Função fictícia para buscar o nome do usuário no banco de dados
# def get_user_name():
#     # Simulação de busca no banco de dados
#     return "Paulo Almeida"

# def main(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.SYSTEM

#     user_name = get_user_name()
#     user_initials = "".join([name[0] for name in user_name.split()[:2]]).upper()

#     def toggle_color(e):
#         if page.bgcolor == ft.colors.BLACK:
#             page.bgcolor = ft.colors.WHITE
#         else:
#             page.bgcolor = ft.colors.BLACK
#         page.update()

#     def show_user_data(e):
#         # Função para buscar e mostrar os dados do usuário
#         user_data = get_user_name()  # Aqui você pode buscar mais dados do usuário
#         ft.dialog(title="Meu Dados", content=ft.Text(f"Nome: {user_data}")).show()

#     def logout(e):
#         # Função para sair
#         ft.dialog(title="Sair", content=ft.Text("Você saiu com sucesso!")).show()

#     app_bar = ft.AppBar(
#         title=ft.Text('Minha Aplicação'),
#         bgcolor=ft.colors.SURFACE_VARIANT,
#         toolbar_height=100,
#         color=ft.colors.AMBER,
#         leading=ft.Icon(ft.icons.HOME),
#         leading_width=100,
#         actions=[
#             ft.IconButton(icon=ft.icons.SUNNY, 
#                           selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
#                           selected=False,
#                           icon_color=ft.colors.WHITE, 
#                           on_click=toggle_color),
#             ft.CircleAvatar(content=ft.Text(user_initials)),
#             ft.PopupMenuButton(
#                 items=[
#                     ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
#                     ft.PopupMenuItem(text='Sair', on_click=logout),
#                 ]
#             )
#         ]
#     )

#     page.appbar = app_bar
#     page.bgcolor = ft.colors.WHITE  # Cor inicial da página
#     page.add(ft.Text("Conteúdo da página"))

# ft.app(target=main)


# import flet as ft

# # Função fictícia para buscar o nome do usuário no banco de dados
# def get_user_name():
#     # Simulação de busca no banco de dados
#     return "Paulo Almeida"

# def main(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.SYSTEM

#     user_name = get_user_name()
#     user_initials = "".join([name[0] for name in user_name.split()[:2]]).upper()

#     def toggle_color(e):
#         if page.bgcolor == ft.colors.BLACK:
#             page.bgcolor = ft.colors.WHITE
#         else:
#             page.bgcolor = ft.colors.BLACK
#         page.update()

#     def show_user_data(e):
#         # Função para buscar e mostrar os dados do usuário
#         user_data = get_user_name()  # Aqui você pode buscar mais dados do usuário
#         ft.dialog(title="Meu Dados", content=ft.Text(f"Nome: {user_data}")).show()

#     def logout(e):
#         # Função para sair e fechar a página
#         page.window.close()

#     app_bar = ft.AppBar(
#         title=ft.Text('Minha Aplicação'),
#         bgcolor=ft.colors.SURFACE_VARIANT,
#         toolbar_height=100,
#         color=ft.colors.AMBER,
#         leading=ft.Icon(ft.icons.HOME),
#         leading_width=100,
#         actions=[
#             ft.IconButton(icon=ft.icons.SUNNY, 
#                           selected_icon=ft.icons.WB_SUNNY_OUTLINED, 
#                           selected=False,
#                           icon_color=ft.colors.WHITE, 
#                           on_click=toggle_color),
#             ft.CircleAvatar(content=ft.Text(user_initials)),
#             ft.PopupMenuButton(
#                 items=[
#                     ft.PopupMenuItem(text='Meu dados', on_click=show_user_data),
#                     ft.PopupMenuItem(text='Sair', on_click=logout),
#                 ]
#             )
#         ]
#     )

#     page.appbar = app_bar
#     page.bgcolor = ft.colors.WHITE  # Cor inicial da página
#     page.add(ft.Text("Conteúdo da página"))

# # ft.app(target=main)
# import flet as ft
# from flet import FilePicker, FilePickerResultEvent

# def main(page: ft.Page):
#     def on_file_picked(e: FilePickerResultEvent):
#         if e.files:
#             avatar.foreground_image_src = e.files[0].path
#             print(e.files[0].path)

#             page.update()

#     file_picker = FilePicker(on_result=on_file_picked)
#     page.overlay.append(file_picker)

#     avatar = ft.CircleAvatar(
#         radius=300,
#         foreground_image_src=""
#     )

#     def pick_image(e):
#         file_picker.pick_files(allow_multiple=False)

#     page.add(
#         ft.Column(
#             [
#                 avatar,
#                 ft.ElevatedButton("Escolher Imagem", on_click=pick_image),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         )
#     )

# ft.app(target=main)

import flet as ft
from flet import FilePicker, FilePickerResultEvent

def main(page: ft.Page):
    def on_file_picked(e: FilePickerResultEvent):
        if e.files:
            avatar.foreground_image_src = e.files[0].path
            print(e.files[0].path)
            page.update()

    file_picker = FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    avatar = ft.CircleAvatar(
        radius=300,
        foreground_image_src=""
    )

    def pick_image(e):
        file_picker.pick_files(allow_multiple=False)

    page.add(
        ft.Column(
            [
                avatar,
                ft.ElevatedButton("Escolher Imagem", on_click=pick_image),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)

