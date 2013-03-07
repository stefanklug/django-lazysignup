import django.dispatch

converted = django.dispatch.Signal(providing_args=['user'])
merge = django.dispatch.Signal(providing_args=['lazy_user','user'])
