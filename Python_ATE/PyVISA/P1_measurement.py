"""
P1 measurement
Set sig gen to 0dbm
read pm
increase sig gen to 10dbm
repeat until P1 point identified
reduce sig gen 10 db, measure pm to identify power drop of 9 db
set sig gen up 20 db, repeate p1 test.
once P1 found increment in 1 db steps until a 9 db drop (P1) occures.
return P1 measurement and sig gen setting.

"""
import Automating_RFTests
import pyvisa
from quantiphy import Quantity
from time import sleep
# get sig gen address
addr_SG = 'The address of the sig gen in use'
addr_pm = 'The address of the power meter in use'
# Example for ethernet pwr_supply = rm.open_resource('TCPIP::192.168.128.24::INSTR')
# to get a list of stuff on the net use rm.list_resources()

rm_sig_gen = pyvisa.SGconnection(addr_SG)
"""mp_sig_gen = rm_sig_gen.open('ASRL/dev/ttyUSB0')
mp_sig_gen.baud_rate = 115200
print(mp_sig_gen.query("*IDN?"))"""

rm_pm = pyvisa.PMconnection(addr_pm)
PM = rm_pm.open_resource('TCPIP::192.168.12.24::INSTR') # connects resource manager to the LAN port
#mp_pm = rm_pm.open('ASRL/dev/ttyUSB0')
#mp_pm.baud_rate = 11520
PM.baud_rate = 11520
print(PM.query("*IDN?"))
while True:
    print(Quantity(mp_pm.query('MEAS?').strip(), "Ohms"))
    sleep(1)
    # Connect to the Spectrum Analyzer
    sa = pyvisa.instrument("GPIB0::23")

    # Set the frequency range
    sa.write("SENS:FREQ:START 100MHz")
    sa.write("SENS:FREQ:STOP 1GHz")

    # Perform a single sweep, need in while loop to make measurement
    sa.write("INIT:IMM")

    # Get the trace data
    trace_data = sa.query("TRACE:DATA?")

    # Close the connection
    sa.close()