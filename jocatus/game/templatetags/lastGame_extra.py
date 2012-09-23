from django import template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from jocatus.game.models import Game


register = template.Library()

@register.simple_tag
def lastGame_extra():
	_lastG = Game.objects.all()
	return render_to_response('include/lastGame.html',{'MEDIA_URL':settings.MEDIA_URL ,'lastGames': _lastG })
