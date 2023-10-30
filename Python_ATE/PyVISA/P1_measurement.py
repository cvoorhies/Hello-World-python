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
import visa
# get sig gen address
addr_SG = 'The address of the sig gen in use'
addr_pm = 'The address of the power meter in use'
rm_sig_gen = visa.SigGen(addr_SG)
rm_pm = visa.PM(addr_pm)
