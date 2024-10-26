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
# from datetime import datetime
# import time

# # Data do casamento (ano, mês, dia, hora, minuto)
# data_casamento = datetime(2024, 12, 31, 15, 0)

# while True:
#     # Data e hora atual
#     data_atual = datetime.now()

#     # Calcula a diferença entre as datas
#     diferenca = data_casamento - data_atual

#     # Extrai os dias e segundos da diferença
#     dias_restantes = diferenca.days
#     segundos_restantes = diferenca.seconds

#     # Converte os segundos restantes em horas e minutos
#     horas_restantes = segundos_restantes // 3600
#     minutos_restantes = (segundos_restantes % 3600) // 60

#     # Limpa a tela (funciona no terminal)
#     print("\033c", end="")

#     print(f"Faltam {dias_restantes} dias, {horas_restantes} horas e {minutos_restantes} minutos para o casamento!")

#     # Espera 1 segundo antes de atualizar novamente
#     time.sleep(1)
import datetime
import flet as ft


def main(page : ft.Page):
    tp = ft.TimePicker(
        cancel_text='Canselar',
        confirm_text='Confimarcao',
        error_invalid_text=' Hora invalida',
        hour_label_text='Hora',
        minute_label_text='Minuto',
        help_text='Selecione a hora',
        time_picker_entry_mode=ft.TimePickerEntryMode.INPUT_ONLY,
        value=datetime.time(10, 11, 18),
    )
    dp = ft.DatePicker(
        cancel_text='Canselar',
        confirm_text='Confimarcao',
        field_hint_text='MM/DD/YYYY',
        field_label_text='igite uma data',
        help_text='Selecione uma data do calendario',
        error_format_text='Data invalida',
        switch_to_calendar_icon=ft.icons.CALENDAR_MONTH,
        switch_to_input_icon=ft.icons.EDIT,

        date_picker_entry_mode=ft.DatePickerEntryMode.INPUT_ONLY,
        date_picker_mode=ft.DatePickerMode.YEAR,
        value=datetime.date(2024, 1, 5), # data inicial
        first_date=datetime.date(2024, 1, 20),# data limite
        error_invalid_text=' Data fora do limite',
        keyboard_type=ft.KeyboardType.NUMBER,

        on_change=lambda _: print(dp.value)
    )

    
    page.overlay.append(dp)
    page.overlay.append(tp)

    btn = ft.ElevatedButton('abri', on_click=lambda _: tp.pick_time())   
    btn2 = ft.ElevatedButton('abri', on_click=lambda _: dp.pick_date())

    page.add(btn,btn2)

ft.app(main)