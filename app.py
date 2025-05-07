from flask import Flask, jsonify, render_template
import socket
from data import obtener_pokenea_aleatoria

app = Flask(__name__)

@app.route("/pokenea-json")
def pokenea_json():
    pokenea = obtener_pokenea_aleatoria()
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": socket.gethostname()
    })

@app.route("/pokenea-imagen")
def pokenea_imagen():
    pokenea = obtener_pokenea_aleatoria()
    return render_template("pokenea_imagen.html", pokenea=pokenea, contenedor_id=socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
