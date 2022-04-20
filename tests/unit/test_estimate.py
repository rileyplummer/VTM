import app

def test_add_inputs(height, radius):
    """
    GIVEN a user enters the radius and height
    WHEN the function calculates using these amounts
    THEN the total cost is calculated

    """
    assert app.add_inputs(360,180) == 141300

