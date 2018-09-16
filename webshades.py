#!/usr/bin/env python
import web
import subprocess
urls = (
    '/getbattery/(.*)', 'get_battery',
    '/getposition/(.*)', 'get_position',
    '/moveup/(.*)', 'move_up',
    '/movedown/(.*)', 'move_down',
    '/stop/(.*)', 'move_stop',
    '/setposition/(.*)/(.*)', 'set_position'
)
app = web.application(urls, globals())
class get_battery:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/home/pi/webshades/control.py', '-t', mac, '-c', 'get_battery'])
        output = output.replace("get_battery ", "").replace("\n","")
        return output
class get_position:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/home/pi/webshades/control.py', '-t', mac, '-c', 'get_position'])
        output = output.replace("get_position ", "").replace("\n","")
        output = abs(int(output) - 100)
        return output
class move_down:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/home/pi/webshades/control.py', '-t', mac, '-c', 'move_down'])
        return "OK"
class move_up:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/home/pi/webshades/control.py', '-t', mac, '-c', 'move_up'])
        return "OK"
class move_stop:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/home/pi/webshades/control.py', '-t', mac, '-c', 'move_stop'])
        return "OK"
class set_position:
    def GET(self, mac, position):
        position = abs(100 - int(position))
        output = subprocess.check_output(['/usr/bin/python','/home/pi/webshades/control.py', '-t', mac, '-c', 'move_target', '-a', str(position)])
        return "OK"
if __name__ == "__main__":
    app.run()
