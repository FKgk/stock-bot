from django.shortcuts import render
from .models import User, Issue
import json

def set_urls(request):
	request = json.loads(request)
	text = request['result']['text']
	chat_id = request['result']['chat']['id']

	if text.startswith('/start'):
		msg_start(chat_id)

	pass

def msg_start(chat_id):
	result = User.objects.create(id=chat_id)
	if result:
		result.save()




