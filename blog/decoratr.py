from django.shortcuts import redirect

def custom_login_required(funk):
    def wrapper(request):
        if not request.user.is_authenticated:
            return redirect('login')
        return funk(request)
    return wrapper