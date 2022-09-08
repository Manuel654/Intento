class ParseOption:
    @classmethod
    def display_menu(cls):
        print("1. Cargar archivo")
        print("2. Exportar ...")
    @classmethod
    def get_option(cls):
        ParseOption.display_menu()
        return int(input('Escriba su opción: '))
        