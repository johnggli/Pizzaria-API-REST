from django.urls import path, include
from .views import *
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),

    path('user/', UserList.as_view(), name=UserList.name),
    path('user/<int:pk>', UserDetail.as_view(), name=UserDetail.name),

    path('address/', AddressList.as_view(), name=AddressList.name),
    path('address/<int:pk>', AddressDetail.as_view(), name=AddressDetail.name),
    path('client/', ClientList.as_view(), name=ClientList.name),
    path('client/<int:pk>', ClientDetail.as_view(), name=ClientDetail.name),
    path('manager/', ManagerList.as_view(), name=ManagerList.name),
    path('manager/<int:pk>', ManagerDetail.as_view(), name=ManagerDetail.name),
    path('employee/', EmployeeList.as_view(), name=EmployeeList.name),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name=EmployeeDetail.name),
    path('progress/', ProgressList.as_view(), name=ProgressList.name),
    path('progress/<int:pk>', ProgressDetail.as_view(), name=ProgressDetail.name),
    path('pizza/', PizzaList.as_view(), name=PizzaList.name),
    path('pizza/<int:pk>', PizzaDetail.as_view(), name=PizzaDetail.name),
    path('demand/', DemandList.as_view(), name=DemandList.name),
    path('demand/<int:pk>', DemandDetail.as_view(), name=DemandDetail.name),
    
    path('manager-employees/', ManagerEmployeeList.as_view(), name=ManagerEmployeeList.name),
    path('employee-demands/', EmployeeDemands.as_view(), name=EmployeeDemands.name),

    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api-docs/', schema_view),

]