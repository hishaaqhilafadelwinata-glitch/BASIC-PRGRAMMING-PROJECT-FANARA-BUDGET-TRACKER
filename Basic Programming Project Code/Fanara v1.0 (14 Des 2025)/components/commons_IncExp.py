import flet as ft
import datetime
class Header(ft.Container):
    def __init__(self, on_save, label, labelclr, bgcolor):
        super().__init__()
        self.height= 120
        self.width=400
        self.border= ft.border.all(1, "#2D2D2D")
        self.margin= ft.margin.only(top=2, right=2, left=2)
        self.bgcolor= bgcolor
        self.label_txt= ft.Text(value=label, size=20, 
                            color=labelclr, 
                            weight=ft.FontWeight.BOLD,
                            width=240)
        self.save_btn= ft.ElevatedButton(content=ft.Text("Save", size=14,
                                                         weight=ft.FontWeight.BOLD,
                                                         color="#FFFFFF"), 
                            width=80, 
                            height=40, bgcolor="#6362D7", 
                            on_click= on_save, disabled=True,
                            color="#2D2D2D", 
                            style=ft.ButtonStyle(
                                side=ft.BorderSide(1, "#222222")),
                            on_hover= self.hover,
                            animate_scale= ft.Animation(300, ft.AnimationCurve.EASE_OUT)
                                )
        
        self.content= ft.Row(
            controls=[
                    ft.Container(width=10),
                    self.label_txt,
                    self.save_btn
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.padding= 20
    def hover(self, e):
        if e.control.disabled == False:
            e.control.scale = 1.05 if e.data == "true" else 1
            e.control.update()
class Input(ft.Container):
    def __init__(self, change):
        super().__init__()
        self.alignment= ft.alignment.center
        self.padding= 20
        self.input_field= ft.TextField(border_radius= 1000, 
                    label= 'Fill in here...', width= 350, on_change=change,
                    filled=True, bgcolor="#FFEBB0", 
                    content_padding=ft.padding.symmetric(vertical=30,
                                                         horizontal=20),
                    text_style=ft.TextStyle(weight=ft.FontWeight.BOLD,
                                            color="#2D2D2D"),
                    focused_border_color="#2D2D2D",
                    label_style=ft.TextStyle(color="#2D2D2D"))
        self.content= ft.Column(
            [
            ft.Text('   Title', size=16, 
                    color="#2D2D2D", weight=ft.FontWeight.BOLD),
            self.input_field
        ],
        spacing=0
    )
    
class Date(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment= ft.alignment.center
        self.padding= ft.padding.symmetric(horizontal=20)
        today= datetime.datetime.now()
        today_str= today.strftime("%d %b %Y")
        self.date_picker = ft.DatePicker(on_change=self.date_change)
        self.date_text= ft.Text(today_str, 
                                color="#2D2D2D", size=14)
        self.btn_date= ft.ElevatedButton(
            content=ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.CALENDAR_MONTH, 
                                    color="#2D2D2D", size=30),
                            self.date_text
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Icon(ft.Icons.EXPAND_MORE, 
                            color="#2D2D2D", size=40)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            width=350, height=50, style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=1000),
                side=ft.border.BorderSide(1, "#2D2D2D")
            ), bgcolor="#FFEBB0",
            on_click= lambda e:e.page.open(self.date_picker)
        )
        self.content= ft.Column(
            controls=[
                ft.Text(value=' Date', size=16, 
                        color='#222222', weight=ft.FontWeight.BOLD),
                self.btn_date
            ],
        )

    def date_change(self, e):
        new_date = e.control.value
        if new_date:
            self.date_text.value= new_date.strftime("%d %b %Y")
            self.btn_date.update()
    
class DialPad(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding= ft.padding.symmetric(horizontal=20)
        self.display = ft.TextField(
            value='0', text_align=ft.TextAlign.CENTER, text_size=30,
            color='#2D2D2D', read_only=True, bgcolor='#FFEBB0', 
            border_color="#2D2D2D", border_radius=30,
            text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
            filled=True, width=350
        )
        self.content= ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value='Amount', color='#222222', 
                        size=16, weight=ft.FontWeight.BOLD),
                    ],
                    width=350
                ),
                self.display,
                self.create_button()
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    def create_button(self):
        dial_pad=[
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['0', 'Del']
        ]
        column = ft.Column(spacing=5)
        for row in dial_pad:
            line = ft.Row(spacing=5, alignment=ft.MainAxisAlignment.CENTER)
            for char in row:
                btn = ft.ElevatedButton(
                    content=ft.Text(
                        char, size=15, weight=ft.FontWeight.BOLD,
                        color="#2D2D2D"
                    ), bgcolor="#C2C2C2", width=80,
                    height=50, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=25),
                        side=ft.border.BorderSide(1, "#2D2D2D")
                                                ),
                    on_click= lambda e, x=char: self.click(x)
                    
                )
                line.controls.append(btn)
            column.controls.append(line)
        return column
    
    def click(self, char):
        current_var = self.display.value.replace(".","")
        if char == 'Del':
            new_var = current_var[:-1]
            if new_var == '':
                self.display.value = '0'
            else:
                format_var = f"{int(new_var):,}".replace(",",".")
                self.display.value = format_var
        else:
            if current_var == '0':
                self.display.value = char
            else:
                new_var = current_var + char
                format_var = f"{int(new_var):,}".replace(",",".")
                self.display.value= format_var
                
        self.display.update()

class CategoryButton(ft.Container):
    def __init__(self, category):
        super().__init__()
        self.alignment= ft.alignment.center
        self.width=400
        self.padding=15
        self.content= self.create_button(cat=category)
        self.selected_value = None
    def create_button(self, cat):
        self.grid = ft.Row(spacing=10, run_spacing=5, 
                           wrap=True, alignment=ft.MainAxisAlignment.CENTER)
        for i in cat: 
            icon = i[0]
            color= i[1]
            label = i[2]
            sign = i[3]
            container = ft.Container(
                content=ft.Column(
                    controls=[
                                ft.Icon(icon,
                                size=30, color='white'),
                                ft.Text(label, size=10, color='white',
                                        weight=ft.FontWeight.BOLD)
                            ],  alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                border_radius=35, bgcolor=color, 
                ink=True, data= sign, on_click= self.handle_click,
                animate_scale= ft.Animation(300, ft.AnimationCurve.EASE_OUT),
                on_hover=self.hover, animate= ft.Animation(500, ft.AnimationCurve.EASE_OUT),
                height=80, width=80
            )
            container.original_color = color
            self.grid.controls.append(container)
        return self.grid
    def handle_click(self, e):
        self.selected_value = e.control.data
        for btn in self.grid.controls:
            if btn.data == self.selected_value:
                btn.bgcolor = btn.original_color
                btn.scale = 1.1
            else:
                btn.bgcolor = ft.Colors.GREY_400
                btn.scale = 1
            btn.update()
    def hover(self, e):
        if e.control.data == self.selected_value:
            e.control.scale = 1.1 
        else: 
            e.control.scale = 1.1 if e.data == 'true' else 1
        e.control.update()
    def get_category(self):
        return self.selected_value
