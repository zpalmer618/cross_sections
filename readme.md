# cross_sections
This script calculates absorption cross sections using anharmonic vibrational frequencies (cm<sup>-1</sup>) and infrared (IR) intensities (km/mol), providing a semi-quantitative observable that is more relevant to astronomy than to spectroscopy.

The calculation of absorption cross sections are based on a document by [Spanget-Larson](https://www.researchgate.net/publication/279441865_Infrared_Intensity_and_Lorentz_Epsilon_Curve_from_'Gaussian'_FREQ_Output) and [Wikipedia](https://en.wikipedia.org/wiki/Absorption_cross_section).

# Input
This is the example input from [freqs.inp](freqs.inp). The first column shows frequencies in cm<sup>-1</sup> and the second column shows IR intensities in km/mol.
```
3441.7 12
3364 1
1526 43
739.5 107
450 1
423.1 163
```