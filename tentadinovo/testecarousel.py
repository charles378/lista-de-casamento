# import flet as ft 
 
# def main(page: ft.Page):
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.bgcolor = ft.colors.WHITE
 
#     # Inicializar a lista de imagens com URLs iniciais
#     image_controls = [ft.Image(src=f'https://picsum.photos/250/300?{num}') for num in range(10)]
 
#     def move_backward(e):
#         carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
#         carousel.update()
    
#     def move_forward(e):
#         carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
#         carousel.update()
 
#     def on_result(event: ft.FilePickerResultEvent):
#         if event.files:
#             # Apender as novas imagens ao carrossel
#             for file in event.files:
#                 new_image = ft.Image(src=file.path, width=250, height=300, fit=ft.ImageFit.COVER)
#                 carousel.controls.append(new_image)
#             carousel.update()
 
#     file_picker = ft.FilePicker(on_result=on_result)
 
#     layout = ft.Container(
#         shadow=ft.BoxShadow(blur_radius=100),
#         content=ft.Column(
#             controls=[
#                 carousel := ft.Row(
#                     scroll=ft.ScrollMode.HIDDEN,
#                     controls=image_controls
#                 ),
#                 ft.Row(
#                     alignment=ft.MainAxisAlignment.END,
#                     controls=[
#                         ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
#                         ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
#                         ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True))
#                     ]
#                 )
#             ]
#         )
#     )
 
#     # Adicionar o FilePicker ao overlay da página
#     page.overlay.append(file_picker)
#     page.add(layout)
 
# if __name__ == '__main__':
#     ft.app(target=main)


# import flet as ft

# def main(page: ft.Page):
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.bgcolor = ft.colors.WHITE

#     # Inicializar a lista de imagens com URLs iniciais
#     image_controls = [ft.Image(src=f'https://picsum.photos/250/300?{num}') for num in range(10)]

#     def move_backward(e):
#         carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
#         carousel.update()

#     def move_forward(e):
#         carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
#         carousel.update()

#     def on_result(event: ft.FilePickerResultEvent):
#         if event.files:
#             # Apender as novas imagens ao carrossel
#             for file in event.files:
#                 new_image = ft.Image(src=file.path, width=250, height=300, fit=ft.ImageFit.COVER)
#                 carousel.controls.append(new_image)
#             carousel.update()

#     def delete_image(e):
#         if carousel.controls:
#             carousel.controls.pop()
#             carousel.update()

#     file_picker = ft.FilePicker(on_result=on_result)

#     layout = ft.Container(
#         shadow=ft.BoxShadow(blur_radius=100),
#         content=ft.Column(
#             controls=[
#                 carousel := ft.Row(
#                     scroll=ft.ScrollMode.HIDDEN,
#                     controls=image_controls
#                 ),
#                 ft.Row(
#                     alignment=ft.MainAxisAlignment.END,
#                     controls=[
#                         ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
#                         ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
#                         ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True)),
#                         ft.IconButton(icon=ft.icons.DELETE, on_click=delete_image)
#                     ]
#                 )
#             ]
#         )
#     )

#     # Adicionar o FilePicker ao overlay da página
#     page.overlay.append(file_picker)
#     page.add(layout)

# if __name__ == '__main__':
#     ft.app(target=main)


# import flet as ft
# import json
# import os

# # Caminho do arquivo para salvar as URLs das imagens
# IMAGE_FILE = "images.json"

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

#     image_controls = [ft.Image(src=url) for url in image_urls]

#     def move_backward(e):
#         carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
#         carousel.update()

#     def move_forward(e):
#         carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
#         carousel.update()

#     def on_result(event: ft.FilePickerResultEvent):
#         if event.files:
#             # Apender as novas imagens ao carrossel e salvar as URLs
#             for file in event.files:
#                 new_image = ft.Image(src=file.path, width=250, height=300, fit=ft.ImageFit.COVER)
#                 carousel.controls.append(new_image)
#                 image_urls.append(file.path)
#             carousel.update()
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

#     file_picker = ft.FilePicker(on_result=on_result)

#     layout = ft.Container(
#         shadow=ft.BoxShadow(blur_radius=100),
#         content=ft.Column(
#             controls=[
#                 carousel := ft.Row(
#                     scroll=ft.ScrollMode.HIDDEN,
#                     controls=image_controls
#                 ),
#                 ft.Row(
#                     alignment=ft.MainAxisAlignment.END,
#                     controls=[
#                         ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
#                         ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
#                         ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True)),
#                         ft.IconButton(icon=ft.icons.DELETE, on_click=delete_image)
#                     ]
#                 )
#             ]
#         )
#     )

#     # Adicionar o FilePicker ao overlay da página
#     page.overlay.append(file_picker)
#     page.add(layout)

# if __name__ == '__main__':
#     ft.app(target=main)

# import flet as ft
# import json
# import os

# # Caminho do arquivo para salvar as URLs das imagens
# IMAGE_FILE = "images.json"

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

#     image_controls = [ft.Image(src=url, width=250, height=300, fit=ft.ImageFit.COVER) for url in image_urls]

#     def move_backward(e):
#         carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
#         carousel.update()

#     def move_forward(e):
#         carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
#         carousel.update()

#     def on_result(event: ft.FilePickerResultEvent):
#         if event.files:
#             # Apender as novas imagens ao carrossel e salvar as URLs
#             for file in event.files:
#                 new_image = ft.Image(src=file.path, width=250, height=300, fit=ft.ImageFit.COVER)
#                 carousel.controls.append(new_image)
#                 image_urls.append(file.path)
#             carousel.update()
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

#     file_picker = ft.FilePicker(on_result=on_result)

#     layout = ft.Container(
#         shadow=ft.BoxShadow(blur_radius=100),
#         content=ft.Column(
#             controls=[
#                 carousel := ft.Row(
#                     scroll=ft.ScrollMode.HIDDEN,
#                     controls=image_controls
#                 ),
#                 ft.Row(
#                     alignment=ft.MainAxisAlignment.END,
#                     controls=[
#                         ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
#                         ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
#                         ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True)),
#                         ft.IconButton(icon=ft.icons.DELETE, on_click=delete_image)
#                     ]
#                 )
#             ]
#         )
#     )

#     # Adicionar o FilePicker ao overlay da página
#     page.overlay.append(file_picker)
#     page.add(layout)

# if __name__ == '__main__':
#     ft.app(target=main)

# import flet as ft
# import json
# import os

# # Caminho do arquivo para salvar as URLs das imagens
# IMAGE_FILE = "images.json"

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
#                 content=ft.Image(src=url, fit=ft.ImageFit.COVER),
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
#                     content=ft.Image(src=file.path, fit=ft.ImageFit.COVER),
#                     border_radius=ft.border_radius.all(5),
#                     on_click=expand_image
#                 )
#                 carousel.controls.append(new_image)
#                 image_urls.append(file.path)
#             carousel.update()
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

#     file_picker = ft.FilePicker(on_result=on_result)

#     layout = ft.Container(
#         width=700,
#         height=300,
#         shadow=ft.BoxShadow(blur_radius=500),
#         bgcolor=ft.colors.GREY_200,
#         border_radius=ft.border_radius.all(10),
#         padding=ft.padding.all(5),
#         content=ft.Column(
#             controls=[
#                 carousel,
#                 ft.Row(
#                     alignment=ft.MainAxisAlignment.END,
#                     controls=[
#                         ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files(allow_multiple=True)),
#                         ft.IconButton(icon=ft.icons.DELETE, on_click=delete_image)
#                     ]
#                 )
#             ]
#         )
#     )

#     page.overlay.append(file_picker)
#     page.add(layout)

# if __name__ == '__main__':
#     ft.app(target=main)


import flet as ft
import json
import os

# Caminho do arquivo para salvar as URLs das imagens
IMAGE_FILE = "images.json"

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

    def delete_image(e):
        if carousel.controls:
            carousel.controls.pop()
            image_urls.pop()
            carousel.update()
            save_images()

    def save_images():
        with open(IMAGE_FILE, "w") as file:
            json.dump(image_urls, file)

    file_picker = ft.FilePicker(on_result=on_result)

    layout = ft.Container(
        width=700,
        height=300,
        shadow=ft.BoxShadow(blur_radius=500),
        bgcolor=ft.colors.GREY_200,
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(5),
        content=ft.Column(
            controls=[
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
    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)
