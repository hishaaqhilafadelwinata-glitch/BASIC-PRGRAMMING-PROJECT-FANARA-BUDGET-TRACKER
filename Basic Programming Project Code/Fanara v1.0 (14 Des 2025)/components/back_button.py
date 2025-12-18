import flet as ft

class BackButton(ft.Container):
    def __init__(self):
        super().__init__()
        self.border_radius=ft.border_radius.only(
                        top_left=1000, top_right=1000
                    )
        self.border=ft.border.only(
                        top=ft.border.BorderSide(1, "#2D2D2D"),
                        right=ft.border.BorderSide(1, "#2D2D2D"),
                        left=ft.border.BorderSide(1, "#2D2D2D")
                    )
        self.bgcolor="#FFC93D"
        self.alignment=ft.alignment.top_center
        self.padding=ft.padding.only(top=20)
        self.width=350
        self.height=175
        self.content= ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.IconButton(
                                    ft.Icons.ARROW_BACK,
                                    icon_color="#FFC93D",
                                    icon_size=20,
                                    on_click= lambda e: e.page.go('/home')
                                ),
                                border_radius=30,
                                bgcolor="#B10000",
                                height=32,
                                width=32,
                                alignment=ft.alignment.center
                            ),
                            ft.Text("Back", size=20, 
                                    color="#B10000", 
                                    weight=ft.FontWeight.BOLD,
                                    italic=True)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                    )