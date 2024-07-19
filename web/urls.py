from django.urls import path
from . import views

from web.views import PaymentViewWebsitetemplate, PaymentViewMobiletemplate, PaymentViewDesktoptemplate, PaymentViewMicrosofttemplate, PaymentViewAdobetemplate, PaymentViewWebsite, PaymentViewMobile, PaymentViewDesktop, PaymentViewEmbeded, PaymentViewGraphics, PaymentViewProject, PaymentViewImage
# from web.views import *

urlpatterns = [
    path('admin/', views.admin, name = "admin"),
    path('signup/', views.signup, name = "signup"),
    path('signin/', views.signin, name = "signin"),
	path('logout/', views.logout, name="logout"),
 
    path("",views.home,name = "home"),
    path("aboutus/",views.aboutus,name = "aboutus"),
    path("base/",views.base,name = "base"),
    path("contactus/",views.contactus,name = "contactus"),
    path("contactpost/",views.contactpost,name = "contactpost"),
    path("contactlist/",views.contactlist,name = "contactlist"),
    path("viewcontact/<int:id>/",views.viewcontact,name = "viewcontact"),
    path('deletecontact/<int:id>/', views.deletecontact, name = "deletecontact"),
    path("dashboard/",views.dashboard,name = "dashboard"),
    path("services/",views.services,name = "services"),
    
    # url for success message
    path("signupsucces/",views.signupsucces,name = "signupsucces"),
    path("logedout/",views.logedout,name = "logedout"),
    
    # path("courses/",views.courses,name = "courses"),
    
    # courses to be tought
    path("computercs/",views.computercs,name = "computercs"),
    path("computereng/",views.computereng,name = "computereng"),
    path("electrical/",views.electrical,name = "electrical"),
    path("civil/",views.civil,name = "civil"),
    path("mechanical/",views.mechanical,name = "mechanical"),
    path("artificial/",views.artificial,name = "artificial"),
    path("softwareeng/",views.softwareeng,name = "softwareeng"),
    path("embeded/",views.embeded,name = "embeded"),
    path("website/",views.website,name = "website"),
    path("mobileapp/",views.mobileapp,name = "mobileapp"),
    path("virtualreality/",views.virtualreality,name = "virtualreality"),
    path("security/",views.security,name = "security"),
    path("desktopapp/",views.desktopapp,name = "desktopapp"),
    path("multmedia/",views.multmedia,name = "multmedia"),
    path("graphics/",views.graphics,name = "graphics"),
    path("iot/",views.iot,name = "iot"),
    path("security/",views.security,name = "security"),
    path("nertworking/",views.nertworking,name = "nertworking"),
    
    # for frontend development
    path("wfrontend/",views.wfrontend,name = "wfrontend"),
    
    path("htmlcss/",views.htmlcss,name = "htmlcss"),
    path("javascript/",views.javascript,name = "javascript"),
    path("vuejs/",views.vuejs,name = "vuejs"),
    path("reactjs/",views.reactjs,name = "reactjs"),
    path("bootstrap/",views.bootstrap,name = "bootstrap"),
    path("angularjs/",views.angularjs,name = "angularjs"),
    
    # for backend website development
    path("wbackend/",views.wbackend,name = "wbackend"),
    
    path("django/",views.django,name = "django"),
    path("flask/",views.flask,name = "flask"),
    path("php/",views.php,name = "php"),
    path("laravel/",views.laravel,name = "laravel"),
    path("rub/",views.rub,name = "rub"),
    
    # for full stack website development
    path("wfullstack/",views.wfullstack,name = "wfullstack"),
    
    path("djangohtml/",views.djangohtml,name = "djangohtml"),
    path("flaskhtml/",views.flaskhtml,name = "flaskhtml"),
    path("phphtml/",views.phphtml,name = "phphtml"),
    path("laravelhtml/",views.laravelhtml,name = "laravelhtml"),
    path("djangoreact/",views.djangoreact,name = "djangoreact"),
    
# for mobile application
    
    #for mobile application front end
    path("mfrontend/",views.mfrontend,name = "mfrontend"),
    
    path("reactnative/",views.reactnative,name = "reactnative"),
    path("kivy/",views.kivy,name = "kivy"),
    path("fluter/",views.fluter,name = "fluter"),

    
    #mobile application backend
    path("mbackend/",views.mbackend,name = "mbackend"),
    
    path("mdjango/",views.mdjango,name = "mdjango"),
    path("mflask/",views.mflask,name = "mflask"),
    path("mfirebase/",views.mfirebase,name = "mfirebase"),
    
    #mobile application full stack development
    path("mfullstack/",views.mfullstack,name = "mfullstack"),
    
    path("reactnativedjango/",views.reactnativedjango,name = "reactnativedjango"),
    path("reactnativeflask/",views.reactnativeflask,name = "reactnativeflask"),
    path("reactnativefirebase/",views.reactnativefirebase,name = "reactnativefirebase"),
    
    #for desktop application
    path("cdeskapp/",views.cdeskapp,name = "cdeskapp"),
    path("pdeskapp/",views.pdeskapp,name = "pdeskapp"),
    path("kdeskapp/",views.kdeskapp,name = "kdeskapp"),
    
#artificial intelligence
    #for machine learning
    # path("machine/",views.machine,name = "machine"),
    
    # path("vision/",views.vision,name = "vision"),
    # path("natural/",views.natural,name = "natural"),
    # path("datascience/",views.datascience,name = "datascience"),
    # path("vision/",views.vision,name = "vision"),
    # path("natural/",views.natural,name = "natural"),
    # path("datascience/",views.datascience,name = "datascience"),
    
    #for deep learning.
    # path("deep/",views.deep,name = "deep"),       
    
    # path("vision/",views.vision,name = "vision"),
    # path("natural/",views.natural,name = "natural"),
    # path("datascience/",views.datascience,name = "datascience"),
    # path("vision/",views.vision,name = "vision"),
    # path("natural/",views.natural,name = "natural"),
    # path("datascience/",views.datascience,name = "datascience"),
    
    #for embeded system
    path("cembeded/",views.cembeded,name = "cembeded"),
    path("aembeded/",views.aembeded,name = "aembeded"),
    path("pembeded/",views.pembeded,name = "pembeded"),
    path("mpembeded/",views.mpembeded,name = "mpembeded"),
    
    #for graphics designing
    path("photoshop/",views.photoshop,name = "photoshop"),
    path("illustrator/",views.illustrator,name = "illustrator"),
    
    # FOR PROJECT
    path("websiteproject/",views.websiteproject,name = "websiteproject"),
    path("mobileproject/",views.mobileproject,name = "mobileproject"),
    path("desktopproject/",views.desktopproject,name = "desktopproject"),
    path("artificialproject/",views.artificialproject,name = "artificialproject"),
    path("embededproject/",views.embededproject,name = "embededproject"),
    path("iotproject/",views.iotproject,name = "iotproject"),
    path("virtualrealityproject/",views.virtualrealityproject,name = "virtualrealityproject"),
    path("cyberproject/",views.cyberproject,name = "cyberproject"),
    
    # FOR IMAGE
    path("image/",views.image,name = "image"),
    
    
    
    
    # template download
    path("webtemplate/",views.webtemplate,name = "webtemplate"),
    
    path("htmlcsstemplate/",views.htmlcsstemplate,name = "htmlcsstemplate"),
    path("reacttemplate/",views.reacttemplate,name = "reacttemplate"),
    
    
    path("mobiletemplate/",views.mobiletemplate,name = "mobiletemplate"),
    path("reactnativetemplate/",views.reactnativetemplate,name = "reactnativetemplate"),
    
    path("desktoptemplate/",views.desktoptemplate,name = "desktoptemplate"),
    
    path("kivytemplate/",views.kivytemplate,name = "kivytemplate"),
    path("pyqttemplate/",views.pyqttemplate,name = "pyqttemplate"),
    path("ctemplate/",views.ctemplate,name = "ctemplate"),
    path("tkintertemplate/",views.tkintertemplate,name = "tkintertemplate"),
    
    path("microsofttemplate/",views.microsofttemplate,name = "microsofttemplate"),
    
    path("wordtemplate/",views.wordtemplate,name = "wordtemplate"),
    path("excelltemplate/",views.excelltemplate,name = "excelltemplate"),
    path("powerpointtemplate/",views.powerpointtemplate,name = "powerpointtemplate"),
    path("publishertemplate/",views.publishertemplate,name = "publishertemplate"),
    
    path("adobetemplate/",views.adobetemplate,name = "adobetemplate"),
    
    path("photoshoptemplate/",views.photoshoptemplate,name = "photoshoptemplate"),
    path("primiertemplate/",views.primiertemplate,name = "primiertemplate"),
    path("illustratortemplate/",views.illustratortemplate,name = "illustratortemplate"),

    # download image
    
    # url posting the course and template url
    path("websitepost/",views.websitepost,name = "websitepost"),
    path("mobilepost/",views.mobilepost,name = "mobilepost"),
    path("desktoppost/",views.desktoppost,name = "desktoppost"),
    path("embededpost/",views.embededpost,name = "embededpost"),
    path("graphicspost/",views.graphicspost,name = "graphicspost"),
    
    # POSTING PROJECT
    path("projectpost/",views.projectpost,name = "projectpost"),
    
    # POSTING IMAGE
    path("imagepost/",views.imagepost,name = "imagepost"),
    
    # for posting templates
    path("websitetemplatepost/",views.websitetemplatepost,name = "websitetemplatepost"),
    path("mobiletemplatepost/",views.mobiletemplatepost,name = "mobiletemplatepost"),
    path("desktoptemplatepost/",views.desktoptemplatepost,name = "desktoptemplatepost"),
    path("microsofttemplatepost/",views.microsofttemplatepost,name = "microsofttemplatepost"),
    path("adobeposttemplate/",views.adobeposttemplate,name = "adobeposttemplate"),
    
    # url for viewing course
    path('viewwebsite/<str:pk>/', views.viewwebsite.as_view(), name = "viewwebsite"),
    path('viewmobile/<str:pk>/', views.viewmobile.as_view(), name = "viewmobile"),
    path('viewdesktop/<str:pk>/', views.viewdesktop.as_view(), name = "viewdesktop"),
    path('viewembeded/<str:pk>/', views.viewembeded.as_view(), name = "viewembeded"),
    path('viewgraphics/<str:pk>/', views.viewgraphics.as_view(), name = "viewgraphics"),
    
    # VIEW PROJECT
    path('viewproject/<str:pk>/', views.viewproject.as_view(), name = "viewproject"),
    
    # VIEW IMAGE
    path('viewimage/<str:pk>/', views.viewimage.as_view(), name = "viewimage"),
    
    # url for viewing templates
    path("viewwebsitetemplate/<int:id>/",views.viewwebsitetemplate,name = "viewwebsitetemplate"),
    path("viewmobiletemplate/<int:id>/",views.viewmobiletemplate,name = "viewmobiletemplate"),
    path("viewdesktoptemplate/<int:id>/",views.viewdesktoptemplate,name = "viewdesktoptemplate"),
    path("viewmicrosofttemplate/<int:id>/",views.viewmicrosofttemplate,name = "viewmicrosofttemplate"),
    path("viewadobetemplate/<int:id>/",views.viewadobetemplate,name = "viewadobetemplate"),
    
    # url for deleting course
    path('deletewebsite/<int:id>/', views.deletewebsite, name = "deletewebsite"),
    path('deletemobile/<int:id>/', views.deletemobile, name = "deletemobile"),
    path('deletedesktop/<int:id>/', views.deletedesktop, name = "deletedesktop"),
    path('deleteembeded/<int:id>/', views.deleteembeded, name = "deleteembeded"),
    path('deletegraphics/<int:id>/', views.deletegraphics, name = "deletegraphics"),
    
    # DELETE PROJECT
    path('deleteproject/<int:id>/', views.deleteproject, name = "deleteproject"),
    
    # DELETE IMAGE
    path('deleteimage/<int:id>/', views.deleteimage, name = "deleteimage"),
    
    # url for deleting template
    path('deletewebsitetemplate/<int:id>/', views.deletewebsitetemplate, name = "deletewebsitetemplate"),
    path('deletemobiletemplate/<int:id>/', views.deletemobiletemplate, name = "deletemobiletemplate"),
    path('deletedesktoptemplate/<int:id>/', views.deletedesktoptemplate, name = "deletedesktoptemplate"),
    path('deletemicrosofttemplate/<int:id>/', views.deletemicrosofttemplate, name = "deletemicrosofttemplate"),
    path('deleteadobetemplate/<int:id>/', views.deleteadobetemplate, name = "deleteadobetemplate"),
    
    # url for updating courses
    path('updatewebsite/<int:id>/', views.updatewebsite, name = "updatewebsite"),
    path('updatemobile/<int:id>/', views.updatemobile, name = "updatemobile"),
    path('updatedesktop/<int:id>/', views.updatedesktop, name = "updatedesktop"),
    path('updateembeded/<int:id>/', views.updateembeded, name = "updateembeded"),
    path('updategraphics/<int:id>/', views.updategraphics, name = "updategraphics"),
    
    # UPDATING PROJECT
    path('updateproject/<int:id>/', views.updateproject, name = "updateproject"),
    
    # UPDATING IMAGE
    path('updateimage/<int:id>/', views.updateimage, name = "updateimage"),
    
    # url for updating templates
    path('updatewebsitetemplate/<int:id>/', views.updatewebsitetemplate, name = "updatewebsitetemplate"),
    path('updatemobiletemplate/<int:id>/', views.updatemobiletemplate, name = "updatemobiletemplate"),
    path('updatedesktoptemplate/<int:id>/', views.updatedesktoptemplate, name = "updatedesktoptemplate"),
    path('updatemicrosofttemplate/<int:id>/', views.updatemicrosofttemplate, name = "updatemicrosofttemplate"),
    path('updateadobetemplate/<int:id>/', views.updateadobetemplate, name = "updateadobetemplate"),
    
    # FOR PAYMENT
    path('pesapal/transaction/completed/', views.payment_completed, name='payment_completed'),
    
    path('paymentwebsitetemplate/<int:id>/', PaymentViewWebsitetemplate.as_view(), name='paymentwebsitetemplate'),
    path('paymentmobiletemplate/<int:id>/', PaymentViewMobiletemplate.as_view(), name='paymentmobiletemplate'),
    path('paymentdesktoptemplate/<int:id>/', PaymentViewDesktoptemplate.as_view(), name='paymentdesktoptemplate'),
    path('paymentmicrosofttemplate/<int:id>/', PaymentViewMicrosofttemplate.as_view(), name='paymentmicrosofttemplate'),
    path('paymentadobetemplate/<int:id>/', PaymentViewAdobetemplate.as_view(), name='paymentadobetemplate'),
    
    path('paymentwebsite/<int:course_id>/', PaymentViewWebsite.as_view(), name='paymentwebsite'),
    path('paymentmobile/<int:course_id>>/', PaymentViewMobile.as_view(), name='paymentmobile'),
    path('paymentdesktop/<int:course_id>>/', PaymentViewDesktop.as_view(), name='paymentdesktop'),
    path('paymentembeded/<int:course_id>>/', PaymentViewEmbeded.as_view(), name='paymentembeded'),
    path('paymentgraphics/<int:course_id>>/', PaymentViewGraphics.as_view(), name='paymentgraphics'),
    
    path('paymentproject/<int:project_id>>/', PaymentViewProject.as_view(), name='paymentproject'),
    path('paymentimage/<int:image_id>>/', PaymentViewImage.as_view(), name='paymentimage'),

]

