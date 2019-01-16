from flask import Flask, request, jsonify

app = Flask('necssus-bot')

@app.route('/neccsus/command', methods=['GET', 'POST'])
def command():
  message = dict(request.values)

  author = message.get('author')
  text = message.get('text')

  if 'vs' in text:
    reply = {
      'author': 'necssus-bot',
      'text': f'Which is better?',
      'attachments': [{
        'title': 'A poll',
        'actions': [{
          'type': 'buttons',
          'options': [{
            'name': 'best-option',
            'text': option.strip(),
            'value': option.strip(),
          } for option in text.split('vs')],
        }],
      }],
    }
  else:
    reply = {
      'author': 'necssus-bot',
      'text': f'Nice one, {author}. You sent a message with {len(text.split())} words.',
      
    }

  return jsonify(reply)

@app.route('/neccsus/interactivity', methods=['GET', 'POST'])
def interactivity():
  params = request.values

  reply = {
    'author': 'necssus-bot',
    'text': f'You said {params["best-option"]!r} was the best.',
  }

  return jsonify(reply)

if __name__ == '__main__':
  app.run(debug=True)
