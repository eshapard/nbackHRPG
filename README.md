nbackHRPG
=========

A simple script to integrate Brain Workshop (a python dual n-back game) with HabitRPG.


Prerequisites
=============

This script rewards your HabitRPG account for every 100 trials completed in Brain Workshop.

1. HabitRPG.com
2. http://brainworkshop.sourceforge.net/

Installation
============

Install nbackHRPG.py and nbackHRPG.conf to the brainworkshop directory; the same directory where you'll find brainworkshop.pyw

Next edit the nbackHRPG.conf file to update your HabitRPG user id and api token.

This next bit is the tricky part. You'll need to edit whatever script you use to launch Brain Workshop so that it runs 'python nbackHRPG.py' after running Brain Workshop.

In Linux, this can easily be done with the following launch file:

#!/bin/bash
export DISPLAY=:0.0
cd $(dirname $0)
python brainworkshop.pyw
python nbackHRPG.py
exit

For Windows, you'll have to install python and then install the win32 source installation of brainworkshop. Then you can create a batch file. The one below will probably work, but I haven't tested it.

start /wait cmd /C "c:\path\to\python.exe brainworkshop.pyw"
c:\path\to\python.exe nbackHRPG.py
