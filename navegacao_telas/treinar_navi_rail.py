import flet as ft


def main(page: ft.Page):

    def chamar_rota(e):
            match e.control.selected_index:
                case 0:
                    #page.go('/')
                    
                    page.add(ft.Text('teste home'))
              
                case 1:
                    #page.go('/cadastra')
              
                    page.add(ft.Text('teste teste'))


    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.HOME,),
            ft.NavigationRailDestination(icon=ft.icons.AC_UNIT)
        ],
        on_change=chamar_rota,
    )

    linha = ft.Row(controls=[rail], expand=True)

    page.add(linha)

if __name__ == '__main__':
    ft.app(main)