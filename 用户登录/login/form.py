from django import forms
from .models import *


class BookForm(forms.ModelForm):
    # 重写ProductModelForm类的初始函数__init__
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # 设置下拉框的数据
        publish_obj = Publish.objects.values('name')
        author_obj = Author.objects.values('name')
        publish_choices_list = [(i + 1, v['name']) for i, v in enumerate(publish_obj)]
        author_choices_list = [(i + 1, v['name']) for i, v in enumerate(author_obj)]
        self.fields['publish'].choices = publish_choices_list
        self.fields['authors'].choices = author_choices_list
        # 初始化字段name
        #self.fields['name'].initial = '我的手机'

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': '书名',
            'publishDate': '出版日期',
            'price': '价格',
            'pageNum': '页数',
            'publish': '出版社',
            'authors': '作者'
        }



class AthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name': '姓名',
            'age': '年龄'
        }

class PublishForm(forms.ModelForm):
    class Meta:
        model = Publish
        fields = '__all__'
        labels = {
            'name': '出版社',
            'city': '城市',
            'email': '邮箱'
        }