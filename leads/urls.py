from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()

router.register('api/leads', LeadViewSet, 'leads')
# router.register('api/test', LeadViewSet.as_view({'get': 'list'}), basename='test')

urlpatterns = router.urls
