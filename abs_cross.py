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

def get_R(wavelength, ranges):
    for low, high, res in ranges:
        if low <= wavelength <= high:
            return float(res)
    return None

wave_to_mu = 10000.0

list_freq = []
list_int = []
with open('freqs.inp', 'r') as infile:
    frequencies = infile.readlines()
    for freq in frequencies:
        freq = freq.strip().split()
        list_freq.append(float(freq[0]))
        list_int.append(float(freq[1]))

list_micron = []
for freq in list_freq:
    micron = wave_to_mu / freq
    list_micron.append(micron)

list_del_lambda = []
for micron in list_micron:
    R = get_R(micron, res_range)
    if R is None:
        print(f"Warning: No resolution found for wavelength {micron} micron.")
        continue
    del_lambda = wave_to_mu * (R / micron)
    list_del_lambda.append(del_lambda)

list_epmax = []
for del_lambda, intensity in zip(list_del_lambda, list_int):
    epmax = 27.648 * (intensity / del_lambda)
    list_epmax.append(epmax)

list_acs = []
for epmax in list_epmax:
    acs = (math.log(10) * (1000 / 6.022E23)) * epmax
    list_acs.append(acs)

for i in list_acs:
    print(f'{i:.1e}')