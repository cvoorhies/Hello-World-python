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
import pyvisa
from quantiphy import Quantity
from time import sleep


def P1meas(lowf=1000000000, cntrF=1500000000, highf=2000000000):
    freqList = [lowf, cntrF, highf]
    # Connect to the power meter and signal generator
    pm = pyvisa.ResourceManager('GPIB0::16::INSTR') #pyvisa.ResourceManager().open_resource('GPIB0::16::INSTR')
    sg = pyvisa.ResourceManager('GPIB0::18::INSTR') #pyvisa.ResourceManager().open_resource('GPIB0::16::INSTR')
    #while True: # Need a condition to run this in ?? steps
    print(Quantity(mp_pm.query('MEAS?').strip(), "Ohms"))
    sleep(1)
    for feq in freqList:
        # Get the power measurement
        power = pm.query('MEAS:POW?')

        freqset = f'SOUR:FREQ {freq}'
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
            print(Quantity(mp_pm.query('MEAS?').strip(), "Ohms"))
            power = pm.query('MEAS:POW?')
            return power
        
        # Close the connection to the Signal Generator
        sg.close()

            # Close the connection to the Power Meter
        pm.close()

result = P1meas(8000000000, 8500000000, 9000000000)
print(result)