from flask import Flask


class Server:
    app = Flask("python")

    def run(self):
        self.app.run(
            debug=True,
        )


server = Server()
