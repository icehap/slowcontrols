##run once on startup

##can check current configs with crontab -l

##this adds processes to the local cron
##these will run periodically, automatically

import sys, os
from crontab import CronTab
import datetime

def new_cron(cron, cmnd, time, freq):
    job = cron.new(command = cmnd)
    print("--- Confirgure the Job ---")
    print(job)
    if time not in ["min", "hour"]:
        raise ValueError
    if time is "min":
        job.every(freq).minutes()
    if time is "hour":
        job.every(freq).hours()
    print("--- Scheduling the Job ---")
    #job.enable()
    if job.is_valid() == False:
        print("SlowMon Couldn't Start...")
        cron.remove(job)
        raise IOError
    cron.write()
    #cron.remove_all()
    print("--- List of all Cron Jobs ---")
    print(cron)
    return cron

def restart_cron(cron):
    print("Removing all cron jobs...")
    # cron = CronTab(user='icehap-daq')
    cron.remove_all()
    #cron.write()
    print("icehap-daq user cron empty..")
    return cron

def start_cron():
    cron = CronTab(user='icehap-daq')
    print("Starting SlowMon...")
    return cron

def inspect_cron(cron):
    for job in cron:
        print(f"--- Job {job} ---")
        sch = job.schedule(date_from=datetime.datetime.now())
        print("Next Run Time: ", sch.get_next())

if __name__ == '__main__':
    cron = start_cron()
    print("Adding jobs to cron...")

    cron = new_cron(cron, 'python3 /home/icehap-daq/dvt/crontab/check_cron.py', "hour", 2)
    cron = new_cron(cron, 'python3 /home/icehap-daq/software/goldschmidt/goldschmidt/record_temp.py /dev/ttyUSB1 1 2 3 4 /home/icehap-daq/software/goldschmidt/goldschmidt/temp.csv', "min", 10)
    cron = new_cron(cron, 'python3 /home/icehap-daq/software/check_disk/slow_disk_check.py / /home/icehap-daq/software/check_disk/disk_space.csv', "min", 30)
    cron = new_cron(cron, 'python3 /home/icehap-daq/software/plotting/temperature_plot.py', "hour", 2)
    cron = new_cron(cron, 'python3 /home/icehap-daq/software/plotting/slow_disk_plot.py', "hour", 2)
    cron = new_cron(cron, 'python3 /home/icehap-daq/dvt/crontab/push_update.py', "hour", 4)
    cron = new_cron(cron, 'python3 /home/icehap-daq/dvt/crontab/backup_cron.py', "hour", 24)

    inspect_cron(cron)

    ##write the cron
    #cron.write()

##end