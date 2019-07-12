import platform
import socket
import os
import win32api
import win32profile

print "Using platform.node(): %s" % platform.node()
print "Using socket.gethostname(): %s" % socket.gethostname()
print "Using os.environ['COMPUTERNAME']: %s" % os.environ['COMPUTERNAME']
print "Using win32api.GetComputerName(): %s" % win32api.GetComputerName()

WIN32_ComputerNameDnsHostname = 1 
print "Using win32api.GetComputerNameEx(WIN32_ComputerNameDnsHostname): %s" % win32api.GetComputerNameEx(WIN32_ComputerNameDnsHostname)

env = win32profile.GetEnvironmentStrings()
print "Using win32profile.GetEnvironmentStrings()['COMPUTERNAME']: %s" % env['COMPUTERNAME']
