from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse
from miriapp.serializer.user_serializer import UserForm

class UserFormView(View):
   from_class = UserForm
   template_name='miriapp/login.html'

   #display blank form
   @csrf_exempt
   def get(self,request):
       form=self.from_class(None)
       return HttpResponse(request, self.template_name, {'form': form})

   @csrf_exempt
   def post(self,request):
       form=self.from_class(request.POST)
       if form.is_valid():
           user = form.save(commit=False)

           # cleaned data
           username=form.cleaned_data['username']
           password=form.cleaned_data['password']
           user.set_password(password)
           user.save()

           user = authenticate(username=username , password=password)

           if user is not None:
               if user.is_active:
                   login(request,user)
                   return redirect('miriapp:index')
       return HttpResponse(request,self.template_name,{'form':form})