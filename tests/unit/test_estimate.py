from pickletools import read_unicodestring1
import app 


def test_add_inputs():
    """
    GIVEN a user enters the radius and height
    WHEN the function calculates using these amounts
    THEN the total cost is calculated
    """
    radius = 180
    height = 360
    assert app.add_inputs() == 141300.00000000003