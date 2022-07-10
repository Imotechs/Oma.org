from django.conf import settings
from mainapp.models import Album
from users.models import AlbumPayment,EventPayment,Event
from django.views.generic import TemplateView,View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from users import functions
from users.models import Account

        
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


class AlbumPayView(TemplateView):
    template_name = 'users/paystack.html'
    def get_context_data(self, **kwargs: any):
        job_id =self.kwargs['pk']
        user = self.request.user
        payment = AlbumPayment.objects.filter(id = job_id)

        context = super(AlbumPayView,self).get_context_data(**kwargs)
        context.update({
              'user':user,
            'payment':payment[0],
            'PAYSTACK_PUBLICK_KEYS':settings.PAYSTACK_PUBLICK_KEYS,

        })
        return context


class PaymentSuccess(View):
        
  def get(self,request,*args, **kwargs):
    if request.method == 'GET':
      ref = kwargs['ref']
      obj = AlbumPayment.objects.get(user =request.user,
                                  transaction_id = ref,
              is_id = True,is_valid = False)
      verified = obj.verify_payment()
      if verified:
        user = obj.album.user
        account,created = Account.objects.get_or_create(user = user)
        account.balance = account.balance + functions.get_album_cent(obj.cost)
        account.save()
        messages.success(request,'Varification succesfull')
        return render(request,'users/payment_succes.html')
      else:
          messages.success(request,'Varification failed!!!')
          return redirect('profile')



# Ticket Payment 
        
@login_required
def event_payment_checkout(request,pk):
    current_payment = EventPayment.objects.filter(user = request.user,
                            event =Event.objects.get(id = pk), is_id = True, is_valid = False)
    if request.method =='POST':
            if not current_payment:
                cost = request.POST['choice']
                event = Event.objects.get(id = pk)
                txn_id = functions.get_payment_id('ev')
                event_code = functions.get_event_code()
                obj = EventPayment(user = request.user,transaction_id = txn_id,
                            event =event, is_id = True, 
                            cost =cost,event_code = event_code 
                            )
                obj.save()
                payment = EventPayment.objects.filter(user = request.user, transaction_id = txn_id)
                payment_pk = payment[0].id
                return redirect('eventpayment',int(payment_pk))

            else: 
                cost = request.POST['choice']
                event = Event.objects.get(id = pk)
                txn_id = functions.get_payment_id('ev')
                event_code = functions.get_event_code()
                obj = EventPayment(user = request.user,
                            transaction_id = txn_id,
                            event =event, is_id = True, 
                            cost =cost,
                            event_code = event_code
                            )
                obj.save()
                payment = EventPayment.objects.filter(user = request.user, transaction_id = txn_id)
                payment_pk = payment[0].id
                return redirect('eventpayment',int(payment_pk))

    event = Event.objects.get(id = pk)
    context = {
        'event':event,
    }
    return render(request,'users/ticket.html',context)


class EventPayView(TemplateView):
    template_name = 'users/paystack1.html'
    def get_context_data(self, **kwargs: any):
        job_id =self.kwargs['pk']
        user = self.request.user
        payment = EventPayment.objects.filter(id = job_id)

        context = super(EventPayView,self).get_context_data(**kwargs)
        context.update({
              'user':user,
            'payment':payment[0],
            'PAYSTACK_PUBLICK_KEYS':settings.PAYSTACK_PUBLICK_KEYS,
        })
        return context


class EventPaymentSuccess(View):
      
  def get(self,request,*args, **kwargs):
    if request.method == 'GET':
      ref = kwargs['ref']
      obj = EventPayment.objects.get(user =request.user,
                                  transaction_id = ref,
              is_id = True,is_valid = False)
      verified = obj.verify_payment()
      if verified:
        user = obj.event.user
        account,created = Account.objects.get_or_create(user = user)
        account.balance = account.balance + functions.get_event_cent(obj.cost)
        account.save()
        context = {
          'event':obj
        }
        messages.success(request,'Varification succesfull')
        return render(request,'users/event_payment_succes.html',context)
      else:
          messages.success(request,'Varification failed!!!')
          return redirect('profile')