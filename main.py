from src.server.instance import server
from src.controllers import products_controller, user_controller
app = server.app
server.run()