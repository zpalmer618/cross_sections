from abs_cross import get_R
from abs_cross import load_freqs
from abs_cross import get_wavelength
import pytest

# Three-phase plan:
# 1. run any test, unrelated to the current code
def test_passes():
    got = abs(-1)
    want = 1
    assert got == want


# 2. run a test on this code
def test_get_R():
    got = get_R(7.855, [(7.477, 8.765, 3520)])
    want = 3520
    assert got == want

# 3. test the whole program
#def main(): ...
#
#
#if __name__ == "__main__":
#    main()