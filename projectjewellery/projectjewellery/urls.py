"""projectjewellery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from jeweapp.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	
	url(r'^$',TemplateView.as_view(template_name ='index.html')),
	
	url(r'^custhome/$',TemplateView.as_view(template_name ='customerhome.html')),
	url(r'^staffhome/$',TemplateView.as_view(template_name ='staffhome.html')),
	
	url(r'^report/$',TemplateView.as_view(template_name ='orderreport.html')),
		  
    url(r'^admin/', include(admin.site.urls)),

	


	url(r'^home/',home,name="home"),

	url(r'^customer/',customer,name="customer"),
	url(r'^customeraction/',customeraction,name="customeraction"),
	url(r'^viewcustomer/',viewcustomer,name="viewcustomer"),
	url(r'^uactivate/$',uactivate,name='uactivate'),

	url(r'^login/',login,name="login"),
	url(r'^searchlogin/$',searchlogin,name='searchlogin'),




	url(r'^adminhome/',adminhome,name="adminhome"),

	url(r'^category/',category,name="category"),
	url(r'^categoryaction/',categoryaction,name="categoryaction"),
	url(r'^viewcategory/',viewcategory,name="viewcategory"),
	url(r'^delcat/$',delcat,name='delcat'),
	url(r'^editcat/$',editcat,name='editcat'),
	url(r'^updatecat/$',updatecat,name='updatecat'),

	url(r'^subcategory/',subcategory,name="subcategory"),
	url(r'^subcategoryaction/',subcategoryaction,name="subcategoryaction"),
	url(r'^viewsubcategory/',viewsubcategory,name="viewsubcategory"),
	url(r'^delsubcat/$',delsubcat,name='delsubcat'),
	url(r'^editsubcat/$',editsubcat,name='editsubcat'),
	url(r'^updatesubcat/$',updatesubcat,name='updatesubcat'),

	url(r'^rate/',rate,name="rate"),
	url(r'^rateaction/',rateaction,name="rateaction"),
	url(r'^viewrate/',viewrate,name="viewrate"),
	url(r'^delrate/$',delrate,name='delrate'),
	url(r'^editrate/$',editrate,name='editrate'),
	url(r'^updaterate/$',updaterate,name='updaterate'),

	url(r'^item/',item,name="item"),
	url(r'^itemaction/',itemaction,name="itemaction"),
	url(r'^viewitem/',viewitem,name="viewitem"),
	url(r'^delprod/$',delprod,name='delprod'),
	url(r'^editprod/$',editprod,name='editprod'),
	url(r'^updateprod/$',updateprod,name='updateprod'),

	url(r'^staff/',staff,name="staff"),
	url(r'^staffaction/',staffaction,name="staffaction"),
	url(r'^viewstaff/',viewstaff,name="viewstaff"),
	url(r'^editstaff/$',editstaff,name='editstaff'),
	url(r'^updatestaff/$',updatestaff,name='updatestaff'),
	url(r'^sactivate/$',sactivate,name='sactivate'),
	
	url(r'^vendor/',vendor,name="vendor"),
	url(r'^vendoraction/',vendoraction,name="vendoraction"),
	url(r'^viewvendor/',viewvendor,name="viewvendor"),
	url(r'^delvendr/$',delvendr,name='delvendr'),
	url(r'^editvendor/$',editvendor,name='editvendor'),
	url(r'^updatevendor/$',updatevendor,name='updatevendor'),

	url(r'^purchasemaster/',purchasemaster,name="purchasemaster"),
	url(r'^purchasemasteraction/',purchasemasteraction,name="purchasemasteraction"),
	url(r'^viewpurchasemaster/',viewpurchasemaster,name="viewpurchasemaster"),
	
	url(r'^purchasechild/',purchasechild,name="purchasechild"),
	url(r'^purchasechildaction/',purchasechildaction,name="purchasechildaction"),
	url(r'^viewpurchasechild/',viewpurchasechild,name="viewpurchasechild"),
	url(r'^delpchild/$',delpchild,name='delpchild'),
	
	url(r'^porder/$',porder,name='porder'),
	url(r'^assign/$',assign,name='assign'),	
	
	url(r'^orderreport/$',orderreport,name='orderreport'),
	url(r'^staffreport/$',staffreport,name='staffreport'),
	url(r'^venreport/$',venreport,name='venreport'),
	url(r'^purreport/$',purreport,name='purreport'),

	url(r'^logout/$',logout,name='logout'),



	
	url(r'^vproduct/$',vproduct,name='vproduct'),
	
	url(r'^pdetails/$',pdetails,name='pdetails'),
	
	url(r'^cart/$',cart,name='cart'),
	url(r'^vcart/$',vcart,name='vcart'),
	url(r'^delcart/$',delcart,name='delcart'),
	
	url(r'^upcart/$',upcart,name='upcart'),
	
	url(r'^myorder/$',myorder,name='myorder'),
	
	
	
	
	url(r'^aorders/$',aorders,name='aorders'),
	
	
	
	
	url(r'^buyaction/$',buyaction,name='buyaction'),
	url(r'^status/$',status,name='status'),
	url(r'^salereport/$',salereport,name='salereport'),
	
	
	
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()