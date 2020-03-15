from django.http import HttpResponse
from .models import User, Issue
import json

def set_urls(request):
	return "success"
	request = json.loads(request)
	text = request['result']['text']
	chat_id = request['result']['chat']['id']

	if text.startswith('/start'):
		return msg_start(chat_id)
	if text.startswith('/stop'):
		return msg_stop(chat_id)
	if text.startswith('/delete'):
		return msg_delete(chat_id)

	return HttpResponse("info")



def msg_start(chat_id):
	user = User.objects.filter(id=chat_id)

	if user:
		user = user[0]
		user.status = True
		user.save()
	else:
		User.objects.create(id=chat_id)

	return HttpResponse("docs")

def msg_stop(chat_id):
	response = "stop success"

	try:
		user = User.objects.get(id=chat_id)
		user.status = False
		user.save()
	except DoesNotExist as dne:
		response = "doesn't defined user. \nplease send '/start'"
	
	return HttpResponse(response)

def msg_delete(chat_id):
	response = "stop success"

	try:
		user = User.objects.get(id=chat_id)
		user.delete()
	except DoesNotExist as dne:
		response = "not defined user"

	return HttpResponse(response)




def test_api(reuqest):
	return HttpResponse("test_api")
