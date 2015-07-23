import random
import string
import test_m

import cherrypy
import time



class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        op1 = """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" name = "name"/>
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

        return op1

    @cherrypy.expose
    def generate(self,name=None):
        # return "Your Unique number is:" + str(random.randint(1000000000000,9999999999999999))
        print "Hello %s" %name
        try:
          return str(test_m.train(int(name)))[1:-1].replace('"','').replace(',',' ')
        except:
          print "Error!Bad Request"


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
