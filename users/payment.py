from django.conf import settings
from mainapp.models import Album
from users.models import AlbumPayment,EventPayment,Event
from django.views.generic import TemplateView,View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from users import functions
        
@login_required
def payment_checkout(request,pk):
    current_payment = AlbumPayment.objects.filter(user = request.user,
                            album =Album.objects.get(id = pk), is_id = True, is_valid = False)
    if request.method =='POST':
            if not current_payment:
                album = Album.objects.get(id = pk)
                txn_id = functions.get_payment_id('al')
                obj = AlbumPayment(user = request.user,transaction_id = txn_id,
                            album =album, is_id = True, cost =album.cost )
                obj.save()
                messages.info(request, f'Make your Payment!')
                payment = AlbumPayment.objects.filter(user = request.user, transaction_id = txn_id)
                payment_pk = payment[0].id
                return redirect('payment',int(payment_pk))

            else: 
                return redirect('payment',int(current_payment[0].id))

    album = Album.objects.get(id = pk)
    context = {
        'album':album,
    }
    return render(request,'users/checkout.html',context)


class FlutterPayView(TemplateView):
    template_name = 'users/flutter.html'
    def get_context_data(self, **kwargs: any):
        job_id =self.kwargs['pk']
        user = self.request.user
        payment = AlbumPayment.objects.filter(id = job_id)

        context = super(FlutterPayView,self).get_context_data(**kwargs)
        context.update({
              'user':user,
            'payment':payment[0],
            'FLUTTER_KEYS':settings.FLUTTER_KEYS
        })
        return context


class PaymentSuccess(View):
  def post(self,request,*args, **kwargs):#here and below
       

        return render(request,'mainapp/payment_succes.html') 
        
  def get(self,request,*args, **kwargs):
    if request.method == 'GET':
      obj = AlbumPayment.objects.get(user =request.user,
                                  transaction_id =request.GET['tx_ref'],
              is_id = True)
      if obj:
        obj.is_valid =True
        obj.save()
        messages.success(request,'Your payment was succesfull')
        return render(request,'users/payment_succes.html')


# Ticket Payment 
        
@login_required
def event_payment_checkout(request,pk):
    current_payment = EventPayment.objects.filter(user = request.user,
                            event =Event.objects.get(id = pk), is_id = True, is_valid = False)
    if request.method =='POST':
            if not current_payment:
                cost = request.POST['choice']
                print('the cost amount is :',cost)
                event = Event.objects.get(id = pk)
                txn_id = functions.get_payment_id('ev')
                obj = EventPayment(user = request.user,transaction_id = txn_id,
                            event =event, is_id = True, cost =cost )
                obj.save()
                messages.info(request, f'Make your Payment!')
                payment = EventPayment.objects.filter(user = request.user, transaction_id = txn_id)
                payment_pk = payment[0].id
                return redirect('eventpayment',int(payment_pk))

            else: 
                return redirect('payment',int(current_payment[0].id))

    event = Event.objects.get(id = pk)
    context = {
        'event':event,
    }
    return render(request,'users/ticket.html',context)


class EventFlutterPayView(TemplateView):
    template_name = 'users/flutter.html'
    def get_context_data(self, **kwargs: any):
        job_id =self.kwargs['pk']
        user = self.request.user
        payment = EventPayment.objects.filter(id = job_id)

        context = super(EventFlutterPayView,self).get_context_data(**kwargs)
        context.update({
              'user':user,
            'payment':payment[0],
            'FLUTTER_KEYS':settings.FLUTTER_KEYS
        })
        return context


class EventPaymentSuccess(View):
  def post(self,request,*args, **kwargs):#here and below
       

        return render(request,'mainapp/payment_succes.html') 
        
  def get(self,request,*args, **kwargs):
    if request.method == 'GET':
      obj = EventPayment.objects.get(user =request.user,
                                  transaction_id =request.GET['tx_ref'],
              is_id = True)
      if obj:
        obj.is_valid =True
        obj.save()
        messages.success(request,'Your payment was succesfull')
        return render(request,'users/payment_succes.html')