from vypis import Vypis

vypis = Vypis()

pokracovat = True  # přiřazení boolenovské hodnoty k proměnné pro použitý while cyklu

# nastavení špatné odpovědi
spatne = "Špatná odpověď, prosím znovu.\n"
neni = "\nHledaný pojištěnec se bohužel nenachází v seznamu, prosím pokračujte libovolnou klávesou do hlavní nabídky...\n"
velikost_sloupce = 18



# cyklus pro užívání aplikace dokud uživatel nezadá č. 4 - konec aplikace (False hodnota u Pokračovat)
while pokracovat:
    vypis.obrazovka_hlavicka_cela()
    spravne_zadani = False
    while spravne_zadani != True:  # cyklus pro zadání správné odpovědi, dokud nebude zadána, bude se opakovat
        try:
            vyber = int(input())
            if vyber == 1:
                spravne_zadani = True  # již nebude splněna podmínka - provedli jsme správné zadání
                from pridat_novy import PridatUzivatele  # importování třídy pro přidání nového uživatele

                pridat_uzivatele = PridatUzivatele()
                pridat_uzivatele.kompletni_zapis()  # zavolání funkce pro zápis nového uživatele



            elif vyber == 2:
                pozice = -1  # nastavení proměnné, která poumůže s výpisem požadovaných indexů z listu
                vypis.obrazovka_hlavicka()  # vyčištění obrazovky a vypsání hlavičky - loga
                spravne_zadani = True  # již nebude splněna podmínka - provedli jsme správné zadání
                pojistenci = pridat_uzivatele.__str__()  # načtení všech uložených/přidaných dat z třídy pridat_uzivatele do proměnné pojistenci
                while pozice != (len(pojistenci) - 1):  # cykl, který vypíše postupně všechny pojistence pod sebe
                    print("{0}{1}{2}{3}{4}{5}{6}".format(pojistenci[pozice + 1],
                                                         " " * (velikost_sloupce - len(pojistenci[pozice + 1])),
                                                         pojistenci[pozice + 2],
                                                         " " * (velikost_sloupce - len(pojistenci[pozice + 2])),
                                                         pojistenci[pozice + 3],
                                                         " " * (velikost_sloupce - len(str(pojistenci[pozice + 3]))),
                                                         pojistenci[pozice + 4]))

                    pozice += 4  # po vypsání se posuneme o 4 indexy na dalšího pojistence
                print("\nPokračujte libovolnou klávesou...\n")
                input()



            elif vyber == 3:
                spravne_zadani = True
                vypis.obrazovka_hlavicka()  # vyčištění obrazovky a vypsání hlavičky - loga
                jmeno = input("Zadejte jméno pojištěného:\n")
                prijmeni = input("\nZadejte příjmení pojištěného:\n")
                vypis.obrazovka_hlavicka()  # vyčištění obrazovky a vypsání hlavičky - loga
                pojistenci = pridat_uzivatele.__str__()  # načtení všech uložených/přidaných dat z třídy pridat_uzivatele do proměnné pojistenci
                if (jmeno and prijmeni) in pojistenci:
                    index_jmeno = pojistenci.index(jmeno)
                    index_prijmeni = pojistenci.index(prijmeni)  # zjištění indexu pro zadané příjmení
                    if (
                            index_prijmeni - index_jmeno) == 1:  # podmínka, že zadané jméno a příjmení musejí v listu být vedle sebe a tím pádem přísluší jednomu pojištěnci
                        print("{0}{1}{2}{3}{4}{5}{6}".format(pojistenci[index_jmeno],
                                                             " " * (velikost_sloupce - len(pojistenci[index_jmeno])),
                                                             pojistenci[index_prijmeni],
                                                             " " * (velikost_sloupce - len(pojistenci[index_prijmeni])),
                                                             pojistenci[index_prijmeni + 1], " " * (
                                                                         velikost_sloupce - len(
                                                                     str(pojistenci[index_prijmeni + 1]))),
                                                             pojistenci[index_prijmeni + 2]))
                        # výpis dat v uspořádaném formátu, každý sloupec nastaven na 15 znaků
                        print("\nPokračujte libovolnou klávesou...\n")
                        input()
                    else:  # pokud jméno a příjmení nejsou v listu vedle sebe, vypíše informaci, že pojistenec není v listu
                        print(neni)
                        input()
                else:  # pokud nenajdeme jmeno a prijmeni v listu, vypíše informaci, že pojistenec není v listu
                    print(neni)
                    input()



            elif vyber == 4:
                spravne_zadani = True
                pokracovat = False
                pass



            else:
                print(spatne)  # výpis hlášky o špatně zadaném vstupu v úvodním menu
        except:
            print(spatne)  # výpis hlášky o špatně zadaném vstupu v úvodním menu

vypis.obrazovka_hlavicka()
print("              GAME OVER - Thank you.\n------------------------------------------------\n")




