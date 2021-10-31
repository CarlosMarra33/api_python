from src.server.instance import server
from src.controllers import products_controller
# print("teste main")
app = server.app
server.run()