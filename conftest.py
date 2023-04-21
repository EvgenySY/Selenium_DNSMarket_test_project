import pytest



@pytest.fixture(scope="module")
def set_group():
    print("\n ----------\n Start Test \n")
    yield
    print(" \n Need phone number verification \n Test Finished \n ----------")
