import config
from twilio.rest import TwilioRestClient


def call(number)
	TWILIO_PHONE_NUMBER = config.phone_number
	DIAL_NUMBERS = [number]
	TWIML_INSTRUCTIONS_URL = \
  		"http://static.fullstackpython.com/phone-calls-python.xml"
	client = TwilioRestClient(config.sid, config.auth_token)
	dial_numbers(DIAL_NUMBERS, TWILIO_PHONE_NUMBER, TWIML_INSTRUCTIONS_URL)

def dial_numbers(numbers_list, TWILIO_PHONE_NUMBER_PARAM, TWIML_INSTRUCTIONS_URL_PARAM):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER_PARAM,
                            url=TWIML_INSTRUCTIONS_URL_PARAM, method="GET")