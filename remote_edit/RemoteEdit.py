import subprocess
from pyngrok import ngrok
import argparse


class RemoteEdit:

    def __init__(self, path, port, username, password):
        self.path = path
        self.port = port
        self.username = username
        self.password = password



    def ngrok_connect(self):
        ngrok.connect(self.port)
        tunnels = ngrok.get_tunnels()
        public_url = tunnels[0].public_url
        print(public_url)
        ngrok_process = ngrok.get_ngrok_process()
        flaskcode_cmd= 'flaskcode '+ self.path + ' --username ' + self.username + ' --password '+ self.password
        print(self.path)
        subprocess.run(flaskcode_cmd, shell=True)
        try:
            # Block until CTRL-C or some other terminating event
            ngrok_process.proc.wait()
        except KeyboardInterrupt:
            print(" Shutting down server.")
            ngrok.kill()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "--Path", help="Show Path")
    parser.add_argument("--o", "--Output", help="Show Output")
    parser.add_argument("--username", "--Username", help="Username")
    parser.add_argument("--password", "--Password", help="Password")
    parser.add_argument("--port", "--port", default=5001, help="Port")
    args = vars(parser.parse_args())
    path = args['path']
    port = args['port']
    username = args['username']
    password = args['password']
    remote_edit = RemoteEdit(path, port, username, password)
    remote_edit.ngrok_connect()

