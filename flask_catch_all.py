from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    print('\n\n==== NEW CONNECTION ====\n', request.headers)
    if request.method == 'POST':
        return {'ip': request.headers.get('X-Real-IP', '127.0.0.1'),
		'path': path,
		'json': request.get_json(),
		'form': request.form.to_dict(),
		'data': json.loads(request.data, encoding='utf8')
		}, 201
    else:
        return {'ip': request.headers.get('X-Real-IP', '127.0.0.1'),
		'path': path,
		'args': request.args.to_dict()
		}, 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)


