from django.shortcuts import redirect
from django.urls import resolve


class CheckUser(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_name = resolve(request.path).url_name
        # print(request.user.is_authenticated)
        if request.user.is_authenticated:
            response = self.get_response(request)
            return response
        elif url_name == 'loginpage':
            if request.user.is_authenticated:
                return redirect("dashboard_index")
            response = self.get_response(request)
            return response
        else:
            return redirect("loginpage")
