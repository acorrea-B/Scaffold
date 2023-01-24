from hello import subtract
from hello import toyou
from hello import add


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


##un to see failed test
#def test_hello_add():
    #assert add(test_hello_add.x) == 12

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9

def test_hello_add():
    assert add(test_hello_add.x) == 11

def test_hello_to_you():
    assert toyou(test_hello_to_you.x) == "hi 10"