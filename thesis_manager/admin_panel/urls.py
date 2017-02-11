from django.conf.urls import url
from . import views
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^$', views.admin_homepage, name='admin_homepage'),
    url(r'^new_year/$', views.new_year, name='new_year'),
    url(r'^man_years/$', views.man_years, name='man_years'),
    url(r'^upload_students/$', views.upload_students, name='upload_students'),
    url(r'^upload_supervisors/$', views.upload_supervisors, name='upload_supervisors'),
    url(r'^upload_thesis/$', views.upload_thesis, name='upload_thesis'),
    url(r'^upload_reviewers/$', views.upload_reviewers, name='upload_reviewers'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^supervisor_handler/$', views.supervisor_handler, name='supervisor_handler'),
    url(r'^supervisor_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_supervisors')), name='supervisor_handler/redirection'),
    url(r'^student_handler/$', views.student_handler, name='student_handler'),
    url(r'^student_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_students')), name='student_handler/redirection'),
    url(r'^thesis_handler/$', views.thesis_handler, name='thesis_handler'),
    url(r'^thesis_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_thesis')), name='thesis_handler/redirection'),
    url(r'^reviewer_handler/$', views.reviewer_handler, name='reviewer_handler'),
    url(r'^reviewer_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_reviewer')), name='reviewer_handler/redirection'),
    url(r'^file_handler/$', views.file_handler, name='file_handler'),
    url(r'^file_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('upload_students')), name='file_handler/redirection'),
    url(r'^standard_handler/$', views.standard_handler, name='standard_handler'),
    url(r'^standard_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('admin_homepage')), name='standard_handler/redirection'),
    url(r'^prearranged_handler/$', views.prearranged_handler, name='prearranged_handler'),
    url(r'^prearranged_handler/redirection/$', RedirectView.as_view(url=reverse_lazy('admin_homepage')), name='prearranged_handler/redirection'),
    url(r'^graduate/$', views.graduate, name='graduate'),
    url(r'^graduate/redirection/$', RedirectView.as_view(url=reverse_lazy('admin_homepage')), name='graduate/redirection'),
    # url(r'^saving_database/$', views.saving_database, name='saving_database'),
    # url(r'^saving_database/redirection/$', RedirectView.as_view(url=reverse_lazy('man_years')), name='saving_database/redirection'),
    # url(r'^deleting_database/$', views.deleting_database, name='deleting_database'),
    # url(r'^deleting_database/redirection/$', RedirectView.as_view(url=reverse_lazy('man_years')), name='deleting_database/redirection'),
    # url(r'^load_database/$', views.load_database, name='load_database'),
    # url(r'^load_database/redirection/$', RedirectView.as_view(url=reverse_lazy('man_years')), name='load_database/redirection'),
    url(r'^(?P<student_id>[0-9]+)/assign_document$', views.assign_document, name='assign_document'),
    url(r'^(?P<student_id>[0-9]+)/standard_thesis$', views.standard_thesis, name='standard_thesis'),
    url(r'^(?P<student_id>[0-9]+)/handed_assignment_over$', views.handed_assignment_over, name='handed_assignment_over'),

]
