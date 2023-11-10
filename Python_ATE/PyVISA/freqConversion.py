import pyvisa

def set_sweep_mode(address, start_frequency, stop_frequency, sweep_time):
  """
  Sets the sweep mode of a Keysight signal generator.

  Args:
    address: The IP address or VISA resource name of the signal generator.
    start_frequency: The start frequency of the sweep in Hz.
    stop_frequency: The stop frequency of the sweep in Hz.
    sweep_time: The sweep time in seconds.
  """

  # Connect to the signal generator.
  rm = pyvisa.ResourceManager()
  sg = rm.open_resource(address)

  # Set the start frequency.
  sg.write(f"OUTP:FREQ:START {start_frequency}Hz")

  # Set the stop frequency.
  sg.write(f"OUTP:FREQ:STOP {stop_frequency}Hz")

  # Set the sweep time.
  sg.write(f"OUTP:SWE:TIME {sweep_time}s")

  # Enable sweep mode.
  sg.write("OUTP:SWE:MODE CONT")


# Example usage:

# Set the sweep mode of the signal generator to sweep from 1 GHz to 2 GHz in 10 seconds.
address = "TCPIP::192.168.1.100::INSTR"
start_frequency = 1e9  # 1 GHz
stop_frequency = 2e9  # 2 GHz
sweep_time = 10  # 10 seconds

set_sweep_mode(address, start_frequency, stop_frequency, sweep_time)

import visa

def set_sweep_mode(address, start_frequency, stop_frequency, sweep_time, span):
    """
    Sets the sweep mode of a Keysight spectrum analyzer.

    Args:
        address: The IP address or VISA resource name of the spectrum analyzer.
        start_frequency: The start frequency of the sweep in Hz.
        stop_frequency: The stop frequency of the sweep in Hz.
        sweep_time: The sweep time in seconds.
        span: The frequency span of the sweep in Hz.
    """

    # Connect to the spectrum analyzer.
    rm = visa.ResourceManager()
    sa = rm.open_resource(address)

    # Set the start frequency.
    sa.write(f"SENS:FREQ:START {start_frequency}Hz")

    # Set the stop frequency.
    sa.write(f"SENS:FREQ:STOP {stop_frequency}Hz")

    # Set the sweep time.
    sa.write(f"SENS:SWE:TIME {sweep_time}s")

    # Set the frequency span.
    sa.write(f"SENS:FREQ:SPAN {span}Hz")

    # Set the sweep mode to continuous.
    sa.write("SENS:SWE:MODE CONT")

    # Enable the sweep.
    sa.write("INIT:CONT ON")


# Example usage:

# Set the sweep mode of the spectrum analyzer to sweep from 1 GHz to 2 GHz in 10 seconds with a frequency span of 100 MHz.
address = "TCPIP::192.168.1.100::INSTR"
start_frequency = 1e9  # 1 GHz
stop_frequency = 2e9  # 2 GHz
sweep_time = 10  # 10 seconds
span = 1e8  # 100 MHz

set_sweep_mode(address, start_frequency, stop_frequency, sweep_time, span)
