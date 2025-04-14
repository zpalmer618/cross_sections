import math

res_range = [
(1.66, 3.17, 2700),
(4.885, 5.751, 3630),
(5.634, 6.632, 3620),
(6.408, 7.524, 3590),
(7.477, 8.765, 3520),
(8.711, 10.228, 3290),
(10.017, 11.753, 3250),
(11.481, 13.441, 3010),
(13.319, 15.592, 2370),
(15.4, 18.072, 2470),
(17.651, 20.938, 1460),
(20.417, 24.22, 1680),
(23.884, 28.329, 1630),
]

# This function loads the frequencies and intensities from a file
# and returns them as two separate lists.
# The input file should contain a frequency and an intensity separated by whitespace.

# This function is the refactored version of the original code that 
# provides helpful error messages when the input file is not formatted correctly.
# It also counts the line numbers to provide more context in the error message.
def load_freqs(filename):
    list_freq = []
    list_int = []
    with open(filename, 'r') as infile:
        for lineno, line in enumerate(infile, start=1):
            parts = line.strip().split()
            if len(parts) != 2:
                print(f"Error: Input file '{filename}' is not formatted correctly on line {lineno}.")
                print("Each line should contain a frequency and an intensity separated by whitespace.") 
                exit(1)
            # The following if statement is not necessary given the above 'if not' statement.
            # It is left here to remind me later.
            #if len(parts) == 2:
            freq, intensity = map(float, parts)
            list_freq.append(freq)
            list_int.append(intensity)
        return list_freq, list_int

# TO-DO: Check if the frequencies have associated resolutions. 
# If not, print a warning message on the line where the resolution is missing.
# This will likely require 'major' refactoring to thake the list_micron for loop
# and convert it into a function that accepts frequencies as an argument.
def get_R(wavelength: float, ranges: list[tuple[float, float, float]]) -> float | None:
    for low, high, res in ranges:
        if low <= wavelength <= high:
            return float(res)
    return None

wave_to_mu = 10000.0

list_freq, list_int = load_freqs('freqs.inp')

list_micron = []
for freq in list_freq:
    micron = wave_to_mu / freq
    list_micron.append(micron)

# The error message that prints at the bottom will likely change soon.
# I need to follow the above TO-DO and check if the frequencies have associated resolutions.
list_del_lambda = []
for micron in list_micron:
    R = get_R(micron, res_range)
    if R is not None:
        del_lambda = wave_to_mu * (R / micron)
        list_del_lambda.append(del_lambda)
    else:
        print(f"Warning: No resolution found for wavelength {micron} micron.")
        print(f"If this is a mistake, double check the input file and try again.")

list_epmax = []
for del_lambda, intensity in zip(list_del_lambda, list_int):
    epmax = 27.648 * (intensity / del_lambda)
    list_epmax.append(epmax)

list_acs = []
for epmax in list_epmax:
    acs = (math.log(10) * (1000 / 6.022E23)) * epmax
    list_acs.append(acs)

print('Frequency (cm\u207b\u00b9)', '=', 'Absorption Cross Section (cm\u00b2/molecule)')
for i, j in zip(list_freq, list_acs):
    print(f'{i} = {j:.1e}')

# The following is the blocks of old code that have been
# refactored into functions.

#list_freq = []
#list_int = []
#with open('freqs.inp', 'r') as infile:
#    frequencies = infile.readlines()
#    for freq in frequencies:
#        freq = freq.strip().split()
#        list_freq.append(float(freq[0]))
#        list_int.append(float(freq[1]))

# Three-phase plan:
# 1. run any test, unrelated to the current code
#def test_passes():
#    got = abs(-1)
#    want = 1
#    assert got == want
#
#def test_fails():
#    assert True
## 2. run a test on this code
#def test_get_R():
#    got = get_R(7.855, [(7.477, 8.765, 3520)])
#    want = 3520
#    assert got == want
#
#import numpy as np
#
#def test_floats():
#    got = [1/2, 2/3, 4/5]
#    want = [0.5, 0.666666, 0.8]
#    assert np.allclose(got, want, atol=1e-6)
#
#def main():
#    ...
#
#if __name__ == "__main__":
#    main()
## 3. test the whole program