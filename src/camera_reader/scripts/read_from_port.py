#!/usr/bin/env python

## Driver for reading from port

import sys
import rospy
import serial
from std_msgs.msg import Header
    
# Example for data parser
    '''
    def parseData(datum,verbose,seq=0):
        # Buffer return values
        dataval1 = np.array([nan, nan, nan])
        checksum = 'nan'
        success  = False
        # Parsing
        try:
            # Split fields
            fields = datum.split(',')
            # Checksum
            laststr  = fields[-1].split('*')
            checksum = '*' + laststr[1]
            lastval  = laststr[0]
            # Data Value 1
            dataval1[0] = float(fields[1])
            dataval1[1] = float(fields[2])
            dataval1[2] = float(fields[3])
            # Success indicator flag
            success = True
        except:
            print('\tcamera_reader/read_from_port/parseData: FAILED TO READ #%d' %(seq))
            success = False
        # Return
        return dataval1, checksum, success
    '''
    
# Example for unit testing data parser
    '''
    def test_parseData(verbose=True,tol=0.01):
        # Test inputs
        inputs = ['Datum1',
                  'Datum2']
        # True values [DATAVAL1 (units), CHECKSUM]
        truths = [[ 0, 0, 0, '*xx'],
                  [ 0, 0, 0, '*xx']]
        # Run
        isAllGood = True
        testNames = ['Test 1', 'Test 2']
        if verbose:
            print('\tChecking parseData...')
        for i in range(len(testNames)):
            iIn  = inputs[i]
            dataval1, checksum, success = parseVnymr(iIn)
            iOut = [dataval1[0], dataval1[1], dataval1[2], 
                    checksum]
            jOut = truths[i]
            isOutGood = True
            for j in range(len(iOut)):
                isOutGood = isOutGood and (abs(iOut[j] - jOut[j]) <= tol)
            if verbose:
                if isOutGood:
                    print("\tPASS: " + testNames[i] + " is OK")
                else:
                    print("\tFAIL: " + testNames[i] + " is NOT OK")
                print("\t  Got:      [%.2f, %.2f, %.2f, %s]" %(iOut[0], iOut[1],  iOut[2],
                                                               iOut[3]))
                print("\t  Expected: [%.2f, %.2f, %.2f, %s]" %(jOut[0], jOut[1],  jOut[2],
                                                               jOut[3]))
            isAllGood = isAllGood and isOutGood
        # Result
        return isAllGood
    '''
    
if __name__ == '__main__':
    # Display initialization
    pkgname  = 'camera_reader'
    exename  = 'read_from_port'
    nodestr  = '/%s/' %(pkgname) # use this to name node
    topicstr = 'imu'
    datastr  = '' # string of data header type, e.g. VNYMR (IMU) or GPGGA (GPS)
    # Input parsing
    print('%s: Running %s...' %(pkgname, exename))
    argList = ['port']
    argDefault = ['fakeport']
    arg = [[]]*len(argList) # buffer
    if nodestr + argList[0] in rospy.get_param_names(): # e.g. if run with roslaunch
        print('\tExisting node found!' %(dispstr))
        for i in range(len(argList)):
            arg[i] = rospy.get_param(nodestr + argList[i])
            print('\t\tSet %s to %s' %(argList[i],arg[i]))
    elif (len(sys.argv) == 2): # e.g. if run with rosrun + 1 input value
        arg[0] = sys.argv[1]
        for i in range(1,len(argList)):
            arg[i] = argDefault[i]
    else: # script initialized with rosrun without args
        print('\t(ERROR) Need to provide a value for ''port''' %(pkgname, exename))
        1/0
    # Input arg values
    port = arg[0]
    # Main processing
    try:
        # Publishing node
        rospy.init_node(nodestr, anonymous=True)
        camPub = rospy.Publisher(topicstr, Header, queue_size=10) # Header for now; change this later
        # Data buffer
        head = Header()
        head.frame_id = "CAM_Frame"
            #camData = cam_msg()
        # Port initialization
        serial_port = rospy.get_param('~port',port)
        serial_baud = rospy.get_param('~baudrate',4800)
        portOpen = serial.Serial(serial_port, serial_baud, timeout=2.)
        # Read-in
        print('\t##### BEGIN DATA READ #####')
        while not rospy.is_shutdown():
            line = portOpen.readline().strip().decode()
            fields = line.split(',')
            if datastr in fields[0]:
                # Header
                head.seq += 1
                head.stamp = rospy.Time.now()
                    #camData.Header = head
                # Parsing
                    # TBD
                # Data fields
                    # TBD
                # Publishing
                    # TBD
                    #camPub.publish(camData)
    except rospy.ROSInterruptException:
        portOpen.close()
        pass