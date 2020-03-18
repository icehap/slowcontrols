import os
import sys
sys.path.append('/home/icehap-daq/dvt/slackbot/')
from chiba_daq_slackbot import send_warning, push_slow_mon

def push_plot(file_path, name):
    try:
        os.path.isfile(file_path)
    except:
        send_warning("@channel Path to slow-mon plot not found:"+file_path)
        return False

    push_slow_mon(file_path, name)
    return True

if __name__ == '__main__':
    temperature_plot = "/home/icehap-daq/software/plotting/recent_temp.png"
    push_plot(temperature_plot, "Freezer Temperature")

    #try to avoid pushing too fast
    time.sleep(5)

    disk_plot = "/home/icehap-daq/software/plotting/recent_disk.png"
    push_plot(disk_plot, "Disk Space")
