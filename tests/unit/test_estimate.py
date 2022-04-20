import app

def test_add_inputs(radius,height):
    """
    GIVEN a user enters the radius and height
    WHEN the function calculates using these amounts
    THEN the total cost is calculated

    """
    assert app.add_inputs(180,360) == 141300.00000000003

