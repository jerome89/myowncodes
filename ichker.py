import urllib
import threading
import os
import time
import sys
from datetime import datetime
from subprocess import call

url = 'https://www.google.com'
device = 'enp3s0'

def ichker():    
    fail_count = 0
    while True:
        for i in xrange(300, 0, -1):
            time.sleep(1)
            sys.stdout.write('\r')
            sys.stdout.write('%03d' % (i))
            sys.stdout.flush()
        try:
            #print ''
            urllib.urlopen(url)
        except:
            print ''
            log_file = open('/home/jerome/.ichkerlog.txt', 'a+')
            fail_count += 1
            dateandtime = datetime.today().strftime('%Y/%m/%d %H:%M:%S')
            print 'Connection failed!! Restarting network...'
            print 'Fail count : ' + str(fail_count)
            to_write = 'Connection failed at ' + dateandtime + '\n'
            log_file.write(to_write)
            if_down = 'ifconfig ' + device + ' down'
            if_up = 'ifconfig ' + device + ' up'
            call(if_down, shell=True)
            call(if_up, shell=True)
            log_file.close()

print 'Connection checking has started...'
ichker()
