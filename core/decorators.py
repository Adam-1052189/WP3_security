from django.http import HttpResponseRedirect

def custom_login_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:  # Controleer of dit werkt met jouw authenticatielogica
            return HttpResponseRedirect('login')  # Pas dit aan naar de URL van je loginpagina
        else:
            return function(request, *args, **kwargs)
    return wrap
