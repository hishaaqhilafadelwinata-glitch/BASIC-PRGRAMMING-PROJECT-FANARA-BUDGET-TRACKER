import flet as ft
import json
import os
from utils.transactions import delete_data
from components.dashboard_cards import DashboardCard
folder_dir = "Database"
file_dir = "Data.json"
current_file = os.path.abspath(__file__)
pages_folder = os.path.dirname(current_file)
project_folder = os.path.dirname(pages_folder)
data_folder = os.path.join(project_folder, folder_dir)
full_path = os.path.join(data_folder, file_dir)

class TransactionList(ft.Container):
    def __init__(self, on_delete_update):
        super().__init__()
        self.alignment= ft.alignment.top_center
        self.height= 400
        self.width= 400
        self.bgcolor= "#FFFFFF"
        self.clip_behavior= ft.ClipBehavior.ANTI_ALIAS
        self.on_delete_update= on_delete_update
        self.border_radius= ft.border_radius.only(
            top_left=1000, top_right=1000
        )
        self.border= ft.border.only(
            top=ft.border.BorderSide(2, "#2D2D2D"),
            left=ft.border.BorderSide(2, "#2D2D2D"),
            right=ft.border.BorderSide(2, "#2D2D2D")
        )
        self.expand=True
        self.icon_dict={
            "Salary":[ft.Icons.MONETIZATION_ON,"green"],
            "Dividen":[ft.Icons.CASES, "blue"],
            "Gift":[ft.Icons.WALLET_GIFTCARD, "purple"],
            "Others":[ft.Icons.MORE_HORIZ, "#D89F64"],
            "Food":[ft.Icons.RESTAURANT, '#9ED864'], 
            "Transportation":[ft.Icons.DIRECTIONS_CAR, '#64BCD8'],
            "Lifestyle":[ft.Icons.WEEKEND, '#649DD8'],
            "Health":[ft.Icons.HEALTH_AND_SAFETY, '#6465D8'],
            "Electrical":[ft.Icons.ELECTRIC_BOLT, '#D86464'], 
            "Education":[ft.Icons.SCHOOL, '#D8C564'],
            "Entertainment":[ft.Icons.MOVIE, '#D864B4'],
            None:[ft.Icons.QUESTION_MARK, "#B6AEAE"]
        }
        self.content=self.show_transaction()
    def show_transaction(self):
        empty_widget = ft.Column(
            controls=[
                ft.Icon(ft.Icons.RECEIPT_LONG_OUTLINED, size=70, color="#555555"),
                ft.Text("Your transactions will show here", size=14, 
                        color="#2D2D2D", italic=True,
                        weight=ft.FontWeight.BOLD),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0
            )
        if not os.path.exists(full_path):
            return empty_widget
        try:
            container_list = ft.Column(
                spacing=5, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.HIDDEN,
                expand=True,
                controls=[
                    ft.Container(
                        height=80
                    )
                ]
            )
            with open(full_path, 'r') as file:
                data = json.load(file)
            if not data:
                return empty_widget
            for transaction in data:
                data= transaction["id"]
                label = transaction["title"]
                date = transaction["date"]
                amount = transaction["amount"]
                tipe = transaction["Type"]
                category = transaction["Category"]
                icon_data= self.icon_dict[category][0]
                bgicon_data= self.icon_dict[category][1]
                container=self.create_container(dataid=data, label=label,
                                          date=date, amount=amount,
                                          sublabel=category, tipe=tipe,
                                          icon=icon_data, bgicon=bgicon_data)
                container_list.controls.append(container)
            container_list.controls.append(ft.Container(height=100))
            return ft.ShaderMask(
                content=container_list,
                blend_mode=ft.BlendMode.DST_IN,
                shader=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[ft.Colors.TRANSPARENT, ft.Colors.BLACK, ft.Colors.BLACK, ft.Colors.TRANSPARENT],
                    stops=[0.0, 0.05, 0.95, 1.0],
                )
            )
        except json.JSONDecodeError:
            return empty_widget
    def create_container(self, dataid, label,
                         amount, date, tipe, sublabel,
                         icon, bgicon, amount_col=''):
        amount = f"+{amount}" if tipe == 'Income' else f"-{amount}"
        amount_col = 'green' if tipe == 'Income' else 'red'

        def click(e):
            data= {
                "id":dataid,
                "title":label,
                "amount":amount,
                "date":date,
                "Type":tipe,
                "Category":sublabel
            }
            e.page.client_storage.set("Edit data", data)
            e.page.go('/income') if data["Type"]=="Income" else e.page.go('/expense')

        def hover(e):
            e.control.shadow= ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12) if e.data =="true" else None
            e.control.scale= 1.03 if e.data=="true" else 1
            e.control.update()

        return ft.Container(
            padding=10, bgcolor="#FFFFFF", 
            border_radius=24,
            height=100,
            width=300,
            border=ft.border.all(1, "#2D2D2D"),
            ink=True, on_click= click, on_hover=hover,
            animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            content= ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        spacing=15,
                        controls=[
                            ft.Container(
                                bgcolor=bgicon,
                                height=50,
                                width=50,
                                border_radius=20,
                                alignment=ft.alignment.center,
                                content=ft.Icon(icon,
                                    color='white',size=30)),
                            ft.Column(
                                spacing=2,
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(label, size=16, color="#222222",
                                            weight=ft.FontWeight.BOLD),
                                    ft.Text(sublabel, size=12, color=ft.Colors.GREY_900)
                                ]
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(
                                spacing=2,
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        content=ft.Text(amount, size=18, color=amount_col,
                                            tooltip=f"{amount}",no_wrap=True, 
                                            overflow=ft.TextOverflow.ELLIPSIS),
                                        width=80
                                    ),
                                    ft.Text(date, size=12, color=ft.Colors.GREY_900)
                                ]
                            ),
                            ft.IconButton(ft.Icons.DELETE_FOREVER, icon_color="#B10000",
                                        on_click=lambda e: self.delete(dataid))
                        ],
                        spacing=0
                    )
                ]
            )
        )
    def delete(self, Id):
        delete_data(Id)
        self.content= self.show_transaction()
        self.update()

        self.on_delete_update()