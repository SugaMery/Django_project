from django.shortcuts import render,redirect
from django.template import RequestContext
from .models import Chef_departement, Etudiant, Matiere, Professeur
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def deptGit(request):
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie informatique et telecoms')   
    context ={ 'forms' : form}
    return render(request,'departements/git/git.html', context)
    
@login_required(login_url='login')
def deptGitEns(request):
    items =Professeur.objects.filter(departemet__nom_departement='Génie informatique et telecoms')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie informatique et telecoms')
    context ={ 'items':items ,'forms' : form}
    return render(request,'departements/git/enseingnant.html',context)

@login_required(login_url='login')
def deptGitMat(request):
    itemss = Matiere.objects.filter(departemet__nom_departement='Génie informatique et telecoms')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie informatique et telecoms')
    context ={ 'items':itemss ,'forms' : form}
    return render(request,'departements/git/matiere.html',context)
@login_required(login_url='login')
def deptETDIC1(request):
    items = Etudiant.objects.filter(departement__nom_departement='Génie informatique et telecoms').filter(classe__nom_classe='DIC1')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie informatique et telecoms')
    context ={ 'items':items ,'forms' : form}
    return render(request,'departements/git/DIC1.html',context)
@login_required(login_url='login')
def deptETDIC2(request):
    items = Etudiant.objects.filter(departement__nom_departement='Génie informatique et telecoms').filter(classe__nom_classe='DIC2')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie informatique et telecoms')
    context ={ 'items':items ,'forms' : form}
    return render(request,'departements/git/DIC2.html',context)
@login_required(login_url='login')
def deptETDIC3(request):
    items = Etudiant.objects.filter(departement__nom_departement='Génie informatique et telecoms').filter(classe__nom_classe='DIC3')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie informatique et telecoms')
    context ={ 'items':items ,'forms' : form}
    return render(request,'departements/git/DIC3.html',context)


@login_required(login_url='login')
def deptCivil(request):
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie civil')
    context ={ 'forms' : form}
    return render(request,'departements/civil/civil.html', context)
    
@login_required(login_url='login')
def deptCivilEns(request):
    items =Professeur.objects.filter(departemet__nom_departement='Génie civil')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie civil')
    context ={ 'items':items ,'forms' : form}
    return render(request,'departements/civil/enseingnant.html',context)
@login_required(login_url='login')
def deptCivilMat(request):
    itemss = Matiere.objects.filter(departemet__nom_departement='Génie civil')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie civil')
    context ={ 'items':itemss ,'forms' : form}
    return render(request,'departements/civil/matiere.html',context)
@login_required(login_url='login')
def deptCETDIC1(request):
    items = Etudiant.objects.filter(departement__nom_departement='Génie civil').filter(classe__nom_classe='DIC1')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie civil')
    context ={ 'items':items ,'forms' : form}
    return render(request,'departements/civil/DIC1.html',context)
@login_required(login_url='login')
def deptCETDIC2(request):
    items = Etudiant.objects.filter(departement__nom_departement='Génie civil').filter(classe__nom_classe='DIC2')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie civil')
    context ={ 'items':items ,'forms' : form}
    return render(request,'departements/civil/DIC2.html',context)
@login_required(login_url='login')
def deptCETDIC3(request):
    items = Etudiant.objects.filter(departement__nom_departement='Génie civil').filter(classe__nom_classe='DIC3')
    form=Chef_departement.objects.filter(diriger__nom_departement='Génie civil')
    context ={ 'items':items ,'forms' : form}
    return render(request,'departements/civil/DIC3.html',context)


# def eleve(request):
#     items = EleveIngenieur.objects.all()
    
#     # if request.method=='POST':
#     #     form = EleveForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('login')
#     # else :
#     #     form =EleveForm()   
#     context ={
#         'items':items,
#         # 'form':form,
#     }
    
    
#     return render(request,'departements/git.html',context)
