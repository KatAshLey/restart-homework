Based on testing_apis_pt2 homework last week

1) convert 'client = TestClient(app)' into a test fixture to run with a fresh instance of the app in each new case

2) Use @pytest.mark.parametrize() to test your GET API, in different scenario where you get 200 or 404 codes

3) Add another input for @pytest.mark.parametrize() to compare GET response json payload