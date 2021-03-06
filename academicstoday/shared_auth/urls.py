from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from shared_auth.views import email_views
from shared_auth.views import web_views


urlpatterns = (
    # # EMAIL
    # Email Views
    url(r'^activate-email/(.*)/$', email_views.user_activation_email_page, name='at_activate_email'),
    url(r'^reset-password-email/(.*)/$', email_views.reset_password_email_page, name='at_reset_password_email'),

    # WEB
    url(r'^login/$',
    web_views.user_login_master_page,
    name='at_login_master'),

    url(r'^registration/$',
    web_views.user_register_master_page,
    name='at_register_master'),

    url(r'^registration-completed/$',
    web_views.user_register_detail_page,
    name='at_register_detail'),

    url(r'^login/redirector$',
    web_views.user_login_redirector_master_page,
    name='at_login_redirector'),

    url(r'^reset/$',
    web_views.send_reset_password_email_master_page,
    name='at_send_reset_password_email_master'),

    url(r'^reset/submitted$',
    web_views.send_reset_password_email_submitted_page,
    name='at_send_reset_password_email_submitted'),

    url(r'^reset/(.*)/$',
    web_views.rest_password_master_page,
    name='at_reset_password_master'),

    # url(r'^register/$',
    # web_views.register_user_master_page,
    # name='at_register_master'),
    #
    # url(r'^register/done$',
    # web_views.register_user_detail_page,
    # name='at_register_detail'),

    url(r'^activate/(.*)/$',
    web_views.user_activation_detail_page,
    name='at_user_activation_detail'),

    url(r'^logout/redirector$',
    web_views.user_logout_redirector_master_page,
    name='at_logout_redirector'),
)
