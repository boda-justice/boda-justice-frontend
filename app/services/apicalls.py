import json
import requests
from flask import jsonify

def template_error(response):
  print(response)
  return {
    "error": "Something went wrong",
    "status_code": response.status_code
  }

class Request():
  def __init__(self, **kwargs):
    self.host = 'https://boda-justice.herokuapp.com'
    self.endpoint = kwargs['endpoint']
    self.data = kwargs['data'] 
    self.headers = kwargs['headers']
    self.url = self.host + self.endpoint

  def post(self):
    response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data))
    return response._content

  def get(self):
    response = requests.get(self.url, headers=self.headers)
    print(response._content)
    return response._content
  
  def put(self):
    response = requests.put(self.url, headers=self.headers, data=json.dumps(self.data))
    return response._content
