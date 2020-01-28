from django.shortcuts import render, redirect
from .forms import restrev
from .apps import PredConfig

def index(request):
	if request.method == 'POST':
		form = restrev(request.POST)
		if form.is_valid():
			rev = request.POST.get('review')
			cv = PredConfig.countvec.transform([rev]).toarray()
			response = PredConfig.classifier.predict(cv)
			return render(request, 'pred/predvalue.html', {'response': response})
	else:
		form = restrev()
	return render(request, 'pred/predictor.html', {'form':form})