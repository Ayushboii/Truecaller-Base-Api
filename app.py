from flask import Flask, request, Response
import requests

app = Flask(__name__)

TC_URL = "https://search5-noneu.truecaller.com/v2/search"
TC_HEADERS = {
    "User-Agent": "Truecaller/16.7.8 (Android;15)",
    "Accept": "*/*",
    "Accept-Encoding": "identity",   # 🔥 IMPORTANT
    "authorization": "Bearer a2i0s--yWJylvVeF5FNGuh_MJUR2txVpAypP6YUD8otXzdsGeFywFDMok8-DqMou"
}

@app.route("/raw")
def raw():
    number = request.args.get("number")
    if not number:
        return "missing number", 400

    r = requests.get(
        TC_URL,
        params={
            "q": number,
            "countryCode": "IN",
            "type": 4,
            "encoding": "json"
        },
        headers=TC_HEADERS,
        timeout=10
    )

    # 🔥 REMOVE problematic headers
    headers = {}
    if "content-type" in r.headers:
        headers["Content-Type"] = r.headers["content-type"]

    return Response(
        r.content,
        status=r.status_code,
        headers=headers
    )

if __name__ == "__main__":
    app.run()
