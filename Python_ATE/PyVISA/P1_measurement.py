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
rm_sig_gen = pyvisa.SigGen(addr_SG)
mp_sig_gen = rm_sig_gen.open('ASRL/dev/ttyUSB0')
mp_sig_gen.baud_rate = 115200

rm_pm = pyvisa.PM(addr_pm)
mp_pm = rm_pm.open('ASRL/dev/ttyUSB0')
mp_pm.baud_rate = 11520
print(mp_pm.query("*IDN?"))
while True:
    print(Quantity(mp_pm.query('MEAS?').strip(), "Ohms"))
    sleep(1)

