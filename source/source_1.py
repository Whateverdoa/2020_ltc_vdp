import pandas as pd
from pathlib import Path
import PySimpleGUI as sg
import os

from source.paden import *
import source.functions as csv_builder
import source.messen as old_skool_read_outs
from source.summary import verticale_summary

import source.read_out as builder


'''
    Example of GUI
'''

while True:
    sg.change_look_and_feel('DarkBlue12')

    columns = []

    layout = [
        [sg.Text('VDP invul formulier', size=(30, 1), font=('Arial', 14, 'bold'), text_color="orange")],
        [sg.InputText('202012345', key='ordernummer_1'), sg.Text('Ordernummer', font=('Arial', 12))],
        [sg.InputText('8', key='mes'), sg.Text('mes', font=('Arial', 12))],
        [sg.InputText('1', key='vdp_aantal'), sg.Text("VDP's", font=('Arial', 12))],
        [sg.InputText('0', key='afwijkings_waarde'), sg.Text("afwijking_waarde", font=('Arial', 12))],

        [sg.Text()],

        [sg.InputText('10', key='Y_waarde'), sg.Text('Y-waarde')],
        [sg.Text('CSV_file')],
        [sg.Input(), sg.FileBrowse()],

        [sg.Text()],
        # [sg.InputText('', key='totaal'),sg.Text('Totaal')],

        # [sg.InputText('', key='pre'), sg.Text('Pre')],
        # [sg.InputText('', key='begin_1'),sg.Text('Begin nummer')],
        # [sg.InputText('', key='post'), sg.Text('Post')],

        # [sg.InputText('', key='aantal'),sg.Text('Aantal')],
        # [sg.InputText('', key='aantal_per_rol'),sg.Text('Aantal per rol')],

        [sg.InputText('1', key='overlevering_pct'), sg.Text('overlevering %')],
        [sg.InputText('10', key='ee'), sg.Text('extra etiketten')],
        [sg.InputText('10', key='wikkel'), sg.Text('Wikkel')],

        [sg.Button("Ok"), sg.Cancel()],
        # run button

        # this saves the input information
        [sg.Text('_' * 40)],
        [sg.Text('SAVE of LOAD inputform', size=(35, 1))],
        # [sg.Text('Your Folder', size=(15, 1), justification='right'),
        #  sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]

    ]

    window = sg.Window('VDP formulier 2020', layout, default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = window.read()

        if event in ('Exit', None):
            dir_names_lijst_to_be_cleaned = ["tmp", "VDP_map", "vdps", "stapel", "summary", "tmp2"]  # "vdps"

            cleaning_paden_met_Dir_lijst = [Path(wdir, dirnaam) for dirnaam in dir_names_lijst_to_be_cleaned]

            for file_pad in cleaning_paden_met_Dir_lijst:
                cleaner(file_pad)

            for file_pad in cleaning_paden_met_Dir_lijst:
                file_pad.rmdir()

            exit(0)

        elif event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=False)
            # False in mac OS otherwise it will crash
            window.SaveToDisk(filename)

            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=False)
            # False in mac OS otherwise it will crash
            window.LoadFromDisk(filename)
            # load(form)

        elif event == "Cancel":

            dir_names_lijst_to_be_cleaned = ["tmp", "VDP_map", "vdps", "stapel", "summary", "tmp2"]  # "vdps"

            cleaning_paden_met_Dir_lijst = [Path(wdir, dirnaam) for dirnaam in dir_names_lijst_to_be_cleaned]

            for file_pad in cleaning_paden_met_Dir_lijst:
                cleaner(file_pad)

            for file_pad in cleaning_paden_met_Dir_lijst:
                file_pad.rmdir()
            # todo screen message vraag of er echt gecancelled moet worden:)
            # todo clear  screen  als in een reset
            exit(0)

        elif event == "Ok":

            dir_names_lijst_to_be_cleaned = ["tmp"]  # "vdps"

            cleaning_paden_met_Dir_lijst = [Path(wdir, dirnaam) for dirnaam in dir_names_lijst_to_be_cleaned]

            for file_pad in cleaning_paden_met_Dir_lijst:
                cleaner(file_pad)


            ordernummer = values['ordernummer_1']
            mes = int(values['mes'])
            aantal_vdps = int(values['vdp_aantal'])
            etikettenY = int(values['Y_waarde'])
            name_file_in = Path(values['Browse'])
            # name_file_in = Path(r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\2020_ltc_vdp\source\file_in\202014342_proef.csv")
            afwijkings_waarde = int(values['afwijkings_waarde'])

            overlevering_pct = float(values['overlevering_pct'])
            extra_etiketten = int(values['ee'])
            wikkel = int(values['wikkel'])

            print(ordernummer,
                  mes,
                  aantal_vdps,
                  etikettenY,
                  name_file_in,
                  overlevering_pct,
                  extra_etiketten,
                  wikkel)



            pad_tmp = paden_dict['pad_tmp']
            pad_tmp2= paden_dict['pad_tmp2']
            pad_vdps = paden_dict['pad_naar_vdps']
            pad_sum = paden_dict['pad_sum']
            stapel = paden_dict['stapel']
            VDP_map =paden_dict['VDP_map']
            result = paden_dict["result"]




            aantal_banen = int(mes * aantal_vdps)

            file_in = pd.read_csv(name_file_in, delimiter=";", dtype="str")  # try except

            totaal = file_in.aantal.astype(int).sum()

            min_waarde = file_in.aantal.astype(int).min()

            row = aantal_rollen = len(file_in)

            opb = ongeveer_per_baan = (totaal // aantal_banen)

            combinaties = aantal_rollen // mes

            inloop = etikettenY * 10


            print(f'mes = {mes}')

            print(f'aantal rollen= {row}')

            print(f'totaal van lijst is {totaal} en het gemiddelde over {aantal_banen} banen is {opb}')

            print(f'kleinste rol {min_waarde}, de afwijking van het gemiddelde is {afwijkings_waarde}')

            #todo explore pprint en jinja2 for summary
            csv_builder.summary_file("result", ordernummer,
                                     mes,
                                     row,
                                     totaal,
                                     ongeveer_per_baan,
                                     afwijkings_waarde,
                                     inloop,
                                     name_file_in,
                                     etikettenY,
                                     aantal_vdps)

            # begin stappenplan stap 0  afwijking berekenaar splitter

            # stap 2 splitter
            print("--.--" * 20)
            print(" door splitter gemaakte csv files")

            csv_builder.splitter(name_file_in,
                                 aantal_banen,
                                 afwijkings_waarde,
                                 totaal,
                                 aantal_rollen,
                                 ongeveer_per_baan,
                                 pad_tmp)

            print("--.--" * 20)

            # stap 3 kijk of aantal in lijsten overeenkomt met gevraagde aantal banen

            map_tmp = sorted(Path(pad_tmp).glob('*.csv'))
            maplengte = len(map_tmp)
            check_1 = csv_builder.check_map_op_mes(mes,
                                                   maplengte,
                                                   min_waarde,
                                                   file_in,
                                                   aantal_banen,
                                                   afwijkings_waarde)
            if check_1 is not True:
                sg.popup("niet gemaakt teveel of te weinig , stel met afwijking bij")
                print("message")

            else:
                print("banenbuilder begin")
                # maak met de files uit tmp samengevoegde banen in csv , probleem hier is de kolommen
                # todo kolommen zelfde als in da_remark
                csv_builder.banen_builder(map_tmp, pad_tmp, pad_vdps,wikkel, extra_etiketten)
                print("banenbuilder klaar")

                # verzamel de gemaakte csv's uit de vdps map in deze lijst
                vdps = csv_builder.lijstmaker_uit_posixpad_csv(pad_vdps)

                #  maak een lijst in lijst voor als er meer vdps gemaakt moeten worden.
                print(f"aantal VDP's {aantal_vdps}")
                lijst_tmp2 = csv_builder.lijst_opbreker(vdps, mes, aantal_vdps)

                print(f'lijst_tmp2  is lijsten in lijst! = {lijst_tmp2}')

                input_lijst = sorted(csv_builder.lijst_opbreker(lijst_tmp2, mes, aantal_vdps))


                builder.horizontaal_samenvoegen(lijst_tmp2, VDP_map, mes, ordernummer)



                lijst_uit_vdp_map = csv_builder.lijstmaker_uit_posixpad_csv(VDP_map)
                print("1")
                csv_builder.wikkel_n_baans_tc(lijst_uit_vdp_map, etikettenY, inloop, mes, result)
                print("2 inloop uitloop")
                # todo fine tune in uit

                result_map = csv_builder.lijstmaker_uit_posixpad_csv(result)
                print("3 file naar result zonder NAN")
                builder.end_result_csv(result_map, mes)


                # todo summary  output hier


                key_in_values_as_string =['ordernummer_1',
                                          'mes',
                                          'vdp_aantal',
                                          'afwijkings_waarde',
                                          'Y_waarde',
                                          'Browse',
                                          'overlevering_pct',
                                          'ee',
                                          'wikkel']

                values_to_use_in_summary = []
                for key in key_in_values_as_string:
                    values_to_use_in_summary.append(values[key])

                sum_values = dict(zip(key_in_values_as_string,values_to_use_in_summary))

                csv_builder.html_sum_form_writer(ordernummer,**sum_values)

                summary = [x for x in
                           os.listdir(pad_tmp)
                           if x.endswith(".csv")]
                print(f'lijst ={summary}')

                verticale_summary(summary, mes, result, ordernummer, aantal_vdps)

                #laatste regels lost alles op in zoutzuur:)
                # for key, schoon_pad in paden_dict.items():
                #     print(f'{key} is nu leeg')
                #     cleaner(schoon_pad)

                dir_names_lijst_to_be_cleaned = ["tmp","VDP_map","vdps","stapel","summary","tmp2"]  # "vdps"

                cleaning_paden_met_Dir_lijst = [Path(wdir, dirnaam) for dirnaam in dir_names_lijst_to_be_cleaned]

                for file_pad in cleaning_paden_met_Dir_lijst:
                    cleaner(file_pad)

                # for file_pad in cleaning_paden_met_Dir_lijst:
                #     file_pad.rmdir()

    window.close()



