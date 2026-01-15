from flask import Flask, request, Response
import requests

app = Flask(__name__)

TC_URL = "https://search5-noneu.truecaller.com/v2/search"
TC_HEADERS = {
    "User-Agent": "Truecaller/16.7.8 (Android;15)",
    "Accept": "*/*",
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

    # 🔥 EXACT upstream response
    return Response(
        r.content,                      # binary/text jo bhi ho
        status=r.status_code,
        headers={
            "Content-Type": r.headers.get("content-type", "text/plain")
        }
    )

if __name__ == "__main__":
    app.run()
