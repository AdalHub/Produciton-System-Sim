from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample content data
content = {
    1: {"title": "Welcome to our site", "body": "This is the first piece of content."},
    2: {"title": "Latest Update", "body": "Here is the latest news update."}
}

@app.route('/content/<int:content_id>', methods=['GET'])
def get_content(content_id):
    item = content.get(content_id)
    if item:
        return jsonify({"content": item}), 200
    else:
        return jsonify({"error": "Content not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5002)
