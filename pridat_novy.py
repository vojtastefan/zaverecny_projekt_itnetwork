from vypis import Vypis

class PridatUzivatele:

    # zadá křestní jméno a zapíše na poslední místo seznamu
    def pridat_krestni(self):
        self.krestni = input("Zadej křestní jméno pojištěného:\n")
        data_pojistencu.append(self.krestni)

    # zadá příjmení
    def pridat_prijemni(self):
        self.prijmeni = input("Zadej příjmení pojištěného:\n")
        data_pojistencu.append(self.prijmeni)

    # zadá tel. čísla, pouze integer
    def pridat_telefon(self):
        self.spravne = False
        while self.spravne != True:
            try:
                self.telefon = int(input("Zadej telefonní číslo pojištěného:\n"))
                self.spravne = True
            except:
                print("Špatné číslo, telefonní číslo musí obsahovat pouze číslice:\n")
        data_pojistencu.append(self.telefon)

    # zadání věku, integer v rozmězí 0 - 140
    def pridat_vek(self):
        self.spravne = False
        while self.spravne != True:
            try:
                self.vek = int(input("Zadej věk pojištěnce:\n"))
                if self.vek > 0 and self.vek < 140:
                    self.spravne = True
                else:
                    print("Špatný formát,věk musí obsahovat pouze číslice od 1 do 139\n")
                    self.spravne = False
            except:
                print("Špatný formát, věk musí obsahovat pouze číslice:\n")
        data_pojistencu.append(self.vek)


    # zadání vstupů

    def kompletni_zapis(self):
        vypis.obrazovka_hlavicka()
        pridat_uzivatele.pridat_krestni()
        pridat_uzivatele.pridat_prijemni()
        pridat_uzivatele.pridat_telefon()
        pridat_uzivatele.pridat_vek()
        vypis.obrazovka_hlavicka()
        print("Nový pojištěnec úspěšně přidán !\n\nPokračujte libovolnou klávesou...")
        input()

    # metoda, kterou budeme volat z main a které nám do proměnných bude ukládat celou databázi / list se všemi daty uživatelů
    def __str__(self):
        return data_pojistencu

pridat_uzivatele = PridatUzivatele()
vypis = Vypis()


data_pojistencu = []



