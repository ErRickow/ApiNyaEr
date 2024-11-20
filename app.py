from flask import Flask, request, jsonify
from ApiNyaEr.apinya import apinya  # Pastikan untuk mengimpor objek apinya

app = Flask(__name__)

@app.route('/api/<method_name>', methods=['GET', 'POST'])
async def api_handler(method_name):
    # Ambil parameter dari permintaan
    params = request.args.to_dict()  # Untuk GET
    if request.method == 'POST':
        params = request.json  # Untuk POST

    # Coba panggil metode yang sesuai dari apinya
    try:
        method = getattr(apinya, method_name)
        if callable(method):
            result = await method(**params)  # Panggil metode dengan parameter
            return jsonify(result)  # Kembalikan hasil sebagai JSON
        else:
            return jsonify({"error": "Method not callable"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()