# cross_sections
This script calculates absorption cross sections using anharmonic vibrational frequencies (cm<sup>-1</sup>) and infrared (IR) intensities (km/mol), providing a semi-quantitative observable that is more relevant to astronomy than to spectroscopy.

The calculation of absorption cross sections are based on a document by [Spanget-Larson](https://www.researchgate.net/publication/279441865_Infrared_Intensity_and_Lorentz_Epsilon_Curve_from_'Gaussian'_FREQ_Output) and [Wikipedia](https://en.wikipedia.org/wiki/Absorption_cross_section).

## Usage
```
python abs_cross.py freqs.inp
```

# Input/Output
This is the example input from [freqs.inp](freqs.inp): 
```
3441.7 12
3364 1
1526 43
739.5 107
450 1
423.1 163
```
The first column shows frequencies in cm<sup>-1</sup> and the second column shows IR intensities in km/mol.

The output absorption cross sections are printed to the screen as follows, again for [freqs.inp](freqs.inp):
```
Frequency (cm⁻¹) = Absorption Cross Section (cm²/molecule)
3441.7 = 1.4e-25
3364.0 = 1.2e-26
1526.0 = 8.2e-25
739.5 = 6.5e-24
450.0 = 1.4e-25
423.1 = 2.4e-23
```