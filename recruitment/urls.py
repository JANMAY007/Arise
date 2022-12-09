from django.conf.urls.static import static
from django.urls import path

from Arise import settings
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("add-mail/", views.add_mail, name='add_mail'),
    path("signup/", views.signup_user, name="Signup"),
    path("login/", views.login_user, name="Login"),
    path("logout/", views.logout_user, name="Logout"),
    path("contactus/", views.contactus, name="ContactUs"),
    path("lifeatarise/", views.life_at_arise, name="LifeAtArise"),
    path("whyarisesolution/", views.why_arise_solution, name="WhyAriseSolution"),
    path("applicationprocess/", views.applicationprocess, name="ApplicationProcess"),
    path('awards/', views.awards, name="Awards"),
    path("careers/", views.careers, name="Careers"),
    path("apprenticeship/", views.apprenticeship, name="Apprenticeship"),
    path("bulkrecruit/", views.bulkrecruit, name="BulkRecruit"),
    path("contractstaff/", views.contractstaff, name="ContractStaff"),
    path("employeelease/", views.employeelease, name="EmployeeLease"),
    path("hiretraindeploy/", views.hiretraindeploy, name="HireTrainDeploy"),
    path("itstaff/", views.itstaff, name="ItStaff"),
    path("leadership/", views.leadership, name="Leadership"),
    path("payroll/", views.payroll, name="Payroll"),
    path("permstaff/", views.permstaff, name="PermStaff"),
    path("turnkey/", views.turnkey, name="Turnkey"),
    path("walkinform/", views.walk_in_form, name="WalkinForm"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
