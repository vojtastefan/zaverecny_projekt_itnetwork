class Vypis:

    # hlavička - název aplikace
    def vypis_menu(self):
        return "------------------------------------------------\n              Evidence pojištěnců\n------------------------------------------------\n"

    # text pro menu
    def vyber_akci(self):
        return "Vyber akci:\n1  -  Přidat nového pojištěnce\n2  -  Vypsat všechny pojištěnce\n3  -  Vyhledat pojištěnce\n4  -  Game Over\n"

    #  vyčištění obrazovky
    def _vycisti_obrazovku(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    # vyčištění obrazovky a nahrání hlavičky včetně menu
    def obrazovka_hlavicka_cela(self):
        vypis._vycisti_obrazovku()
        print(vypis.vypis_menu())
        print(vypis.vyber_akci())

    # vyčištění obrazovky a nahrání hlavičky bez menu
    def obrazovka_hlavicka(self):
        vypis._vycisti_obrazovku()
        print(vypis.vypis_menu())

# vložení třídy výpis do proměnné
vypis = Vypis()