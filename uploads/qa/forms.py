# -*- coding: utf-8 -*-
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    #def __init__(self, user, *args, **kwargs):
    #    self._user = user
    #    super(AskForm, self).__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'Error occured', code = 'err')
        else:
            return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        u = User.objects.all()[0]
        question.author = u
        question.save()
        return question

class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea, label = 'Введите ответ здесь:') #
    question = forms.IntegerField(widget=forms.HiddenInput()) #
    # forms.ModelChoiceField(queryset = None)

    #def __init__(self, user, *args, **kwargs):
    #   self._user = user
    #   super(AnswerForm, self).__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(('Invalid value'), code='invalid')
            # raise forms.ValidationError () # (u'Error occured', self.errors)
        else:
            return self.cleaned_data

    def save(self):
        #answer = Answer(**self.cleaned_data)
        u = User.objects.all()[0]
        #answer.question = Question.objects.get(id=self.cleaned_data["question"])
        #answer.author = u
        q = Question.objects.get(id=self.cleaned_data["question"])
        t = self.cleaned_data["text"]
        answer = Answer(text = t, question = q, author = u)
        answer.save()
        return answer
