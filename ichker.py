import urllib
import os
import time
import sys
from datetime import datetime
from subprocess import call

url = 'https://www.google.com' # Set desired page to test connection
device = 'YOUR_ETHERNET_INTERFACE' # Change this parameter to your ethernet interface, can be shown when you type 'ifconfig' in terminal
log_file_path = '/YOUR_DESIRED_PATH/DESIRED_FILE_NAME.txt' # Set your log file path here... 

def ichker(chk_interval, log):
    drop_count = 0 # Initialize drop count by 0
    while True:
        for i in xrange(chk_interval, 0, -1): # 'chk_interval' seconds for waiting...to prevent annoying server
            time.sleep(1)
            sys.stdout.write('\r')
            sys.stdout.write('%03d' % (i))
            sys.stdout.flush()
        try:            
            urllib.urlopen(url) # Connection check
        except:
            print '' # Make log every time the connection drops...
            log_file = open(log, 'a+')
            drop_count += 1
            dateandtime = datetime.today().strftime('%Y/%m/%d %H:%M:%S') # Get exact time and date
            print 'Connection dropped!! Restarting network...'
            print 'Drop count : ' + str(drop_count)
            to_write = 'Connection dropped at ' + dateandtime + '\n'
            log_file.write(to_write)
            if_down = 'ifconfig ' + device + ' down' # eth down(disconnect) command
            if_up = 'ifconfig ' + device + ' up' # eth up(reconnect) command
            call(if_down, shell=True) # Execute the eth down command in terminal
            call(if_up, shell=True) # Execute the eth up command in terminal
            log_file.close()

print 'Connection checking has started...'
ichker(300, log_file_path)
