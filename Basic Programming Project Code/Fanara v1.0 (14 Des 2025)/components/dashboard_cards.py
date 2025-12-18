import flet as ft
from utils.summation import InEx_total, total

class DashboardCard(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor= "#FFFFFF"
        self.width= 350
        self.height= 240
        self.padding=20
        self.border_radius=20
        self.balance_text= ft.Text(f"IDR {total()}", size=35, 
                        weight=ft.FontWeight.BOLD, color='#2D2D2D',
                        tooltip=f"{total}", no_wrap=True,
                        overflow=ft.TextOverflow.ELLIPSIS)
        self.content= ft.Column(
            controls=[
                ft.Text("Total Balance", size=12, 
                        color="#2D2D2D", italic=True,
                        weight=ft.FontWeight.BOLD),
                self.balance_text,
                ft.Container(height=20),
                ft.Row(
                    controls=[
                        self.IncExp_card(icon=ft.Icons.ARROW_DOWNWARD, iconclr="#9ED864", iconbgclr="#196420", 
                                         label="Income", amount=InEx_total()[0], bgcolor="#9ED864",
                                         labelclr="#196420"),
                        self.IncExp_card(icon=ft.Icons.ARROW_UPWARD, iconclr="#FF7D7D", iconbgclr="#B10000", 
                                         label="Expense", amount=InEx_total()[1], bgcolor="#FF7D7D",
                                         labelclr="#B10000")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            ],
            spacing=0, 
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
        self.on_hover=self.hover
        self.animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT)
        self.border= ft.border.all(1, "#2D2D2D")
    def hover(self, e):
        e.control.scale=1.05 if e.data =='true' else 1
        e.control.shadow= ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12) if e.data =='true' else None
        e.control.update()    

    def IncExp_card(self, icon, iconclr, iconbgclr, bgcolor, label, amount, labelclr):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=40, height=40, border_radius=20,
                                bgcolor=iconbgclr, alignment=ft.alignment.center,
                                content=ft.IconButton(icon=icon, 
                                                    icon_color=iconclr, icon_size=20)
                            ),
                            ft.Text(label, size=16, 
                                    color=labelclr, weight=ft.FontWeight.BOLD),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Container(height=10),
                    ft.Container(
                        content=ft.Text(amount, size=22,
                            color="#222222", 
                            weight=ft.FontWeight.BOLD, 
                            tooltip=amount, no_wrap=True,
                            overflow=ft.TextOverflow.ELLIPSIS),
                        width=100
                    )
                ], 
                spacing=2,
                horizontal_alignment=ft.CrossAxisAlignment.START
            ),
            bgcolor=bgcolor,
            padding=15,
            border_radius=35,
            border=ft.border.all(1.5, "#2D2D2D")
        )
    
    def update_data(self):
        new_total = total()
        new_inc_exp = InEx_total()
        self.balance_text.value= f"IDR {new_total}"
        self.balance_text.tooltip= f"{new_total}"

        income_card = self.content.controls[3].controls[0]
        income_card.content.controls[2].content.value = new_inc_exp[0]
        income_card.content.controls[2].content.tooltip = new_inc_exp[0]

        expense_card = self.content.controls[3].controls[1]
        expense_card.content.controls[2].content.value = new_inc_exp[1]
        expense_card.content.controls[2].content.tooltip = new_inc_exp[1]

        self.update()
