from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm
from django import forms
from jocatus.game.models import Game
from django.conf import settings

class SearchForm(forms.Form):
	search = forms.CharField(max_length = 100)
	
def searchGame(request):
	if request.method =='POST':
		searchForm= SearchForm(request.POST)
		if searchForm.is_valid():
			search = searchForm.cleaned_date['search']
			_searchGame = Game.objects.get(headline__contains=search)
			return render('library_game.html',{'library_games' :_searchGame})
			#return render_to_response ('library_game.html',{'library_games' :_searchGame}, context_instance=RequestContext(request))
	else:
		searchForm = SearchForm()
	#return render_to_reponse('index.html',{'search':search,}, context_instance=RequestContext(request))
	return render('{{ request.get_full_path }}',{'search' :searchForm})
		
		

def index(request):
	return render_to_response('index.html')

def game(request, game):
	if game:
		_game= Game.objects.filter(name=game)
		return render_to_response('game.html',{'MEDIA_URL':settings.MEDIA_URL,'games':_game})
	
def library_game(request): # TODO rajouter un offset sur la liste
	_library_game = Game.objects.all()
	return render_to_response ('library_game.html',{'library_games':_library_game})	
