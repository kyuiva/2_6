echo "from django.conf.urls import  include, url" >> /home/box/web/ask/qa/urls.py
echo "from qa.views import test" >> /home/box/web/ask/qa/urls.py
echo "" >> /home/box/web/ask/qa/urls.py

echo "urlpatterns = [" >> /home/box/web/ask/qa/urls.py
echo "   url(r'^$', test, name='root')," >> /home/box/web/ask/qa/urls.py
echo "   url(r'^login/.*$', test, name='login')," >> /home/box/web/ask/qa/urls.py
echo "   url(r'^signup/.*', test, name='signup')," >> /home/box/web/ask/qa/urls.py
echo "   url(r'^question/(?P<id>[0-9]+)/$', test, name='question')," >> /home/box/web/ask/qa/urls.py
echo "   url(r'^ask/.*', test, name='ask')," >> /home/box/web/ask/qa/urls.py
echo "   url(r'^popular/.*', test, name='popular')," >> /home/box/web/ask/qa/urls.py
echo "   url(r'^new/.*', test, name='new')," >> /home/box/web/ask/qa/urls.py
echo "]" >> /home/box/web/ask/qa/urls.py
