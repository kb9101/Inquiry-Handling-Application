from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'inquiries', views.InquiryViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('api',UserViewSet.as_view()),
    # path('api/createuser', CreateUserViewSet.as_view()),
    # path('api/<int:pk>', UpdateUserViewSet.as_view()),
    # path('api/<int:pk>/delete', DeleteUserViewSet.as_view()),
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-users'),
    path('all/', views.view_users, name='view_users'),
    path('update/<int:pk>/', views.update_users, name='update-users'),
    path('item/<int:pk>/delete/', views.delete_users, name='delete-users'),

]
