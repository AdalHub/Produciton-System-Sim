from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory orders storage
orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders}), 200

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order_id = len(orders) + 1
    order = {
        "order_id": order_id,
        "item": data.get("item", "Unknown"),
        "quantity": data.get("quantity", 1),
        "status": "processing"
    }
    orders.append(order)
    return jsonify({"message": "Order created", "order": order}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
