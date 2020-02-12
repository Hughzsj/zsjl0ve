from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(request):
	is_login = request.session.get('login')
	if not is_login:
		# return redirect('/web/login/')
		return render(request,'./home/home_t.html')
	username = request.session.get('user')
	return render(request,'./home/home_t.html',{'name':username})
	# return render(request,'base.html')

def login(request):
	if request.method == 'GET':
		return render(request,'./account/login.html')
	else:		
		user = request.POST.get('user')
		password = request.POST.get('password')
		if user == 'hugh' and password == '123':
			request.session['login'] = True
			request.session['user'] = user
			return redirect('/web/index/')
			# return HttpResponse('ok')
		else:
			return HttpResponse('error')