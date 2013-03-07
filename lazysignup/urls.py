from django.conf.urls import patterns, url

from django.views.generic import TemplateView

# URL patterns for lazysignup

urlpatterns = patterns(
    'lazysignup.views',
    url(r'^$', 'convert', name='lazysignup_convert'),
    url(r'^merge/$', 'merge', name='lazysignup_merge'),
    url(r'^done/$',
        TemplateView.as_view(template_name='lazysignup/done.html'),
        name='lazysignup_convert_done'),
)
