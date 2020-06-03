from django import forms

from .models import Post

class PostModelForm(forms.ModelForm):
    # title2 = forms.CharField(max_length=120,label='some field',help_text='some help',
    #                         error_messages={'required':'Not be empty'})
    class Meta:
        model = Post
        fields = [
            "user",
            "title",
            "slug",
            "image"
            ]
        labels = {
            "title":"this is title label",
            "slug":"slug-field"
        }
        help_text = {
            "title":"this is title label",
            "slug":"slug-field"
        }
        # error_messages = {
        #     "title": {"max_length":"this title is too long",
        #     "required"::"Field required"}
        # }
        # error_messages = {
        #     "slug": {"max_length":"this title is too long",
        #     "required":"Field required",
        #     "unique":"slug field must unique"
        #     }
        # }
        # exclude = ["height_field","width_field"]
    def __init__(self,*args,**kwargs):
        super(PostModelForm,self).__init__(*args,**kwargs)
        # self.fields['slug'].error_messages={
        #     'required':'Sorry slug field not be empty',
        #     'unique':'Must be unique else not activate'
        #     }
        # self.fields['title'].error_messages={
        #     'required':'Sorry slug field not be empty',
        #     'unique':'Must be unique else not activate'
        #     }

        for field in self.fields.values():
            field.error_messages = {
                'required':'{fieldname} is required'.format(fieldname=field.label)
            }
    # def clean_title(self,**kwargs):
    #     title = self.cleaned_data.get('title')
        # print(title)
        # raise forms.ValidationError("Nope")
        # return title


    # def save(self,commit=True,**kwargs):
    #     obj = super(PostModelForm,self).save(commit=False,**kwargs)
    #     # obj.title = 'left'
    #     obj.publish = "2020-3-26"
    #     obj.content = "Coming Soon"
    #     from django.utils.text import slugify
    #     obj.title = slugify(obj.title)
    #     if commit:
    #         obj.save()
    #     return obj




Some_choices = (
    ('db-value','display Value01'),
    ('db-value','display Value02'),
    ('db-value','display Value03'),
    
)

Integer_Choice = [tuple([x,x]) for x in range(10,20)]

years = [x for x in range(1986,2021)]

class TestForm(forms.Form):
    date_field = forms.DateField(initial=("2006-03-26"),widget=forms.SelectDateWidget(years=years))
    search_text = forms.CharField(label='Search you want',widget=forms.Textarea(attrs={'cols':8,'rows':1}))
    choices = forms.CharField(widget=forms.Select(choices=Some_choices))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10,widget=forms.Select(choices=Integer_Choice))
    email = forms.EmailField()

    def __init__(self,user=None,*args,**kwargs):
        super(TestForm,self).__init__(*args,**kwargs)
        if user:
            self.fields["search_text"].initial = user

    def clean_integer(self,**kwargs):
        integer = self.cleaned_data.get('integer')
        if integer < 10:
            raise forms.ValidationError("Number must be greater then 10")
        return integer

    def clean_search_text(self,**kwargs):
        search_text = self.cleaned_data.get("search_text")
        if len(search_text) < 3:
            raise forms.ValidationError("Minimum characters is 3")
        return search_text

