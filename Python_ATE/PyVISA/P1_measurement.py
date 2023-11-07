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

def P1meas(cntrF):
    # Connect to the power meter and signal generator
    pm = pyvisa.ResourceManager('GPIB0::16::INSTR') #pyvisa.ResourceManager().open_resource('GPIB0::16::INSTR')
    sg = pyvisa.ResourceManager('GPIB0::18::INSTR') #pyvisa.ResourceManager().open_resource('GPIB0::16::INSTR')
    #while True: # Need a condition to run this in ?? steps
    print(Quantity(mp_pm.query('MEAS?').strip(), "Ohms"))
    sleep(1)
    # Get the power measurement
    power = pm.query('MEAS:POW?')

    freqset = f'SOUR:FREQ {cntrF}'
    # Set the frequency to 1 GHz
    sg.write(freqset)

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

    power -= 10  # Set to a 10 db backoff
    powerdelta = 10
    pwset = f'SOUR:POW {power}'
    sg.write(pwset)
    sleep(1)
    # repeat after 10 db backoff and increment by 1
    while(powerdelta <=9):
        lastPwrdg = pm.query('MEAS:POW?') # expect reading to start at -10dbm, then increase by 10.
        
        pwset = f'SOUR:POW {pwrSetVar}'
        sg.write(pwset)
        sleep(1)
        power = pm.query('MEAS:POW?') # expect reading to be 0dbm on first round. increment by 10 after.
        powerdelta = power - lastPwrdg
        pwrSetVar += 1
        
        sg.write('SOUR:POW 1') # set back to p1 then measure
        power = pm.query('MEAS:POW?')
        return power
    # Close the connection to the Signal Generator
    sg.close()

        # Close the connection to the Power Meter
    pm.close()

result = P1meas(8000000000)
print(result)