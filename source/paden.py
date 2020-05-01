""""this module generates the directories and paths """

from pathlib import Path

wdir = Path.cwd()

# lijst met variable namen om naar de paden te verwijzen
pad_naam_lijst = ["pad_sum",
                  "pad_tmp",
                  "pad_tmp2",
                  "pad_file_in",
                  "pad_naar_vdps",
                  "stapel",
                  "VDP_map"]
print(pad_naam_lijst)
# lijst met alle te gebruiken directories
dir_names_lijst = ["summary",
                   "tmp",
                   "tmp2",
                   "file_in",
                   "vdps",
                   "stapel",
                   "VDP_map"]

# list comprehension om alle paden te maken
paden_met_dir_lijst = [Path(wdir, dirnaam) for dirnaam in dir_names_lijst]

# list comprehension om alle Directories naar de paden te maken
dir_maak_comp_lijst = [dir_to_build.mkdir(parents=True, exist_ok=True) for dir_to_build in paden_met_dir_lijst]

# dict voor snel opzoeken paden
paden_dict = dict(zip(pad_naam_lijst,paden_met_dir_lijst))

print(paden_dict)



def cleaner(pad):

    dir_to_empty = sorted(Path(pad).glob('*.csv'))

    for file in dir_to_empty:
        file.unlink()
        # pad.rmdir()  # test of dit werkt eerst csv weg dan dir

    return 0

list_of_files_to_clean = ["tmp", "summary"]

cleaner(paden_dict["pad_tmp"])
cleaner(paden_dict["pad_naar_vdps"])