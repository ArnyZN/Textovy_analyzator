"""text_analyzator.py: první projekt do Engeto Online Python Akademie

author: Arnošt Raab

email: arnost.raab@gmail.com

discord: Arnošt (Arny) R.#6219"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the UNION PACIFIC RAILROAD,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
print ("Zdravím uživateli. Vítáme tě v analyzátoru textu!")
print("*" * len("Zdravím uživateli. Vítáme tě v analyzátoru textu!"))
max_pokus = 1
registrovani_uzivatele = {"bob":"123", "ann":"pass123", "mike":"password123","liz":"pass123"}
uziv_jmeno = input ("Zadej uživatelské jméno: ")
if uziv_jmeno in registrovani_uzivatele:
    print (f"Ahoj {uziv_jmeno}!")
else: 
    print ("Takového uživatele neznám! Ukončuji program!")
    quit()
uziv_heslo = input ("Zadej uživatelské heslo: ")
while max_pokus <= 4:
    if registrovani_uzivatele[uziv_jmeno] == uziv_heslo:
        print("Heslo sedí")
        break
    elif max_pokus == 4:
        print ("Překročil jsi počet pokusů pro zadání hesla! Ukončuji program!")
        quit()
    else:
        uziv_heslo = input (f"Heslo nesedí! Zadej znovu uživatelské heslo! Máš už jen {4 - max_pokus} pokusů: ")
        max_pokus += 1
cislo_textu = input ("Vyber si zadáním čísla 1-3 nebo slovniho vyjadreni (jedna, dva, tri) text k analýze!: ")
slovni_zadani_textu = {"jedna":"1","dva":"2","tri":"3"}
if cislo_textu in slovni_zadani_textu.values():
    cislo_textu = int(cislo_textu) - 1
    print(f"Vybral jsi text číslo: {cislo_textu + 1}")
elif cislo_textu in slovni_zadani_textu:
    cislo_textu = int(slovni_zadani_textu[cislo_textu]) - 1
    print(f"Vybral jsi text číslo: {cislo_textu + 1}")
else:
    print("Takové číslo textu neexistuje! Ukončuji program!")
    quit()
print("-------------------------- Vybraný text -------------------------")
print(f"{TEXTS[cislo_textu]}")
pocet_slov = 0
slovo_VP = 0
slovo_z_VP = 0
slovo_MP = 0
slovo_z_MP = 0
cislo = 0
suma_cisel = 0
rozsekany_text = TEXTS[cislo_textu].split()
pocet_slov = len(rozsekany_text)
cisla = []
for slovo in rozsekany_text:
    if slovo[0].isupper():
        if slovo.isupper():
            slovo_z_VP+=1
        slovo_VP += 1
    elif slovo[0].islower():
        if slovo.islower():
            slovo_z_MP+=1
        slovo_MP += 1
    elif slovo[0].isdigit():
        if slovo.isdigit():
            cislo += 1
            suma_cisel += int(slovo)
        else:
            r=0 
            cislice=[]
            pismenka = list(slovo)
            for i in pismenka:
                if i[r].isdigit():
                    cislice += i
            cisla=int("".join(cislice))
            cislo += 1
            suma_cisel += cisla
print("----------------------------- Sumář ----------------------------")
print (f"{pocet_slov} slov v textu.")           
print (f"{slovo_VP} slov začínajících VP a {slovo_z_VP} slov(a) složených z VP.")
print (f"{slovo_MP} slov začínajících MP a {slovo_z_MP} slov(a) složených z MP.")
print (f"{cislo} slov(a) obsahujících číslo.")
print(f"Součet čísel v textu (včetně těch spojených s písmeny) je {suma_cisel}.")
print("-------------------------- Souhrný graf -------------------------")
print(len("- Druh ukazatele || Graficke vyjdreni cetnosti || Ciselny pocet -") * "-")
print("- Druh ukazatele || Graficke vyjdreni cetnosti || Ciselny pocet -")
print(len("- Druh ukazatele || Graficke vyjdreni cetnosti || Ciselny pocet -") * "-")
print ("Celkový počet slov v textu.               ||", pocet_slov * "*", "||", str(pocet_slov))
print ("Počet slov s velkým počátečním písmenem.  ||", slovo_VP * "*", "||", str(slovo_VP))
print ("Počet slov složených z velkých písmen.    ||", slovo_z_VP * "*", "||", str(slovo_z_VP))
print ("Počet slov s malým počátečním písmenem.   ||", slovo_MP * "*", "||", str(slovo_MP))
print ("Počet slov složených z malých písmen.     ||", slovo_z_MP * "*", "||", str(slovo_z_MP))
print ("Počet slov s číslem.                      ||", cislo * "*", "||", str(cislo))
