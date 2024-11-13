from django.core.exceptions import PermissionDenied

class SitePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path == "/admin/login":
            return None
        
        if request.path.startwith("/admin/"):
            if not (request.user.is_staff and request.user.is_active):
                raise PermissionDenied