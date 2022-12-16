## **_*Testing using Pytest*_**

- Created a global fixture auth_client that returns a function, if that function is passed a user instance, it'll return an
  instance of DRF's APIClient authenticated by that user instance, otherwise, it'll return an instance of APIClient
  authenticated by an arbitrary user instance

  - [see conftest.py](/conftest.py)

<br/>

- Used pytest to implement my test cases
  - ![Here is a screenshot](/users/tests.png)
