from django.http.response import HttpResponseForbidden


# FILTRA IP MIDDLEWARE
# ----------------------------------------

class FiltraIPMiddleware:

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        return None
