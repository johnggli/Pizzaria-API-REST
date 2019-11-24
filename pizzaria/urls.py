from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),

    path('user', UserList.as_view(), name=UserList.name),
    path('user/<int:pk>', UserDetail.as_view(), name=UserDetail.name),

    path('address', AddressList.as_view(), name=AddressList.name),
    path('address/<int:pk>', AddressDetail.as_view(), name=AddressDetail.name),
    path('client', ClientList.as_view(), name=ClientList.name),
    path('client/<int:pk>', ClientDetail.as_view(), name=ClientDetail.name),
    path('manager', ManagerList.as_view(), name=ManagerList.name),
    path('manager/<int:pk>', ManagerDetail.as_view(), name=ManagerDetail.name),
    path('employee', EmployeeList.as_view(), name=EmployeeList.name),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name=EmployeeDetail.name),
    path('progress', ProgressList.as_view(), name=ProgressList.name),
    path('progress/<int:pk>', ProgressDetail.as_view(), name=ProgressDetail.name),
    path('pizza', PizzaList.as_view(), name=PizzaList.name),
    path('pizza/<int:pk>', PizzaDetail.as_view(), name=PizzaDetail.name),
    path('demand', DemandList.as_view(), name=DemandList.name),
    path('demand/<int:pk>', DemandDetail.as_view(), name=DemandDetail.name),

    path('api-auth/', include('rest_framework.urls')),
]