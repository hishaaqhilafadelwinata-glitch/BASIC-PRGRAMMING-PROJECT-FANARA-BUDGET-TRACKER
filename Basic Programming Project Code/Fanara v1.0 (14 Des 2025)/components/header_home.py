import flet as ft

class HeaderHome(ft.Container):
    def __init__(self, name):
        super().__init__()
        self.width=400
        self.height=120
        self.bgcolor='#FFC93D'
        self.margin= ft.margin.only(top=1, right=1, left=1)
        self.alignment= ft.alignment.center
        self.border= ft.border.all(1, "#2D2D2D")
        self.content= ft.Row(
            controls=[
                ft.Icon(
                     ft.Icons.PERSON, size=50, color="#0C48A6"
                ),
                ft.Container(width=10),
                ft.Column([
                    ft.Text("Welcome to Fanara Budget Tracker!", 
                        size=14, italic=True, color="#0C48A6"
                        ),
                    ft.Text(
                        name, size=18, color="#0C48A6",
                        weight=ft.FontWeight.BOLD
                    )
            ], 
            spacing=0,
            alignment=ft.MainAxisAlignment.CENTER),
            ft.IconButton(
                icon=ft.Icons.LOGOUT,
                icon_color="#0C48A6",
                tooltip="Logout",
                on_click= self.click_logout,
                icon_size=20
            )
        ], 
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0)

    def click_logout(self, e):
            pop_up = ft.AlertDialog(
                title=ft.Text("Log Out"),
                content=ft.Text("Are you sure?"),
                actions=[
                    ft.ElevatedButton(
                        text="Yes",
                        on_click= lambda e: e.page.go('/login'),
                        color="blue",
                        bgcolor=None
                    ),
                    ft.ElevatedButton(
                        text="No",
                        on_click=lambda e: e.page.close(pop_up),
                        color='red',
                        bgcolor= None
                    ),
                ],
                actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                modal=True
            )
            e.page.open(pop_up)