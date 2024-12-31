from django.urls import path
from news import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article',views.ArticleAPIViewset)
router.register('journalist',views.JournalistAPIViewset)

urlpatterns=[
    path('generics/',views.ArticleAPIGeneric.as_view())

]+ router.urls