from django.forms import ModelForm
from .models import Users,Books
class UsersForm(ModelForm):
    class Meta():
        model = Users
        fields = ['username','password','email','college','num']

# class BooksForm(ModelForm):
#     class Meta():
#         model = Books
#         fields = ['ISBN','book_name','author','publish_com','publish_date']