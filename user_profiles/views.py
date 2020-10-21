from django.shortcuts import render

# Create your views here.
def user_profile(request):
    """ Page for user profiles """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
