import flet as ft
from pages.home_page import Home
from pages.login_page import Login
from pages.AT_page import ATPage
from pages.start_page import StartPage
from pages.income_page import IncomePage
from pages.expense_page import ExpensePage

def main(page: ft.Page):
    page.title="Budget Tracker"
    page.padding= 0
    page.window.width= 400
    page.window.height= 750
    page.window.icon= "icon.ico"
    page.scroll= ft.ScrollMode.AUTO
    page.fonts={
        "Lato":"/fonts/Lato-Regular.ttf",
        "Lato-Bold":"/fonts/Lato-Bold.ttf",
        "Lato-Italic":"/fonts/Lato-LightItalic.ttf"
    }
    page.theme= ft.Theme(font_family="Poppins")

    routes = {
        '/': lambda: StartPage(page),
        '/login': lambda: Login(page),
        '/home': lambda: Home(
            username= 
            page.client_storage.get("Saved Name")),
        '/transaction': ATPage,
        '/income': IncomePage,
        '/expense': ExpensePage
    }
    def route_change(e):
        page.views.clear()
        url = routes.get(page.route)
        current_view= url()
        if url is None:
            page.route = '/'
            url= StartPage
        if hasattr(current_view, 'resize_content'):
            page.on_resized= current_view.resize_content
            current_view.resize_content(None)
        else:
            page.on_resized= None
        page.views.append(current_view)
        page.update()
    
    def view_pop(view):
        page.views.pop()
        pages = page.views[-1]
        page.go(pages.route)

    page.on_route_change=route_change
    page.on_view_pop=view_pop
    page.go('/')

if __name__ == "__main__":
    ft.app(target=main, 
           name="FanaraBudgetTracker", assets_dir="assets")