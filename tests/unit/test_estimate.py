import app 


def test_add_inputs(app, client):
    """
    GIVEN a user enters the radius and height
    WHEN the function calculates using these amounts
    THEN the total cost is calculated
    """
    print(" -- add_inputs unit test")
    assert app.add_inputs(180,360) == 141300.00000000003
