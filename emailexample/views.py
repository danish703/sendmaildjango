from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages
def mailtest(request):
    if request.method=='GET':
        return render(request,'form.html')
    else:
        toemail = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        name = request.POST.get('name')
        context = {
            'email':toemail,
            'subject':subject,
            'message':message,
            'name':name,
        }
        emailtemplate = get_template('emailtemplate.html').render(context)
        msg = EmailMessage(
            subject=subject,
            body=emailtemplate,
            from_email='mmmddd.dk@gmail.com',
            to=[toemail,]
        )
        msg.content_subtype='html'
        try:
            msg.send()
            messages.success(request,"Successfully message sent")
            return redirect('sendmail')
        except:
            messages.error(request,'error occur')
            return redirect('sendmail')