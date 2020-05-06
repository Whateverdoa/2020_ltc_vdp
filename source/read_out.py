import pandas as pd
import pathlib as Path

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


def filna_dict(mes):
    """"werkt. maar ga een dict comprehension proberen."""
    key = [f'pdf_{count+1}'for count in range(mes)]
    value = ['stans.pdf'for count in range(mes)]
    filna_tobe_inserted = dict(zip(key,value))
    return filna_tobe_inserted





def lees_per_lijst(lijst_met_posix_paden, mes_waarde):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        # print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        # print(naam)
        naam = pd.read_csv(posix_pad_naar_file, ";")
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes_waarde)

    filnaa_dict = filna_dict(mes_waarde)
    print(filnaa_dict)

    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    print(lijst_over_axis_1.head(10))
    print('-'*40)

    df = lijst_over_axis_1.columns = [kolomnamen]
    df = lijst_over_axis_1.fillna(filnaa_dict, inplace=True)




    # lijst_over_axis_1['pdf_8'].fillna("stans.pdf", inplace=True)
    # lijst_over_axis_1.fillna(value=filnaa_dict)
    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    # return lijst_over_axis_1
    return df




def horizontaal_samenvoegen(opgebroken_posix_lijst, map_uit, meswaarde, ordernummer):
    count = 1
    for lijst_met_posix in opgebroken_posix_lijst:
        vdp_hor_stap = f'{ordernummer}_{count:>{0}{4}}.csv'
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

# todo iterate over laatste VDP_final map
pad= Path(r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\2020_ltc_vdp\source\VDP_map\def_vdp_hor_stap_0001_def_vdp.csv")
file_uit = pad.parent.joinpath("nieuw.csv")
def filna_dict(mes):
    """"werkt. maar ga een dict comprehension proberen."""
    key = [f'pdf_{count+1}'for count in range(mes)]
    value = ['stans.pdf'for count in range(mes)]
    filna_tobe_inserted = dict(zip(key,value))
    return filna_tobe_inserted

fin = filna_dict(8)


df = pd.read_csv(pad, delimiter=";")
df.fillna(fin, inplace=True)
df.to_csv(file_uit, index=0)



