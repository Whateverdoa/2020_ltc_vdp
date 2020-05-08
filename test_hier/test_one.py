import pytest
from source.paden import paden_dict
from source.messen import read_out_2
from source.functions import (print_trespa_rolls,
                              splitter,
                              check_map_op_mes,
                              banen_builder,
                              filna_dict,
                              summary_file)
from source.read_out import kol_naam_lijst_builder


test_file_in = ""

def test_kolom_naam_lijst():
    expected = [
            "omschrijving_1",
            "pdf_1",
            "omschrijving_2",
            "pdf_2",
            "omschrijving_3",
            "pdf_3",
        ]
    mes3 = kol_naam_lijst_builder(3)
    assert mes3 == expected

def test_filnadict():
    expected = {"pdf_1": "stans.pdf",
                "pdf_2": "stans.pdf",
                "pdf_3": "stans.pdf"}
    testing_filna_dikt_with = filna_dict(3)
    assert testing_filna_dikt_with == expected

def test_sum_file():
    testlijst = [1, 2, 3, 4, 5, 6, 7]
    twee_args = summary_file("result","esther",*testlijst)

    expected = len(testlijst)
    assert twee_args == expected



