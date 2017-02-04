from django.conf.urls import url
from . import views
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from .models import Student

urlpatterns = [
    url(r'^$', views.admin_homepage, name='admin_homepage'),
    url(r'^new_year/$', views.new_year, name='new_year'),
    url(r'^man_years/$', views.man_years, name='man_years'),
    url(r'^upload_students/$', views.upload_students, name='upload_students'),
    url(r'^upload_teachers/$', views.upload_teachers, name='upload_teachers'),
    url(r'^upload_thesis/$', views.upload_thesis, name='upload_thesis'),
    url(r'^upload_reviewers/$', views.upload_reviewers, name='upload_reviewers'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^teacher_handler/$', views.teacher_handler, name='teacher_handler'),
    url(r'^teacher_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_teachers')), name='teacher_handler/redirection'),
    url(r'^student_handler/$', views.student_handler, name='student_handler'),
    url(r'^student_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_students')), name='student_handler/redirection'),
    url(r'^thesis_handler/$', views.thesis_handler, name='thesis_handler'),
    url(r'^thesis_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_thesis')), name='thesis_handler/redirection'),
    url(r'^reviewer_handler/$', views.reviewer_handler, name='reviewer_handler'),
    url(r'^reviewer_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_reviewer')), name='reviewer_handler/redirection'),
    url(r'^file_handler/$', views.file_handler, name='file_handler'),
    url(r'^file_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_students')), name='file_handler/redirection'),
    url(r'^empty_tables/$', views.empty_tables, name='empty_tables'),
    url(r'^empty_tables/redirection/$', RedirectView.as_view(url=reverse_lazy('admin_homepage')), name='empty_tables/redirection'),
    url(r'^saving_database/$', views.saving_database, name='saving_database'),
    url(r'^saving_database/redirection/$', RedirectView.as_view(url=reverse_lazy('man_years')), name='saving_database/redirection'),
    url(r'^deleting_database/$', views.deleting_database, name='deleting_database'),
    url(r'^deleting_database/redirection/$', RedirectView.as_view(url=reverse_lazy('man_years')), name='deleting_database/redirection'),
    url(r'^load_database/$', views.load_database, name='load_database'),
    url(r'^load_database/redirection/$', RedirectView.as_view(url=reverse_lazy('man_years')), name='load_database/redirection'),
    url(r'^(?P<student_id>[0-9]+)/assign_document$', views.assign_document, name='assign_document'),
]
