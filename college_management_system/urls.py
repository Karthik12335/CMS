
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from cms import views

router = DefaultRouter()
router.register(r"course", views.CourseView)
router.register(r"subject", views.SubjectView)
router.register(r"student", views.StudentView)
router.register(r"teacher", views.TeacherView)
router.register(r"class", views.ClassView)




# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cms/',include('cms.urls'))
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/doc/", SpectacularSwaggerView.as_view(url_name="schema")),
]