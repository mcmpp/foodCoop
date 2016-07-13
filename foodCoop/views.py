from django.http import HttpResponse
from .models import Member

def detailMember(request, member_id):
    try:
        myMember = Member.object.get(pk=member_id)
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    return HttpResponse("this is the member %s ", % member_id)

def detailOrder(request, order_id):
    myOrder = get_object_or_404(Order, pk=order_id)
    return HttpResponse("this is the order %s ", % order_id)

def detailPayment(request, payment_id):
    myPayment = get_object_or_404(Payment, pk=payment_id)
    return HttpResponse("this is the payment %s ", % payment_id)

def listMember(request):
    listOfMembers = get_object_or_404(Payment,pk=mem )
    return HttpResponse("this is the list of members", % listOfMembers)

def listOrders(request,order_id):
    myPayment = get_object_or_404(Payment, pk=payment_id)
    return HttpResponse("this is the list of possible order")

def listPayment_Member(request,member_id):
    myPayment = get_object_or_404(Payment, pk=payment_id)
    return HttpResponse("this is the list of payments made by a member")
