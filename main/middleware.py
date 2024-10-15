from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings
import re

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [re.compile(settings.LOGIN_URL.lstrip('/'))]
        if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
            self.exempt_urls += [re.compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

    def __call__(self, request):
        path = request.path_info.lstrip('/')

        if not request.user.is_authenticated:
            if not any(m.match(path) for m in self.exempt_urls):
                # Reverse the LOGIN_URL to get the correct URL
                login_url = reverse(settings.LOGIN_URL)
                return redirect(login_url)
        return self.get_response(request)
