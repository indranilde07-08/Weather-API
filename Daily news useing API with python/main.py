import requests
from send_email import send_email

api = "9e1012dac9664e739a3300c0e340a1cf"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2025-02-07&sortBy=publishedAt&apiKey=" \
      "9e1012dac9664e739a3300c0e340a1cf"

# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
# Access the article titles and description

message = ""

for article in content["articles"]:
    message = f"Subject: {article['title']}\n\n{article['description']}"
    print("Sending Email with message:\n", message)

send_email(message)
