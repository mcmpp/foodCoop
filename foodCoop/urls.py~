from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<member_id>[0-9]+)/member/$',views.detailMember , name='member details'),

    url(r'^(?P<share_id>[0-9]+)/member/$', views.detailOrder, name='order details'),

    url(r'^(?P<payment_id>[0-9]+)/member/$', views.detailPayment, name='payment details'),

    url(r'^members/$', views.listMember, name='list of members'),

    url(r'^shares/$', views.listOrders, name='list of orders'),

    url(r'^payments/$', views.listPayment_Member, name='list of payments made by a member'),
]
