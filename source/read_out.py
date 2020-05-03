import pandas as pd

def kol_naam_lijst_builder(mes_waarde=1):
    kollomnaamlijst = []

    for count in range(1, mes_waarde + 1):
        # 5 = len (list) of mes
        # num = f"kolom_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"

        kollomnaamlijst.append(omschrijving)
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
        # feilnaam = f'file{count:>{0}{4}}'
        # print(naam)
        feilnaam = pd.read_csv(posix_pad_naar_file, ";")
        concatlist.append(feilnaam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes_waarde)
    print(kolomnamen)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    # lijst_over_axis_1.columns = [kolomnamen]

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1


def horizontaal_samenvoegen(opgebroken_posix_lijst, map_uit, meswaarde):
    count = 1
    for lijst_met_posix in opgebroken_posix_lijst:
        vdp_hor_stap = f'vdp_hor_stap_{count:>{0}{4}}.csv'
        vdp_hor_stap = map_uit/ vdp_hor_stap

        print(vdp_hor_stap)
        # df = lees_per_lijst(lijst_met_posix, meswaarde)
        # print(df.tail(5))

        lees_per_lijst(lijst_met_posix, meswaarde).to_csv(vdp_hor_stap, ";")

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



