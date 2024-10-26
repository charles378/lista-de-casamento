
import flet as ft
import json
import os

# Caminho do arquivo para salvar as URLs das imagens e do avatar
IMAGE_FILE = "images.json"
AVATAR_FILE = "avatar.json"

def Home(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    # Carregar as URLs das imagens salvas
    if os.path.exists(IMAGE_FILE):
        with open(IMAGE_FILE, "r") as file:
            image_urls = json.load(file)
    else:
        image_urls = [f'https://picsum.photos/250/300?{num}' for num in range(10)]

    # Carregar a URL do avatar salvo
    if os.path.exists(AVATAR_FILE):
        with open(AVATAR_FILE, "r") as file:
            avatar_url = json.load(file)
    else:
        avatar_url = 'https://www.naoviu.com.br/wp-content/uploads/2023/08/Spacex.jpg'

    def expand_image(e):
        for c in carousel.controls:
            c.col = 1
        e.control.col = 12 - len(carousel.controls) + 1
        carousel.update()

    carousel = ft.ResponsiveRow(
        columns=12,
        spacing=5,
        controls=[
            ft.Container(
                col=1,
                content=ft.Image(src=url, fit=ft.ImageFit.COVER, width=250, height=300),
                border_radius=ft.border_radius.all(5),
                on_click=expand_image
            ) for url in image_urls[:6]  # Limitar a 6 imagens
        ]
    )

    if carousel.controls:
        carousel.controls[0].col = 12 - len(carousel.controls) + 1

    def on_result(event: ft.FilePickerResultEvent):
        if event.files and len(carousel.controls) < 6:  # Verificar se há menos de 6 imagens
            for file in event.files:
                new_image = ft.Container(
                    col=1,
                    content=ft.Image(src=file.path, fit=ft.ImageFit.COVER, width=250, height=300),
                    border_radius=ft.border_radius.all(5),
                    on_click=expand_image
                )
                carousel.controls.append(new_image)
                image_urls.append(file.path)
            carousel.update()
            save_images()

    def on_avatar_result(event: ft.FilePickerResultEvent):
        if event.files:
            avatar.src = event.files[0].path
            avatar.update()
            save_images()

    def delete_image(e):
        if carousel.controls:
            carousel.controls.pop()
            image_urls.pop()
            carousel.update()
            save_images()

    def delete_avatar(e):
        avatar.src = ''
        avatar.update()
        save_images()

    def save_images():
        with open(IMAGE_FILE, "w") as file:
            json.dump(image_urls, file)
        with open(AVATAR_FILE, "w") as file:
            json.dump(avatar.src, file)

    file_picker = ft.FilePicker(on_result=on_result)
    avatar_picker = ft.FilePicker(on_result=on_avatar_result)

    avatar = ft.Image(
        src=avatar_url,
        height=180,
        width=180,
        fit=ft.ImageFit.COVER,
        border_radius=ft.border_radius.all(120),
        offset=ft.Offset(x=1.3, y=0.1)
    )
    botao = ft.Row([
        ft.ElevatedButton('Minha lista', on_click=lambda _: page.go('/casal')), 
        ft.ElevatedButton('convidador', on_click=lambda _: page.go('/validador_sanha'))],
        alignment=ft.alignment.center,
        )
    data_falta = ft.Container(
        content=ft.Text('Falta tantos dias e 00.00.00 segundos'),
        offset=ft.Offset(x=0.9, y=1.5),)
    


    layout = ft.Container(
        width=700,
        height=310,  # Aumentei a altura para garantir espaço para os botões
        shadow=ft.BoxShadow(blur_radius=500),
        bgcolor=ft.colors.GREY_200,
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(5),
        offset=ft.Offset(x=0, y=0.2),
        content=ft.Column(
            controls=[
                carousel,
               
            ]
        )
    )

    page.overlay.append(file_picker)
    page.overlay.append(avatar_picker)
    #page.add(avatar,layout)
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column([
            avatar,
            data_falta,
            ft.Container(
                content=botao,             
                alignment=ft.alignment.center,
                width=240,
                bgcolor=ft.colors.WHITE12,
                border_radius=50,
                offset=ft.Offset(x=0.9, y=1.2)
              ),
            layout
           ],
           alignment=ft.alignment.center,
        )
    )
