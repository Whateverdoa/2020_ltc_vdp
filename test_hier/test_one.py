import pytest
from source.paden import paden_dict
from source.messen import read_out_2
from source.functions import (print_trespa_rolls,
                              splitter,
                              check_map_op_mes,
                              banen_builder)


test_file_in = ""


def test_splitter():
    split =  splitter(test_file_in,8,10,10000,10,1000,pad)


def test_checkmapenmes():
    pass


def test_trespa_rolls():

    assert 1 ==2


def test_banenbuilder():

    assert 2==2

