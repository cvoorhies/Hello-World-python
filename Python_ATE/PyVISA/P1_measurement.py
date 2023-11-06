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
#import Automating_RFTests
import pyvisa
from quantiphy import Quantity
from time import sleep
# get sig gen address
#addr_SG = 'The address of the sig gen in use'
#addr_pm = 'The address of the power meter in use'
# Example for ethernet pwr_supply = rm.open_resource('TCPIP::192.168.128.24::INSTR')
# to get a list of stuff on the net use rm.list_resources()

# Connect to the power meter and signal generator
pm = Pm('GPIB0::16::INSTR') #pyvisa.ResourceManager().open_resource('GPIB0::16::INSTR')
sg = SigGen('GPIB0::16::INSTR') #pyvisa.ResourceManager().open_resource('GPIB0::16::INSTR')
#while True: # Need a condition to run this in ?? steps
print(Quantity(mp_pm.query('MEAS?').strip(), "Ohms"))
sleep(1)
# Get the power measurement
power = pm.query('MEAS:POW?')

# Set the frequency to 1 GHz
sg.write('SOUR:FREQ 1000-000-000')

# Set the power to 10 dBm
sg.write('SOUR:POW 10')

# Turn on the output
sg.write('OUTP ON')

# Generate a signal
sg.write('INIT:IMM')

# Get the power measurement
power = pm.query('MEAS:POW?')

# Set the power to -10 dBm
sg.write('SOUR:POW -10')
sleep(1)

powerdelta = 10
lastPwrdg = 0
pwrSetVar = 0
while(powerdelta <=9):
    lastPwrdg = pm.query('MEAS:POW?') # expect reading to start at -10dbm, then increase by 10.
    
    pwset = f'SOUR:POW {pwrSetVar}'
    sg.write(pwset)
    sleep(1)
    power = pm.query('MEAS:POW?') # expect reading to be 0dbm on first round. increment by 10 after.
    powerdelta = power - lastPwrdg
    pwrSetVar += 10

# Get the power measurement
power = pm.query('MEAS:POW?') # expect reading to be -10dbm

# Set the power to 20 dBm
sg.write('SOUR:POW 20')
sleep(1)
# Set the power to 10 dBm 
sg.write('SOUR:POW 10')
sleep(1)
# Get the power measurement, 9db drop?? repeat if not.
power = pm.query('MEAS:POW?') # expect reading to be 10dbm

# Set the power to 30 dBm
sg.write('SOUR:POW 30')
sleep(1)
# Set the power to 20 dBm
sg.write('SOUR:POW 20')
sleep(1)
# Get the power measurement, 9db drop?? repeat if not.
power = pm.query('MEAS:POW?') # expect reading to be 20dbm

# Set the power to 40 dBm
sg.write('SOUR:POW 40')
sleep(1)
# Set the power to 30 dBm
sg.write('SOUR:POW 30')
sleep(1)
# Get the power measurement, 9db drop?? repeat if not.
power = pm.query('MEAS:POW?') # expect reading to be ~29dbm or less.


# Close the connection to the Signal Generator
sg.close()

# Close the connection to the Power Meter
pm.close()