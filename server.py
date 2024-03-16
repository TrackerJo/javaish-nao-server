 #Python 3 server example
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SimpleHTTPServer
# from naoqi import ALProxy
import SocketServer


import time




# Import Module

import urllib


 



port = 465  # For SSL

hostName = "10.100.27.192"
serverPort = 8080

usingRobot = True

class MyServer(SimpleHTTPRequestHandler):
    def load_binary(filename):
        with open(filename, 'rb') as file_handle:
            return file_handle.read()
        
    def do_GET(self):

        self.send_response(200)
        
        # self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:5500")
        
        paths = self.path.split("/")
        
        if paths[1] == "run_file":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            fileName = paths[2]
            execute(open( fileName + ".py").read())
            self.wfile.write(bytes("file ran", "utf-8"))
        if paths[1] == "run_string":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Split the encoded string into components
            components = paths[2].split("+")

            # Decode each component and join them back into a string
            decoded_string = " ".join(urllib.unquote(component) for component in components)
   
            print(decoded_string)
            execute(decoded_string)
            self.wfile.write(bytes("string ran"))
def execute(string):
    exec(string)
if __name__ == "__main__":        

    httpd = SocketServer.TCPServer(("", serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped.")
