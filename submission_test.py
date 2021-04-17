import import_ipynb
import nb_gen
import pytest

# Test hello world function
@pytest.mark.hello_world
def test_hello_world():
    assert nb_gen.hello_world() == "Hello, world!"

# Test factorial function
@pytest.mark.factorial
@pytest.mark.parametrize(["in_val", "out_val"], [(0, 1), (4, 24), (10, 3628800)])
def test_factorial(in_val, out_val):
    assert nb_gen.factorial(in_val) == out_val