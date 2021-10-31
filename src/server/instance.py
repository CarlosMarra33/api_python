from flask import Flask
# from flask_restx import Api

class Server():
    app = Flask("python")

    def run(self):
        self.app.run(
            debug=True,
        )
server = Server()
