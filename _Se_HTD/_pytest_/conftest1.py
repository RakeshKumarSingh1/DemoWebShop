import pytest


@pytest.fixture(autouse="True",scope="class")
def greet():
    print("****hi****") #set up module
    yield
    print("***Bye***") #teardown module

@pytest.mark.usefixtures("greet")
class TestDemo:
    def test_spam(greet):
     print("in test spam")

    def test_display(greet):
     print("in display")
