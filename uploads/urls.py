from django.conf.urls import  include, url
from qa.views import test, root, question_page, popular_sort_page

urlpatterns = [                                              
   url(r'^$', root, name='root'),
   url(r'^login/.*$', test, name='login'),                                    
   url(r'^signup/.*', test, name='signup'),                                   
   url(r'^question/(?P<id>[0-9]+)/', question_page, name='question'),
   url(r'^ask/.*', test, name='ask'),                                         
   url(r'^popular/.*', popular_sort_page, name='popular'),
   url(r'^new/.*', test, name='new'),                                         
]
