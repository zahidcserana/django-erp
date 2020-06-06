from django.shortcuts import redirect
from django.urls import resolve


class CheckUser(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_name = resolve(request.path).url_name
        # print(request.session['username'])
        if 'username' in request.session:
            response = self.get_response(request)
            return response
        elif url_name == 'loginpage':
            if 'username' in request.session:
                return redirect("dashboard_index")
            response = self.get_response(request)
            return response
        else:
            return redirect("loginpage")
