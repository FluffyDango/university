from flask import jsonify, request
import os
from dotenv import load_dotenv

def init_routes(app):
    @app.route('/api/hello', methods=['GET'])
    def hello_world():
        return jsonify({'message': 'Hello, World!'})

    @app.route('/api/echo', methods=['POST'])
    def echo():
        data = request.json
        return jsonify({'you sent': data}), 200
    
    @app.route('/api/compare-image', methods=['POST'])
    def compare_image():
        from .image_comparison.SSIM import use_ssim
        use_ssim()
        return jsonify({'message': 'Image comparison complete!'}), 200
