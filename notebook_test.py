import import_ipynb
import nb_gen
import pytest

# Test function on some values
@pytest.mark.parametrize(["in_val", "out_val"], [(0, 1), (4, 24), (1, 1)])
def test_function(in_val, out_val):
    assert nb_gen.factorial(in_val) == out_val