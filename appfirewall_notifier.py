import gntp as gntp
import gntp.notifier
import time

"""
Monitors the Application Firewall log for changes and sends a popup when they occur.  
TODO set a rate limit
Requires the Growl Application and gntp
http://growl.info
https://pypi.python.org/pypi/gntp/1.0.2
enable the growl notify server and configure your firewall settings.  
the notify server can run in host only mode.  
"""
# More complete example
growl = gntp.notifier.GrowlNotifier(
    applicationName = "AppFirewall.log",
    notifications = ["Inbound Alert"],
    defaultNotifications = ["Inbound Alert"],
    # hostname = "computer.example.com", # Defaults to localhost
    # password = "abc123" # Defaults to a blank password
)
growl.register()
def gnotify(Title, Description):
    image = open('/Users/jesse/Documents/dev/shortcuts/Zim.png', 'rb').read()
    growl.notify(
    noteType = "Inbound Alert",
    title = Title,
    description = Description,
    icon = image,
)
while True:
    with open('/var/log/appfirewall.log','rb') as log_lines:
        log_lines=log_lines.readlines()
        print(len(log_lines))
        time.sleep(15)
    with open('/var/log/appfirewall.log', 'rb') as log_lines_step:
        log_lines_step=log_lines_step.readlines()
        if len(log_lines_step) > len(log_lines):
            new_lines_index=len(log_lines_step)-len(log_lines)
            #print new_lines_index
            #print log_lines_step
            if new_lines_index>5:
                gnotify('Incident Alert!!', '%s events in last 15 seconds.')
                new_lines_index=5
            change_index=range(1,new_lines_index+1)
            change_index.reverse()
            for num in change_index:
                gnotify('Firewall Alert', log_lines_step[-num])
        else:
            print('no change')