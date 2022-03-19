from django.shortcuts import render

from main.models import levelMod

# Create your views here.

def home(request):

    if request.user.is_authenticated:
        temp = levelMod.objects.filter(email=request.user.email)
        if temp.exists():
            obj = levelMod.objects.get(email=request.user.email)
            lev = obj.level
            return render(request, 'home.html', {'level': lev})
    
    return render(request, 'home.html')    

def gameEnds(request):
    if request.user.is_authenticated and request.method == 'GET':
        temp = levelMod.objects.filter(email=request.user.email)
        if temp.exists():
            obj = levelMod.objects.get(email=request.user.email)
            obj.score = obj.score + 1  

            if obj.score > 800:
                obj.level = 'Master'
            elif obj.score > 400:
                obj.level = 'Expert'
            elif obj.score > 200:
                obj.level = 'Specialist'
            elif obj.score > 100:
                obj.level = 'Champion'
            elif obj.score > 60:
                obj.level = 'Genius'
            elif obj.score > 20:
                obj.level = 'Pro'
            elif obj.score > 10:
                obj.level = 'Beginner'  

            lev = obj.level          
            obj.save()
        else:
            sc = levelMod.objects.create(name=request.user.username, email=request.user.email, score=1, level="Bot")   
            lev = 'Bot'
            sc.save()

        return render(request, 'home.html', {'level': lev})

    return render(request, 'home.html')    

