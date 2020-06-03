from django.forms import formset_factory,modelformset_factory
from django.shortcuts import render

# Create your views here.
from .models import Post
from django.utils import timezone
from .forms import TestForm,PostModelForm


# def formset_view(request):
#     TestFormset = formset_factory(TestForm,extra=2)
#     formset = TestFormset(request.POST or None)
#     if formset.is_valid():
#         for form in formset:
#             print(form.cleaned_data)
#     context = {
#         "formset":formset
#     }

#     return render(request,"formset_view.html",context)

def formset_view(request):
    PostModelFormset = modelformset_factory(Post,form=PostModelForm,extra=2)
    formset = PostModelFormset(request.POST or None,queryset=Post.objects.filter(user__username="root"))
    if formset.is_valid():
        for form in formset:
            obj =form.save(commit=False)
            if form.cleaned_data:
                obj.title = f"{obj.title}" 
                print(obj.title)
                obj.publish = timezone.now()
                obj.save()

    context = {
        "formset":formset,
        
    }

    return render(request,"formset_view.html",context)







# def home(request):
#     form = PostModelForm(request.POST or None)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.publish = timezone.now()
#         obj.save()

#     if form.has_error:
#         # print(form.errors.as_json)
#         # print(form.errors.as_text())
#         data = form.errors.items()
#         for key,value in data:
#             # print(key,value)
#             error_str = "{field}: {error}".format(
#                         field=key,
#                         error=value.as_text()
#                     )
#             print(error_str)
        # print(form.fields)


    return render(request,'forms.html',{"form":form})
    


    # initial_dict = {
    #     # "search_text": "search",
    #     # "boolean": "True",
    #     # "integer": "123",
    #     # "email": "xxxx@xxx.com"
    # }
    # form = TestForm(request.POST or None,initial=initial_dict)
    # if form.is_valid():
    #     print(form.cleaned_data)
    # if request.method == 'POST':
    #     form = TestForm(data=request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #     # print(request.POST)
    #     # print(request.POST.get('username'))
    # else:
    #     request.method == 'GET'
    #     form = TestForm(user=request.user)
    #     print(request.GET)

    
