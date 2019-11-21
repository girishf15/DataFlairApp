from django.shortcuts import redirect
from django.http import HttpResponse

from django.views.decorators.cache import cache_page

@cache_page(200)
def index(request):
    return HttpResponse("<h1>Data Flair Django</h1>Hello, you just configured your First URL")


#cookie
@cache_page(200)
def setcookie(request):

    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")

    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html = HttpResponse("<h1>Welcome Back</h1>")
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = 'Welcome for the First Time'
        html = HttpResponse("<h1>{}</h1>".format(text))
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)

    return html

#The cache_page() method takes in one argument, the expiration\
#time of cache data. The value is in seconds and we have given 200 in the above example.
@cache_page(200)
def showcookie(request):

    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')

#cookie sesssion
def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response


#seesssion based
def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")

def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"

    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('createsession/')

def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")
