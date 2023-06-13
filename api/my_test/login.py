from http.server import BaseHTTPRequestHandler
from urllib import parse
 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    url_path=self.path
    url_components=parse.urlsplit(url_path)
    query_list=parse.parse_qsl(url_components)
    my_dict=dict(query_list)
    name=my_dict.get('name')
    if name:
        message= f"welcome {name}"
    else:
         message= f"welcome man!"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return