def test_add_inputs(app,client):
    """
    GIVEN a user enters the radius and height
    WHEN the function calculates using these amounts
    THEN the total cost is calculated
    """
    with app.test_client() as test_client:
        # pass in the data use Chrome Developer Tools -> Network -> Click on page -> Payload
        calculate = {"radius":"180", "height":"360"} 
        res = test_client.post('/add_inputs', data=calculate)
        assert res.status_code == 200 
        assert b"141300.00000000003" in res.data 
