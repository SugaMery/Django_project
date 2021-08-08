from django.urls import path
from . import views

urlpatterns=[
    path('git/',views.deptGit,name='git'),
    path('git/enseingnement',views.deptGitEns,name='giten'),
    path('git/matiere',views.deptGitMat,name='gitmt'),
    path('git/DIC1',views.deptETDIC1,name='gitdic1'),
    path('git/DIC2',views.deptETDIC2,name='gitdic2'),
    path('git/DIC3',views.deptETDIC3,name='gitdic3'),

    path('civil/',views.deptCivil,name='civil'),
    path('civil/enseingnement',views.deptCivilEns,name='civilen'),
    path('civil/matiere',views.deptCivilMat,name='civilmt'),
    path('civil/DIC1',views.deptCETDIC1,name='civildic1'),
    path('civil/DIC2',views.deptCETDIC2,name='civildic2'),
    path('civil/DIC3',views.deptCETDIC3,name='civildic3'),
]