import time
import numpy as np
from gpiozero import MCP3008

#designates the pins
chtemp = MCP3008(channel=0, clock_pin=11, mosi_pin=10,miso_pin=9, select_pin=8)

tsample = 0.5 #how often to get data
tdisp = 1 #how often to display data
tstop = 20 #how long data should be gathered
vref = 3.3 #voltage used
ktemp = 13 #

tprev = 0
tcurr = 0
tstart = time.perf_counter()

print('Running code for', tstop, 'seconds...')
while tcurr <= tstop:
    tcurr = time.perf_counter() - tstart
    valuecurr = chtemp.value
    tempcurr = vref*ktemp*valuecurr
    if (np.floor(tcurr/tdisp) - np.floor(tprev/tdisp)) == 1:
        print("Temperature = {:d} deg C".format(int(np.round(tempcurr))))
    tprev = tcurr

print('Done.')
#releases pins
chtemp.close()
