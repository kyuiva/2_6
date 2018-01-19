echo "from django.contrib.auth.models import User" >> /home/box/web/ask/qa/models.py
echo "" >> /home/box/web/ask/qa/models.py
echo "class QuestionManager(models.Manager):" >> /home/box/web/ask/qa/models.py
echo "    def new(self):" >> /home/box/web/ask/qa/models.py
echo "        return self.order_by('-added_at')" >> /home/box/web/ask/qa/models.py
echo "    def popular(self):" >> /home/box/web/ask/qa/models.py
echo "        return self.order_by('-rating')" >> /home/box/web/ask/qa/models.py
echo "" >> /home/box/web/ask/qa/models.py
echo "class Question(models.Model):" >> /home/box/web/ask/qa/models.py
echo "    objects = QuestionManager()" >> /home/box/web/ask/qa/models.py
echo "    title = models.CharField(max_length=128)" >> /home/box/web/ask/qa/models.py
echo "    text = models.TextField()" >> /home/box/web/ask/qa/models.py
echo "    added_at = models.DateTimeField(blank = True, auto_now_add = True)" >> /home/box/web/ask/qa/models.py
echo "    rating = models.IntegerField(default = 0)" >> /home/box/web/ask/qa/models.py
echo "    author = models.ForeignKey(User)" >> /home/box/web/ask/qa/models.py
echo "    likes = models.ManyToManyField(User, related_name='likes_set')" >> /home/box/web/ask/qa/models.py
echo "" >> /home/box/web/ask/qa/models.py
echo "class Answer(models.Model):" >> /home/box/web/ask/qa/models.py
echo "    text = models.TextField()" >> /home/box/web/ask/qa/models.py
echo "    added_at = models.DateTimeField(blank = True, auto_now_add = True)" >> /home/box/web/ask/qa/models.py
echo "    question = models.ForeignKey(Question)" >> /home/box/web/ask/qa/models.py
echo "    author = models.ForeignKey(User)" >> /home/box/web/ask/qa/models.py


