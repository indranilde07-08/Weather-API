import requests
from send_email import send_email

topic ="India"
api = "9e1012dac9664e739a3300c0e340a1cf"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2025-03-01&sortBy=publishedAt&apiKey=" \
      "9e1012dac9664e739a3300c0e340a1cf&language=en"

# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
# Access the article titles and description

message_list = []

for article in content["articles"][:20]:
    messages = f" {article['title']}\n\n{article['description']}\n \n {article['url']}\n"
    message_list.append(messages)
# convert list to string
message= "Subject: Today's Top 20 News \n\nHere are today's top 20 article\n\n"+"\n".join(message_list)
print("Sending Email with message:\n", message)
send_email(message=message)
