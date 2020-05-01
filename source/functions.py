import pandas as pd
from pathlib import Path


def splitter(file_in,
             aantal_banen,
             afwijkings_waarde,
             totaal,
             aantal_rollen,
             ongeveer_per_baan,
             outgoing_posix_pad):
    """"alle variabelen  als argument  try *arg"""
    # afwijkings_waarde = 0 deze komt nu uit def

    file_in = pd.read_csv(file_in, ";")
    a = 0

    begin_eind_lijst = []
    be_LIJST = []

    for num in range(aantal_rollen):
        b = file_in.aantal.iloc[a:num].sum()
        # print(a, num)

        if num == (len(file_in) - 1):
            c = file_in.aantal.iloc[a:num].sum()
            begin_eind_lijst.append([c, a, num + 1])
            be_LIJST.append([a, num + 1])

            csv_naam = Path(f"{outgoing_posix_pad}/{a:>{0}{5}}.csv")
            print(csv_naam)
            file_in.iloc[a : (num + 1)].to_csv(csv_naam)
            print("splitter klaar")

        elif b >= ongeveer_per_baan + afwijkings_waarde:

            csv_naam = Path(f"{outgoing_posix_pad}/{a:>{0}{5}}.csv")
            print(csv_naam)
            file_in.iloc[a : (num + 1)].to_csv(csv_naam)

            begin_eind_lijst.append([b, a, num])
            be_LIJST.append([a, num + 1])
            be_LIJST.append(f"[{a}:{num}]")
            a = num + 1

        continue

    return print(begin_eind_lijst), print(be_LIJST)

def check_map_op_mes(mes,
                     maplengte,
                     min_waarde_rol,
                     file_in,
                     aantal_banen,
                     afwijkings_waarde=0):
    # for loop of while true loop
    mes_controle = aantal_banen
    print(f'mes controle = {mes_controle}')
    print(f'maplengte = {maplengte}')
    if mes_controle == maplengte:
        print("ok")
        print(afwijkings_waarde, maplengte)
        return True

    elif mes_controle < maplengte:
        print("te weinig")
        # afwijkings_waarde += min_waarde_rol
        print(mes_controle, maplengte)
        # mappen opschonen
        # nieuwe waardes toepassen in splitter()
        return False

    else :
        print("te veel")
        print(afwijkings_waarde, maplengte)
        return False


def print_trespa_rolls(colorcode, beeld, aantal, filenaam_uit, ee = 10):
    """
    Take line from list and build csv for that line
    """
    oap = overaantalpercentage = 1  # 1.02 = 2% overlevering
    # ee = 4  # = etiketten overlevering handmatig

    with open(filenaam_uit, "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f"{colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)

        print(f";{beeld}\n" * int(aantal * oap + ee), end="", file=fn)
        # print(f"{colorcode}, {int(aantal * oap)};leeg.pdf\n", end="", file=fn)

        print(f"{colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)
        print(f";stans.pdf\n", end="", file=fn)

    return 3 + int(aantal * oap + ee)


def banen_builder(lijst_van_split_csv, posix_pad_tmp, posix_pad_vdps_uit):
    count = 0
    for row in lijst_van_split_csv:
        file_Naam_In = f'{posix_pad_tmp / row}'
        # print(file_Naam_In)


        # file_Naam_In = f"{naam}_inschiet.csv"
        filenaam_uit = f"{posix_pad_vdps_uit}\\vdp{count:>{0}{5}}_bewerkt.csv"
        # print(file_Naam_In)
        # print(filenaam_uit)
        count += 1

        trespa_lijst = pd.read_csv(file_Naam_In, ",", encoding="utf-8")
        # print(trespa_lijst[0:1])

        oap = overaantalpercentage = 1  # 1.02 = 2% overlevering
        ee = 4  # = etiketten overlevering handmatig

        df = trespa_lijst[["Colorcode", "beeld", "aantal"]]
        df.to_csv("lijst_in.csv", index=0)

        new_input_list = []

        with open("lijst_in.csv") as input:
            num = 0
            for row in input:
                line_split = row.split(",")

                new_input_list.append(line_split)
                num += 1

        list_length = len(new_input_list)

        beg = 1
        eind = 2

        with open(filenaam_uit, "w", encoding="utf-8") as fn:

            print("omschrijving1;pdf1", file=fn)

        with open(filenaam_uit, "a", encoding="utf-8") as fn:
            for _ in range(list_length - 1):
                a = str(new_input_list[beg:eind][0][0])
                b = str(new_input_list[beg:eind][0][1])
                c = int(new_input_list[beg:eind][0][2])
                print_trespa_rolls(a, b, c, filenaam_uit)

                beg += 1
                eind += 1



def lijstmaker_uit_posixpad_csv(padnaam):
    rollen_posix_lijst = [rol for rol in padnaam.glob("*.csv") if rol.is_file()]
    return rollen_posix_lijst


def html_sum_form_writer(titel="summary", **kwargs):
    """"build a html file for summary purposes with  *kwargv
    search jinja and flask
    css link toevoegen
    """
    for key, value in kwargs.items():
        print(key, value)

    naam_html_file = f'summary/{titel}_.html'
    with open(naam_html_file, "w") as f_html:

        #         for key, value in kwargs.items():
        #             print(key, value)

        print("<!DOCTYPE html>\n", file=f_html)
        print('<html lang = "en">\n', file=f_html)
        print("     <head>\n", file=f_html)
        print("<meta charset='UTF-8>'\n", file=f_html)
        print(f"<title>{titel.capitalize()}</title>\n", file=f_html)
        print("     </head>", file=f_html)
        print("         <body>", file=f_html)
        for key, value in kwargs.items():
            print(f' <p><b>{key}</b> : {value}<p/>', file=f_html)

        print("         </body>", file=f_html)
        print(" </html>", file=f_html)
    return naam_html_file


def lijst_opbreker(lijst_in, mes, combinaties):
    start = 0
    end = mes
    combinatie_binnen_mes = []

    for combinatie in range(combinaties):
        # print(combinatie)
        combinatie_binnen_mes.append(lijst_in[start:end])
        start += mes
        end += mes
    return combinatie_binnen_mes


def kol_naam_lijst_builder(mes_waarde=1):
    kollomnaamlijst = []

    for count in range(1, mes_waarde + 1):
        # 5 = len (list) of mes
        num = f"kolom_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(pdf)
        # kollomnaamlijst.append(omschrijving)

    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst


def lees_per_lijst(lijst_met_posix_paden, mes_waarde):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        # print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        # print(naam)
        naam = pd.read_csv(posix_pad_naar_file)
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes_waarde)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1


def horizontaal_samenvoegen(opgebroken_posix_lijst, map_uit, meswaarde):
    count = 1
    for lijst_met_posix in opgebroken_posix_lijst:
        vdp_hor_stap = f'vdp_hor_stap_{count:>{0}{4}}.csv'
        vdp_hor_stap = map_uit/ vdp_hor_stap
        # print(vdp_hor_stap)
        df = lees_per_lijst(lijst_met_posix, meswaarde)
        # print(df.tail(5))

        lees_per_lijst(lijst_met_posix, meswaarde).to_csv(vdp_hor_stap, index=0)

        count += 1
    return print("hor")


def stapel_df_baan(naam,lijstin, ordernummer, map_uit):
    stapel_df = []
    for lijst_naam in lijstin:
        # print(lijst_naam)
        to_append_df = pd.read_csv(
            f"{lijst_naam}", ",", dtype="str", index_col=0)
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{map_uit}/{naam}_{ordernummer}.csv", ",")
    return pd.DataFrame(stapel_df)


def kolom_naam_gever_num_pdf_omschrijving(mes=1):
    """supplies a specific string  met de oplopende kolom namen num_1, pdf_1, omschrijving_1 etc"""

    def list_to_string(functie):
        kolom_namen = ""
        for kolomnamen in functie:
            kolom_namen += kolomnamen + ","
        return kolom_namen[:-1] + "\n"

    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(pdf)
        kollomnaamlijst.append(omschrijving)

    namen = list_to_string(kollomnaamlijst)

    return namen


def wikkel_n_baans_tc(input_vdp_posix_lijst, etiketten_Y, in_loop, mes):
    """last step voor VDP adding in en uitloop"""

    inlooplijst = (".,stans.pdf,," * mes)
    inlooplijst = inlooplijst[:-1] + "\n" # -1 removes empty column in final file

    for file_naam in input_vdp_posix_lijst:
        with open(f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        nieuwe_vdp_naam = VDP_Def / file_naam.name
        with open(nieuwe_vdp_naam, "w", encoding="utf-8") as target:
            target.writelines(kolom_naam_gever_num_pdf_omschrijving(mes))

            target.writelines(readline[1:etiketten_Y + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                (inlooplijst) * in_loop)  # inloop
            print("inloop maken")
            target.writelines(readline[1:])  # bestand

            target.writelines(
                (inlooplijst) * in_loop)  # inloop  # uitloop
            print("uitloop maken")
            target.writelines(readline[-etiketten_Y:])