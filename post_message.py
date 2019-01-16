import requests

params = {
  'author': 'kenni',
  'text': 'This is a really good message.',
}

requests.post('http://localhost:5005/api/actions/message', params=params)
