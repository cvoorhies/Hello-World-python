################################################################################
# © Keysight Technologies 2016
#
# You have a royalty-free right to use, modify, reproduce and distribute
# the Sample Application Files (and/or any modified version) in any way
# you find useful, provided that you agree that Keysight Technologies has no
# warranty, obligations or liability for any Sample Application Files.
#
################################################################################

import pyvisa
import sys

class ATE_test:

    def __init__(self, Visa_Add):
        # Change this variable to the address of your instrument
        self.VISA_ADDRESS = Visa_Add

    try:
        # Create a connection (session) to the instrument
        resourceManager = pyvisa.ResourceManager('@py')
        session = resourceManager.open_resource(VISA_ADDRESS)
    except pyvisa.Error as ex:
        print('Couldn\'t connect to \'%s\', exiting now...' % VISA_ADDRESS)
        sys.exit()

    # For Serial and TCP/IP socket connections enable the read Termination Character, or read's will timeout
    if session.resource_name.startswith('ASRL') or session.resource_name.endswith('SOCKET'):
        session.read_termination = '\n'

    # Send *IDN? and read the response
    session.write('*IDN?')
    idn = session.read()

    print('*IDN? returned: %s' % idn.rstrip('\n'))

    # Close the connection to the instrument
    session.close()
    resourceManager.close()

    print('Done.')

    def exceptionHandler(exception):

        print('Error information:\n\tAbbreviation: %s\n\tError code: %s\n\tDescription: %s' % \
            (exception.abbreviation, exception.error_code, exception.description))


    # Change this variable to the address of your instrument
    VISA_ADDRESS = 'Your instruments VISA address goes here!'

    # Part 1:
    #
    # Shows the mechanics of how to deal with an error in PyVISA when it occurs.
    # To stimulate an error, the code will try to open a connection to an instrument at an invalid address...
    #
    # First we'll provide an invalid address and see what error we get

    resourceManager = pyvisa.ResourceManager('@py')

    try:
        session = resourceManager.open_resource("BAD ADDRESS")
    except pyvisa.VisaIOError as ex:
        print('VISA ERROR - An error has occurred!\n')

        # To get more specific information about the exception, we can check what kind of error it is and
        # add specific error handling code. In this example, that is done in the exceptionHandler function
        exceptionHandler(ex)

        # Part 2:
        #
        # Stimulate another error by sending an invalid query and trying to read its response.
        #
        # Before running this part, don't forget to set your instrument address in the 'VISA_ADDRESS'
        # variable at the top of this script

        session = resourceManager.open_resource(VISA_ADDRESS)

        # Misspell the *IDN? query as *IND?
        try:
            session.write('*IND?')
        except visa.VisaIOError as ex2:
            print(
                'VISA ERROR - You\'ll never get here, because the *IND? data will get sent to the instrument successfully, '
                'it\'s the instrument that won\'t like it.')

        # Try to read the response (*IND ?)
        try:
            idnResponse = session.read()
            print('*IDN? returned: %s\n' % idnResponse)
        except visa.VisaIOError as ex3:
            print('VISA ERROR - The read call will timeout, because the instrument doesn\'t'
                ' know what to do with the command that we sent it.')

        # Check the instrument to see if it has any errors in its queue
        rawError = ''
        errorCode = -1

        while errorCode != 0:
            session.write('SYST:ERR?')
            rawError = session.read()

            errorParts = rawError.split(',')
            errorCode = int(errorParts[0])
            errorMessage = errorParts[1].rstrip('\n')

            print('INSTRUMENT ERROR - Error code: %d, error message: %s' % (errorCode, errorMessage))

        # Close the connection to the instrument
        session.close()
        resourceManager.close()

        print('Done.')

        ################################################################################
    # © Keysight Technologies 2016
    #
    # You have a royalty-free right to use, modify, reproduce and distribute
    # the Sample Application Files (and/or any modified version) in any way
    # you find useful, provided that you agree that Keysight Technologies has no
    # warranty, obligations or liability for any Sample Application Files.
    #
    ################################################################################

    def find(searchString):

        resourceManager = pyvisa.ResourceManager('@py')

        print('Find with search string \'%s\':' % searchString)
        devices = resourceManager.list_resources(searchString)
        if len(devices) > 0:
            for device in devices:
                print('\t%s' % device)
        else:
            print('... didn\'t find anything!')

        resourceManager.close()


    # Finding all devices and interfaces is straightforward
    print('Find all devices and interfaces:\n')
    find('?*')

    # You can specify other device types using different search strings. Here are some common examples:

    # All instruments (no INTFC, BACKPLANE or MEMACC)
    find('?*INSTR')
    # PXI modules
    find('PXI?*INSTR')
    # USB devices
    find('USB?*INSTR')
    # GPIB instruments
    find('GPIB?*')
    # GPIB interfaces
    find('GPIB?*INTFC')
    # GPIB instruments on the GPIB0 interface
    find('GPIB0?*INSTR')
    # LAN instruments
    find('TCPIP?*')
    # SOCKET (::SOCKET) instruments
    find('TCPIP?*SOCKET')
    # VXI-11 (inst) instruments
    find('TCPIP?*inst?*INSTR')
    # HiSLIP (hislip) instruments
    find('TCPIP?*hislip?*INSTR')
    # RS-232 instruments
    find('ASRL?*INSTR')

    print('Done.')

    ################################################################################
    # © Keysight Technologies 2016
    #
    # You have a royalty-free right to use, modify, reproduce and distribute
    # the Sample Application Files (and/or any modified version) in any way
    # you find useful, provided that you agree that Keysight Technologies has no
    # warranty, obligations or liability for any Sample Application Files.
    #
    ################################################################################

       # Change VISA_ADDRESS to a serial VISA address, e.g. 'ASRL2::INSTR'
    VISA_ADDRESS = 'Your instruments VISA address goes here!'

    try:
        # Create a connection (session) to the serial instrument
        resourceManager = pyvisa.ResourceManager('@py')
        session = resourceManager.open_resource(VISA_ADDRESS)

        # For Serial and TCP/IP socket connections enable the read Termination Character, or read's will timeout
        if session.resource_name.startswith('ASRL') or session.resource_name.endswith('SOCKET'):
            session.read_termination = '\n'

        # If you've setup the serial port settings in Connection Expert, you can remove this section.
        # Otherwise, set your connection parameters
        session.set_visa_attribute(pyvisa.constants.VI_ATTR_ASRL_BAUD, 9600)
        session.set_visa_attribute(pyvisa.constants.VI_ATTR_ASRL_DATA_BITS, 8)
        session.set_visa_attribute(pyvisa.constants.VI_ATTR_ASRL_PARITY, visa.constants.VI_ASRL_PAR_NONE)
        session.set_visa_attribute(pyvisa.constants.VI_ATTR_ASRL_FLOW_CNTRL, visa.constants.VI_ASRL_FLOW_DTR_DSR)

        # Send the *IDN? and read the response
        session.write('*IDN?')
        idn = session.read()

        print('*IDN? returned: %s' % idn.rstrip('\n'))

        # Close the connection to the instrument
        session.close()
        resourceManager.close()

    except pyvisa.Error as ex:
        print('An error occurred: %s' % ex)

    print('Done.')

#Creating an instance of itself so that it can be called and used 
#in the measurement files.
class VNA(ATE_test):
    def __init__(self, args):
        super().__init__(self, args)
        self.address = args
    def connection():
        instrument = self.resourceManager.list_resources()
        for inst in instrument:
            if(inst.startswith('USB')):
                this_resource = rm.open_resource(inst)
                this_resource.query_delay = 0.1 # some things like a pause
                print(f"\nTrying {inst}")
            try:
                print(this_resource.query("*IDN?"),strip())
            except Exception as e:
                print(e)
            this_resource.close()
    
    pass

class SpecA(ATE_test):
    def __init__(self, args):
        super().__init__(self, args)
        self.address = args
    pass

class SigGen(ATE_test):
    def __init__(self, args):
        super().__init__(self, args)
        self.address = args
    pass
class Pm(ATE_test):
    def __init__(self, args):
        super().__init__(self, args)
        self.address = args
    pass