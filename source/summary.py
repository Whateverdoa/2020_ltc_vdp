import os
import pandas as pd

def verticale_summary(summary_lijst, mes, paduit, ordernummer, aantal_vdps):
    gesplitste_lijst_sum = []
    begin = 0
    eind = mes
    for index in range(aantal_vdps):
        gesplitste_lijst_sum.append(summary_lijst[begin:eind])
        begin += mes
        eind += mes

    print(gesplitste_lijst_sum)


    sum_lijst_vert = []
    count = 0

    # _______________________________________________________
    # _______________________________________________________

    for naam in summary_lijst:
        df = f'df{count}'
        print(df)
        df = pd.read_csv(f'tmp/{naam}', ",", encoding="utf-8", dtype="str")
        # todo maak een try except versie om de komma kolon optevangen
        #     df2 = pd.DataFrame([[f'{ordernummer}_baan_{count+1}']], dtype="str")
        df2 = pd.DataFrame([[f'{ordernummer}_baan_{count + 1} | {df.aantal.astype(int).sum()} etiketten']])  # dtype="int"
        print(df.aantal.astype(int).sum())

        sum_lijst_vert.append(df2)
        sum_lijst_vert.append(df)

        count += 1

        sam2 = pd.concat(sum_lijst_vert, axis=0).to_csv(f"{ordernummer}_v_sum.csv", ";")