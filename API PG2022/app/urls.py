from rest_framework import routers
from .views import UssdPaymentsControl,UssdPaymentsControlTypeMercados,UssdRequestControl, RegisterAPI, UssdRequests, UssdRequestsOperadoras
from django.urls import path, include

routers = routers.DefaultRouter()
# routers.register(r'employeer', EmployeerViewSet)
# routers.register(r'formation', FormationViewSet)
# routers.register(r'test', GetFormation)
# routers.register(r'formadd', AddFormatioViewSet)
routers.register(r'auth/ussd', UssdRequestControl)
routers.register(r'auth/payments', UssdPaymentsControl)
routers.register(r'auth/endpointmercados', UssdPaymentsControlTypeMercados)

# routers.register(r'auth/payments/mercados/all', UssdPaymentsControlMercados)
routers.register(r'auth/all_requests', UssdRequests)
routers.register(r'auth/por_operadoras', UssdRequestsOperadoras)



urlpatterns = [*routers.urls,
    path('auth/', include('knox.urls')),
    path('auth/register/', RegisterAPI.as_view()),
]