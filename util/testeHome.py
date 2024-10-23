
# import flet as ft
# import json
# import os

# # Caminho do arquivo para salvar as URLs das imagens e do avatar
# IMAGE_FILE = "images.json"
# AVATAR_FILE = "avatar.json"

# def main(page: ft.Page):
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.bgcolor = ft.colors.WHITE

#     # Carregar as URLs das imagens salvas
#     if os.path.exists(IMAGE_FILE):
#         with open(IMAGE_FILE, "r") as file:
#             image_urls = json.load(file)
#     else:
#         image_urls = [f'https://picsum.photos/250/300?{num}' for num in range(10)]

#     # Carregar a URL do avatar salvo
#     if os.path.exists(AVATAR_FILE):
#         with open(AVATAR_FILE, "r") as file:
#             avatar_url = json.load(file)
#     else:
#         avatar_url = 'https://www.naoviu.com.br/wp-content/uploads/2023/08/Spacex.jpg'

#     def expand_image(e):
#         for c in carousel.controls:
#             c.col = 1
#         e.control.col = 12 - len(carousel.controls) + 1
#         carousel.update()

#     carousel = ft.ResponsiveRow(
#         columns=12,
#         spacing=5,
#         controls=[
#             ft.Container(
#                 col=1,
#                 content=ft.Image(src=url, fit=ft.ImageFit.COVER, width=250, height=300),
#                 border_radius=ft.border_radius.all(5),
#                 on_click=expand_image
#             ) for url in image_urls
#         ]
#     )

#     if carousel.controls:
#         carousel.controls[0].col = 12 - len(carousel.controls) + 1

#     def on_result(event: ft.FilePickerResultEvent):
#         if event.files:
#             for file in event.files:
#                 new_image = ft.Container(
#                     col=1,
#                     content=ft.Image(src=file.path, fit=ft.ImageFit.COVER, width=250, height=300),
#                     border_radius=ft.border_radius.all(5),
#                     on_click=expand_image
#                 )
#                 carousel.controls.append(new_image)
#                 image_urls.append(file.path)
#             carousel.update()
#             save_images()

#     def on_avatar_result(event: ft.FilePickerResultEvent):
#         if event.files:
#             avatar.foreground_image_url = event.files[0].path
#             avatar.update()
#             save_images()

#     def delete_image(e):
#         if carousel.controls:
#             carousel.controls.pop()
#             image_urls.pop()
#             carousel.update()
#             save_images()

#     def save_images():
#         with open(IMAGE_FILE, "w") as file:
#             json.dump(image_urls, file)
#         with open(AVATAR_FILE, "w") as file:
#             json.dump(avatar.foreground_image_url, file)

#     file_picker = ft.FilePicker(on_result=on_result)
#     avatar_picker = ft.FilePicker(on_result=on_avatar_result)

#     avatar = ft.CircleAvatar(
#         col=3,
#         foreground_image_url=avatar_url,
#         height=240,
#         width=180,
#     )
    
#     layout = ft.Container(
#         width=700,
#         height=400,  # Aumentei a altura para garantir espaço para os botões
#         shadow=ft.BoxShadow(blur_radius=500),
#         bgcolor=ft.colors.GREY_200,
#         border_radius=ft.border_radius.all(10),
#         padding=ft.padding.all(5),
#         content=ft.Column(
#             controls=[
                
                
#                 carousel,
#                 ft.Row(
#                     alignment=ft.MainAxisAlignment.END,
#                     controls=[ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: avatar_picker.pick_files(allow_multiple=False), icon_color=ft.colors.AMBER),
#                         ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True)),
#                         ft.IconButton(icon=ft.icons.DELETE, on_click=delete_image)
#                     ]
#                 )
#             ]
#         )
#     )

#     page.overlay.append(file_picker)
#     page.overlay.append(avatar_picker)
#     page.add(avatar,layout)

# if __name__ == '__main__':
#     ft.app(target=main)


import flet as ft
import json
import os

# Caminho do arquivo para salvar as URLs das imagens e do avatar
IMAGE_FILE = "images.json"
AVATAR_FILE = "avatar.json"

def main(page: ft.Page):
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
            ) for url in image_urls
        ]
    )

    if carousel.controls:
        carousel.controls[0].col = 12 - len(carousel.controls) + 1

    def on_result(event: ft.FilePickerResultEvent):
        if event.files:
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

    def save_images():
        with open(IMAGE_FILE, "w") as file:
            json.dump(image_urls, file)
        with open(AVATAR_FILE, "w") as file:
            json.dump(avatar.src, file)

    file_picker = ft.FilePicker(on_result=on_result)
    avatar_picker = ft.FilePicker(on_result=on_avatar_result)

    avatar = ft.Image(
        src=avatar_url,
        width=240,
        height=240,
        fit=ft.ImageFit.COVER,
        border_radius=ft.border_radius.all(120)
    )

    layout = ft.Container(
        width=700,
        height=400,  # Aumentei a altura para garantir espaço para os botões
        shadow=ft.BoxShadow(blur_radius=500),
        bgcolor=ft.colors.GREY_200,
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(5),
        content=ft.Column(
            controls=[
                
                ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: avatar_picker.pick_files(allow_multiple=False)),
                carousel,
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True)),
                        ft.IconButton(icon=ft.icons.DELETE, on_click=delete_image)
                    ]
                )
            ]
        )
    )

    page.overlay.append(file_picker)
    page.overlay.append(avatar_picker)
    page.add(avatar,layout)

if __name__ == '__main__':
    ft.app(target=main)


import flet as ft
import json
import os

# Caminho do arquivo para salvar as URLs das imagens e do avatar
IMAGE_FILE = "images.json"
AVATAR_FILE = "avatar.json"

def main(page: ft.Page):
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
            ) for url in image_urls
        ]
    )

    if carousel.controls:
        carousel.controls[0].col = 12 - len(carousel.controls) + 1

    def on_result(event: ft.FilePickerResultEvent):
        if event.files:
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

    def save_images():
        with open(IMAGE_FILE, "w") as file:
            json.dump(image_urls, file)
        with open(AVATAR_FILE, "w") as file:
            json.dump(avatar.src, file)

    file_picker = ft.FilePicker(on_result=on_result)
    avatar_picker = ft.FilePicker(on_result=on_avatar_result)

    avatar = ft.Image(
        src=avatar_url,
        width=240,
        height=240,
        fit=ft.ImageFit.COVER,border_radius=ft.border_radius.all(120)
    )

    layout = ft.Container(
        width=700,
        height=400,  # Aumentei a altura para garantir espaço para os botões
        shadow=ft.BoxShadow(blur_radius=500),
        bgcolor=ft.colors.GREY_200,
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(5),
        content=ft.Column(
            controls=[
                
                ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: avatar_picker.pick_files(allow_multiple=False)),
                carousel,
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True)),
                        ft.IconButton(icon=ft.icons.DELETE, on_click=delete_image)
                    ]
                )
            ]
        )
    )


    page.overlay.append(file_picker)
    page.overlay.append(avatar_picker)
    page.add(avatar,layout)

if __name__ == '__main__':
    ft.app(target=main)