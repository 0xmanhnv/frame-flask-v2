from flask import Blueprint, jsonify
api_v1 = Blueprint('api',__name__)

@api_v1.route('/test')
def index():
	return jsonify({
		'error' : False,
		'msg':'success'
	}), 200