import requests

api = "9e1012dac9664e739a3300c0e340a1cf"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2025-02-07&sortBy=publishedAt&apiKey=" \
      "9e1012dac9664e739a3300c0e340a1cf"

# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
