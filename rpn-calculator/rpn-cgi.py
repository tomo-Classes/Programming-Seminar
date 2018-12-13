import falcon
import json
from r2 import rpn

class RPN:
	def on_get(self, req, res):
		# print(req.get_param("q", True))
		try:
			obj = {
				"result": rpn(req.get_param("q", True))
			}
		except Exception as err:
			obj = {
				"error": str(err)
			}
		res.body = json.dumps(obj, ensure_ascii=False)

app = falcon.API()
app.add_route("/", RPN())

if __name__ == "__main__":
	from wsgiref import simple_server

	httpd = simple_server.make_server("127.0.0.1", 8000, app)
	httpd.serve_forever()
