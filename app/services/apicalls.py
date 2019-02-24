import json
import requests

def template_error(response):
  print(response)
  return {
    error: "Something went wrong",
    status_code: response.status_code
  }

class Request():
  def __init__(self, **kwargs):
    self.host = 'https://boda-justice.herokuapp.com'
    self.endpoint = kwargs['endpoint']
    self.data = kwargs['data'] 
    self.headers = kwargs['headers']
    self.url = self.host + self.endpoint

  def post(self):
    response = requests.post(self.url, headers=self.headers, data=self.data)
    if response.status_code >= 400:
      return template_error(response)
    return json.loads(response.text)

  def get(self):
    response = requests.get(self.url, headers=self.headers)
    if response.status_code >= 400:
      return template_error(response)
    return json.loads(response.text)
  
  def put(self):
    response = requests.put(self.url, headers=self.headers)
    if response.status_code >= 400:
      return template_error(response)
    return json.loads(response.text)
