from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
def bot():
    # Get user message
    user_msg = request.values.get('Body', '').strip().lower()

    # Prepare the response
    response = MessagingResponse()

    # Formulate search query
    query = user_msg + " site:geeksforgeeks.org"

    # Store search results
    results = []
    try:
        for url in search(query, num_results=3):
            results.append(url)
    except Exception as e:
        response.message("Error while searching: " + str(e))
        return str(response)

    # Reply with search results
    if results:
        response.message(f"🔍 Top results for: *{user_msg}*")
        for url in results:
            response.message(url)
    else:
        response.message("❌ No results found. Try asking differently.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
