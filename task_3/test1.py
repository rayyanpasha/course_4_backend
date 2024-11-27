import requests
def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandboxbc647ea749c44d70844c2102fecb0b17.mailgun.org/messages",
  		auth=("api", "f7380d544b07d7f83488128ad0e6fe21-c02fd0ba-aee54ce3"),
  		data={"from": "Excited User <mailgun@sandboxbc647ea749c44d70844c2102fecb0b17.mailgun.org>",
  			"to": ["kshitiz.t@atriauniversity.edu.in"],
  			"subject": "Hello",
  			"text": "Testing some Mailgun awesomeness!"})

send_simple_message()