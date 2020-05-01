from source.functions import print_trespa_rolls, lijst_opbreker
import pytest


lijst_in_test =[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

def test_print_trespa_rolls():
    roltest = print_trespa_rolls("color", "mooiman", 12,"pad", )
    assert roltest == 2




def test_lijst_opbreker():
    expected = 1
    gebroken_lijst = lijst_opbreker(lijst_in_test,3,1)
    assert gebroken_lijst == expected



def test_false():
    assert 1== 2