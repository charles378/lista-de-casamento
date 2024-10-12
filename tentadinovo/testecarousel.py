import flet as ft 
 
def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE
 
    # Inicializar a lista de imagens com URLs iniciais
    image_controls = [ft.Image(src=f'https://picsum.photos/250/300?{num}') for num in range(10)]
 
    def move_backward(e):
        carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()
    
    def move_forward(e):
        carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()
 
    def on_result(event: ft.FilePickerResultEvent):
        if event.files:
            # Apender as novas imagens ao carrossel
            for file in event.files:
                new_image = ft.Image(src=file.path, width=250, height=300, fit=ft.ImageFit.COVER)
                carousel.controls.append(new_image)
            carousel.update()
 
    file_picker = ft.FilePicker(on_result=on_result)
 
    layout = ft.Container(
        shadow=ft.BoxShadow(blur_radius=100),
        content=ft.Column(
            controls=[
                carousel := ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=image_controls
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
                        ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True))
                    ]
                )
            ]
        )
    )
 
    # Adicionar o FilePicker ao overlay da página
    page.overlay.append(file_picker)
    page.add(layout)
 
if __name__ == '__main__':
    ft.app(target=main)