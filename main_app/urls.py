from django.conf.urls import url
from .views import index, post_relief_effort, show, post_item_request, relief_efforts_index
from .views import login_view, org_admin_signup, post_org_admin_user, signup, donor_signup
from .views import about
from .orgadminviews import OrgAdminSignUpView

urlpatterns = [
    url(r'^$', index),
    url(r'^org_admin_signup/$', org_admin_signup, name='org_admin_signup'),
    url(r'^donor_signup/$', donor_signup, name='donor_signup'),
    url(r'^post_url/$', post_relief_effort, name='post_relief_effort'),
    url(r'^org_admin_signup/post/$', post_org_admin_user, name='post_org_admin_user'),
    url(r'^relief_efforts/$', relief_efforts_index, name = 'relief_efforts_index'),
    url(r'^signup_login/$', login_view, name="login"),
    url(r'^org_admin_signup_v2/$', OrgAdminSignUpView.as_view(), name='org_admin_signup_v2'),
    url(r'^signup/$', signup, name="signup"),
    url(r'^about/$', about, name="about"),
    url(r'^([0-9]+)/$', show, name = 'show'),
    url(r'^([0-9]+)/post_item_request/$', post_item_request, name = 'post_item_request')
]
