from flask import Flask, jsonify, request
from card import MetroCard

app = Flask(__name__)

card = MetroCard(0)


@app.route('/purchase', methods=['POST'])
def purchase_card():
    amount = request.json.get('amount')
    try:
        card.purchase_card(amount)
        return jsonify({'message': 'Card purchased successfully!'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/top-up', methods=['POST'])
def top_up_card():
    amount = request.json.get('amount')
    try:
        card.top_up_card(amount)
        return jsonify({'message': 'Card topped up successfully!'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/fare', methods=['POST'])
def calculate_fare():
    station_count = request.json.get('station_count')
    try:
        fare = card.calculate_fare(station_count)
        return jsonify({'fare': fare})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/deduct-fare', methods=['POST'])
def deduct_fare():
    fare = request.json.get('fare')
    try:
        card.deduct_fare(fare)
        return jsonify({'message': 'Fare deducted successfully!'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/enter-station', methods=['POST'])
def enter_station():
    try:
        card.enter_station()
        return jsonify({'message': 'Entered the station successfully!'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/exit-station', methods=['POST'])
def exit_station():
    try:
        card.exit_station()
        return jsonify({'message': 'Exited the station successfully!'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/apply-discount', methods=['POST'])
def apply_discount():
    card.station_count = request.json.get('station_count')
    card.apply_discount()
    return jsonify({'message': 'Discount applied successfully!'})


if __name__ == '__main__':
    app.run(debug=True)
