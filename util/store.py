# import flet as ft


# def Store(page: ft.Page):
#     return ft.Container(
#         bgcolor='amber',
#         width=300,
#         alignment=ft.alignment.center,
#         content=ft.Column(controls=[
#             ft.Text('Store', size=30),
#             ft.ElevatedButton('voltar para home', on_click=lambda _: page.go('/'))
#             ]
#         )
#     )
from datetime import datetime
import time

# Data do casamento (ano, mês, dia, hora, minuto)
data_casamento = datetime(2024, 12, 31, 15, 0)

while True:
    # Data e hora atual
    data_atual = datetime.now()

    # Calcula a diferença entre as datas
    diferenca = data_casamento - data_atual

    # Extrai os dias e segundos da diferença
    dias_restantes = diferenca.days
    segundos_restantes = diferenca.seconds

    # Converte os segundos restantes em horas e minutos
    horas_restantes = segundos_restantes // 3600
    minutos_restantes = (segundos_restantes % 3600) // 60

    # Limpa a tela (funciona no terminal)
    print("\033c", end="")

    print(f"Faltam {dias_restantes} dias, {horas_restantes} horas e {minutos_restantes} minutos para o casamento!")

    # Espera 1 segundo antes de atualizar novamente
    time.sleep(1)
