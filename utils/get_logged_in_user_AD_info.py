import commands
import os

user = os.getenv('USER').decode('utf-8')

try:
    cmd = "dscl /Active\ Directory/ -read . SubNodes"
    ret, subnode = commands.getstatusoutput(cmd)
    print "Subnode: %s" % subnode
    if subnode and not ret:
        if "No such key" in subnode:
            subnode=""
        subnode = subnode.lstrip('SubNodes:')[1:]
    else:
        print "Unable to get subnodes in active directory for user %s, error %d" % (user, ret)
except Exception, fault:
    print "Error: %s" % str(fault)

try:
    cmd_userinfo = 'dscl /Active\ Directory/"%s"/All\ Domains/ -read /Users/"%s"' %(subnode, user)
    ret, userinfo = commands.getstatusoutput(cmd_userinfo)
    print "userinfo: %s" % userinfo
    if ret:
        print "Unable to get userinfo in active directory for user %s, command error %d" % (user, ret)
except Exception, fault:
    #status = str(fault)
    print "Unable to get userinfo in AD for user %s. Error: %s. Using cached credentials", user, str(fault)

try:
    cmd_ad_info = "dsconfigad -show | awk '/Active Directory Domain/{print $NF}'"
    ret, adinfo = commands.getstatusoutput(cmd_ad_info)
    print "adinfo: %s" % adinfo
    if ret:
        print "The Mac is not bound to domain"
except Exception, fault:
    print "Error in check domain. %s" % str(fault)

print "Current logged-in user details: %s" % str(commands.getstatusoutput('id -u %s' % user))
