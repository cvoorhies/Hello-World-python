"""
Equipment needed
oscilloscope
power supply
noise source, with PS. Some times the SA will have a NS option

the effect of the device under test (DUT) input matching (usually due to inconsistent LNA
 values) and lower accuracy at higher frequencies make the Y-factor technique a poor candidate
 for testing noise above 18 GHz (K-Band).

"""

import numpy as np

def y_factor_noise_figure(y_factor, noise_source_temperature):
  """
  Calculates the noise figure of a device under test (DUT) using the Y-factor method.

  Args:
    y_factor: The Y-factor, which is the ratio of the output noise power of the DUT when the noise source is turned on to the output noise power of the DUT when the noise source is turned off.
    noise_source_temperature: The temperature of the noise source in Kelvin.

  Returns:
    The noise figure of the DUT in decibels (dB).
  """

  # Calculate the noise figure in decibels.
  noise_figure_db = 10 * np.log10(y_factor - 1) + 290 / noise_source_temperature

  return noise_figure_db


# Example usage:

# Measure the Y-factor using a noise figure meter.
y_factor = 1.5

# Calculate the noise figure using the Y-factor method.
noise_source_temperature = 290  # Kelvin

noise_figure_db = y_factor_noise_figure(y_factor, noise_source_temperature)

print("The noise figure of the DUT is {} dB.".format(noise_figure_db))