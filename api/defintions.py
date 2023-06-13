from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    list_of_dif=[]


    url_path=self.path
    url_components=parse.urlsplit(url_path)
    query_list=parse.parse_qsl(url_components)
    my_dict=dict(query_list)

    if 'word' in my_dict:
      word=my_dict.get('word')
      url='https://restcountries.com/v3.1/capital/'
      res=requests.get(url+word)
      data=res.json()
    self.wfile.write(list_of_dif.encode())
    return