class Solution(object):
    """Vytvořím si objekt, který bude mít 2 funkce. Objekt se jmenuje Solution(řešení), a řešení má 2 možnosti, buď complicated nebo short"""

    # Funkce bere 2 argumenty, počet čtverců co chceme a velikost vektoru o který posouváme
    # kwargs je keywords arguments a používá se to pro lepší orientaci
    def generate_n_rectangles_complicated(self, **kwargs):
        """Tohle je funkce, která je náročná. Nejprve udělá prázdné pole plné '  ', potom do středu dá # poté pomocí vektorů tyto # duplikuje
        i do rohů dalšího čtverce a pokračuje dokuď není v poslední vrstvě.
        Potom se spojí rohy čárou a vektorem se znovu posunou, ale teď do menšího čtverce.
        """

        number_of_rectangles = kwargs.get("počet_čtverců", 1)
        vector_length = kwargs.get("mezera_mezi_čtverci", 1)

        array = []  # hlavní pole ve kterém se vše děje
        list_of_sizes = []  # pole se všemi velikosti čtverců (používá se pro for loopy)

        # Tento loop přidá do list_of_sizes všechny velikosti
        for i in range(number_of_rectangles):
            list_of_sizes.append(
                i + 1
            )  # Python počítá od 0, tak tam potřebuju + 1, protože moje čtverce začínají od velikosti 1

        # Velikost finálního pole
        size = 1 + ((number_of_rectangles - 1) * vector_length * 2)

        # Vytvoření 2D pole, které má délku a výšku jako size a dá se tam '  '
        for row in range(size):
            row = ["  " for _ in range(size)]
            array.append(row)

        # Vytvoření # v centru
        center = (size-1)//2
        array[center][center] = "# "  # určíš souřadnicemi kde je # (y, x)

        # v defaultu to je [[2,2], [2,-2], [-2,2], [-2,-2]]
        vectors = [
            [vector_length, vector_length],
            [vector_length, -vector_length],
            [-vector_length, vector_length],
            [-vector_length, -vector_length],
        ]  # určím si vektory které budu používat pro posun
        list_of_centers = [[center, center]]  # list souřadnic se kterým chci pracovat
        visited = set(
            tuple(corner) for corner in list_of_centers
        )  # toto je list souřadnic které jsem navštívil, set je speciální druh listu, kde nejsou duplikáty a je neměný, využívá se při hledání

        for _ in range((len(list_of_sizes) - 1)):
            new_list_of_centers = []  # list nových středů

            # Tato smička mi veme střed a udělá z něho petern, co je třeba na kostce, když uka  zuje 5 (zduplikování symbolů do rohů)
            for cord in list_of_centers:
                x = cord[0]  # nastavení bodu x
                y = cord[1]  # nastavení bodu y

                # Toto jede pro každý vektor ve vektorech
                for vector in vectors:
                    dx, dy = (
                        vector  # Pro vektor [2, 2] je dx 2 a dy 2, pro vektor [2, -2] to bude dx 2 a dy -2
                    )
                    nx, ny = (
                        x + dx,
                        y + dy,
                    )  # Tohle udělá nx a ny což je součet souřadnice cord[0] a cord[1] a to se akorát sečte s vektorem, který jsme si vytvořili o řádek nahoře

                    # Podmínka, co jenom hlídá jestli nikde nepřesahujeme a už jsme nenavštívili ten bod
                    if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited:
                        # Jestli vše splňujeme na souřadnice nx a ny se hodí #
                        array[nx][ny] = "# "
                        new_list_of_centers.append(
                            [nx, ny]
                        )  # Uložíme si souřadnice do nových corners, protože tato funkce poběží i pro tyto vytvořené body
                        visited.add((nx, ny))  # Uložíme si bod i do navštívených bodů
                    list_of_centers = new_list_of_centers  # Změníme si list_of_centers na nový a smyčka jede tolikrát kolik máme čtverců
            # Tato funkce nám udělala šachovnici s '# ' nebo '  ', můžeme si rozhodnout vše o ní, velikost a i velikost mezi mezerami

        # vytvoříme si list souřadnic, kde jsou všechny rohy pole array
        list_of_corners = [
            [0, 0],
            [0, size - 1],
            [size - 1, 0],
            [size, size - 1],
        ]

        for _ in range((len(list_of_sizes) - 1)):
            # znovu si vytvoříme pole nových rohů
            new_list_of_corners = []

            #  deklarujeme si, co je horní levý, horní pravý etc. roh aby se nám kód lépe psal (topleft = 0,0, topright = 0, size-1 etc.)
            top_left, top_right, bottom_left, bottom_right = list_of_corners

            # pro každé x v poli horní levý a horní pravý x + 1 dáme #
            # Tohle jen že zadáme 2 souřadnice a podle osy x nám to nakreslí rovnou čáru '# '
            for x in range(top_left[1], top_right[1] + 1):
                array[top_left[0]][x] = "# "

            # Tohle je to stejné akorát pro spodní rohy
            for x in range(bottom_left[1], bottom_right[1] + 1):
                array[bottom_left[0]][x] = "# "

            # Toto je to stejné ale místo osy x to je pro osu y
            # Toto kreslí levou stěnu
            for y in range(top_left[0], bottom_left[0]):
                array[y][top_left[1]] = "# "

            # Toto kreslí pravou stěnu
            for y in range(top_right[0], bottom_right[0]):
                array[y][top_right[1]] = "# "

            # Teď si pouze všechny rohy posunu o 2 do středu, zase pomocí vektoru
            new_list_of_corners.append(
                [top_left[0] + vector_length, top_left[1] + vector_length]
            )
            new_list_of_corners.append(
                [top_right[0] + vector_length, top_right[1] - vector_length]
            )
            new_list_of_corners.append(
                [bottom_left[0] - vector_length, bottom_left[1] + vector_length]
            )
            new_list_of_corners.append(
                [bottom_right[0] - vector_length, bottom_right[1] - vector_length]
            )

            # Změníme list rohů
            list_of_corners = new_list_of_corners
        # Tato smyčka jede zase podle toho kolik máme čtverců a z šachovnice udělá finální výtvor

        # Celé pole vytiskneme
        for row in array:  # pro linku v poli
            for char in row:  # pro symbol v lince
                print(char, end="")  # tisk symbolu buď '# ' nebo '  '
            print("")  # odřádkování

    # do funkce vložíme jenom celkový počet čtverců
    def generate_n_rectangles_short(self, number_of_rectangles):
        # Toto není moje řešení, ale napadlo to člena soutěže TdA
        size = 1 + (
            (number_of_rectangles - 1) * 4
        )  # nastavení velikosti celkového pole

        for y in range(
            size
        ):  # pro y v size (v pythnu jak jsme už psal nahoře se první bere osa Y, protože když máme 2 rozměrné pole, tak máme 2 závorky [0][0] s dvěmi indexy a první
            # první ukazuje v jakém subpoli se pohybujeme a druhé ukazuje v jakém prvku toho sub pole jsme, takže jestli máme tohle:
            # [
            # ['a', 'b', 'c'],
            # ['1', '2', '3'],
            # ['z', 'x', 'y']
            # ]
            # tak to je jedno velké pole kde jsou 3 malá pole, první nám ukazuje v jakém poli se pohybujeme pole[0] = pismenka, pole[1] = čísla, pole[2] = souřadnice a teprve druhá nám
            # ukazuje kde v tom druhém poli jsme pole[0][0] = a, pole[2][2] = y

            # Takže ta smička nahoře jede pro velká pole a tohle pro každý ten jednotlivý prvek
            for x in range(size):
                # Toto je if vložené do funcke a říká to: vytiskni # pokud minimální hodnota z x,y size-x-1, size-y-1 je dělitelná 2 beze zbytku, jinak vytiskni '  '
                # Vlastně to funguje na tom, že čtverec je vždy v sudé vrstvě 0, 2, 4 etc. Takže se to jen podívá kde je to nejblíže k nějakému rohu min(x, y, size - x - 1, size - y - 1)
                # A jestli ta hodnota je dělitelná 2 tak tam je '# '
                print(
                    "# " if min(x, y, size - x - 1, size - y - 1) % 2 == 0 else "  ",
                    end="",
                )
            # Odřádkování
            print()


# Vytvoření 2 objektů solution a každá zavolá jinou funkci
Solution().generate_n_rectangles_complicated(
    počet_čtverců=3, mezera_mezi_čtverci=2
)  # bere si funkce 2 argumenty počet čtverců který chceme vytvořit a mezeru mezi čtverci
print()
Solution().generate_n_rectangles_short(3)

# Snad tento komentář někomu pomohl pochopit python lépe. Moje řešení tohoto problému nebylo nejlepší, co se týče jednoduchosti, ale k výsledku jsem se dostal, navíc to může generovat i
# jiné věci když se změní vektor
# Druhé řešení považuji za správné, jen mě to prostě nenapadlo. Creator: Víťa aka sprtokiller
