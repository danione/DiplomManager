from django.conf.urls import url
from . import views
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^$', views.admin_homepage, name='admin_homepage'),
    url(r'^new_year/$', views.new_year, name='new_year'),
    url(r'^man_years/$', views.man_years, name='man_years'),
    url(r'^upload_students/$', views.upload_students, name='upload_students'),
    url(r'^upload_teachers/$', views.upload_teachers, name='upload_teachers'),
    url(r'^upload_thesis/$', views.upload_thesis, name='upload_thesis'),
    url(r'^upload_reviewers/$', views.upload_reviewers, name='upload_reviewers'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^student_handler/$', views.student_handler, name='student_handler'),
    url(r'^student_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_students')), name='student_handler/redirection'),
]
