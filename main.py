from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
  body="This is a test message from Python and twilio API, all i say is that i am a python developer and i love python",
  from_=keys.twilio_number,
  to=keys.target_number
)

print(message.sid)