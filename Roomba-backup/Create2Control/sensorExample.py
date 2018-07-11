import create2api
import json   # We'll use this to format the output
import threading
import time

def timelimit(timeout, func, args=(), kwargs={}):
    """ Run func with the given timeout. If func didn't finish running
        within the timeout, raise TimeLimitExpired
    """
    class FuncThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None
            
        def run(self):
            self.result = func(*args, **kwargs)

    it = FuncThread()
    it.start()
    it.join(timeout)
    if it.isAlive():
        return False
    else:
        return True


i = 1
while i < 7:


    bot = create2api.Create2()

    bot.start()
    bot.safe()

    timelimit(2, bot.get_packet, (100, ), {})

    print '==============Start Up Data=============='
    #print json.dumps(bot.sensor_state, indent=4)

    print '========================================='
    print ''

    #Packet 100 contains all sensor data.
    #bot.get_packet(100)

    print '==============Updated Sensors=============='
    #print json.dumps(bot.sensor_state, indent=4, sort_keys=False)

    print str(bot.sensor_state['oi mode']) + " " + str(bot.sensor_state['voltage'])
    i+=1

    #bot.SCI.Close()
    bot.destroy()
    print "Pausing for 1 sec"
    time.sleep(1)


bot = create2api.Create2()
bot.start()
