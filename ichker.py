import urllib
import os
import time
import sys
from datetime import datetime
from subprocess import call

url = 'https://www.google.com' # Set desired page to test connection
device = 'YOUR_ETHERNET_INTERFACE' # Change it to your ethernet interface, can be shown when you type 'ifconfig' in terminal

def ichker():
    fail_count = 0 # Initialize failure count by 0
    while True:
        for i in xrange(300, 0, -1): # For 300 seconds waiting...to prevent annoying server
            time.sleep(1)
            sys.stdout.write('\r')
            sys.stdout.write('%03d' % (i))
            sys.stdout.flush()
        try:            
            urllib.urlopen(url)
        except:
            print '' # Make log every time the connection fails...
            log_file = open('/YOUR_DESIRED_PATH/DESIRED_FILE_NAME.txt', 'a+') # Change the log file path to your own
            fail_count += 1
            dateandtime = datetime.today().strftime('%Y/%m/%d %H:%M:%S') # Get exact time and date
            print 'Connection failed!! Restarting network...'
            print 'Fail count : ' + str(fail_count)
            to_write = 'Connection failed at ' + dateandtime + '\n'
            log_file.write(to_write)
            if_down = 'ifconfig ' + device + ' down' # eth down(disconnect) command
            if_up = 'ifconfig ' + device + ' up' # eth up(reconnect) command
            call(if_down, shell=True) # Execute the eth down command in terminal
            call(if_up, shell=True) # Execute the eth up command in terminal
            log_file.close()

print 'Connection checking has started...'
ichker()
