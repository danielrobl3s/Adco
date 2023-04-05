from django.middleware.csrf import get_token

class CsrfTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            # Get the CSRF token and add it to the request headers
            csrf_token = get_token(request)
            request.headers['X-CSRFToken'] = csrf_token

        response = self.get_response(request)
        return response
