from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import *
import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/Loging/")
def index(request):
    company=CompanyInfoM.objects.all()
    return render(request,'index.html',{'company':company})

@login_required(login_url="/Loging/")
def maindashboard(request):
    company = CompanyInfoM.objects.all()
    return render(request,'dashboard.html',{'company':company})
@login_required(login_url="/Loging/")
def accountD(request):
    company = CompanyInfoM.objects.all()
    return render(request,'accounts/dashboard.html',{'company':company})
@login_required(login_url="/Loging/")
def adminD(request):
    company = CompanyInfoM.objects.all()
    return render(request,'admin/dashboard.html',{'company':company})
@login_required(login_url="/Loging/")
def companyinfoV(request):
    company = CompanyInfoM.objects.all()
    return render(request,'admin/companyinfo.html',{'company':company})
@login_required(login_url="/Loging/")
def companyinfosaveV(request):
    name=request.POST.get('name')
    address=request.POST.get('address')
    phone=request.POST.get('phone')
    fax=request.POST.get('fax')
    email=request.POST.get('email')
    if request.method == 'POST' and request.FILES:
        logo_name = request.FILES['logo']
        store = FileSystemStorage()
        filename = store.save(logo_name.name, logo_name)
        profile_pic_url = store.url(filename)
        company = CompanyInfoM(name=name, address=address, phone=phone, Fax=fax, email=email,logo=filename)
        company.save()
        messages.success(request, 'Data save')
        return redirect('/companyinfo/')
    else:
        messages.success(request, 'Data Not Saved')
        return redirect('/companyinfo/')
@login_required(login_url="/Loging/")
def companyinfoeditV(request,id=0):
    company = CompanyInfoM.objects.all()
    if id !=0:
        companyedit = CompanyInfoM.objects.filter(id=id)
    else:
        messages.error(request,'Data not found')
    return render(request,'admin/companyinfoedit.html',{'company':company,'companyedit':companyedit})
@login_required(login_url="/Loging/")
def companyinfoupdateV(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    fax = request.POST.get('fax')
    email = request.POST.get('email')
    if request.method =='POST' and request.FILES:
        logo_name = request.FILES['logo']
        store = FileSystemStorage()
        filename = store.save(logo_name.name, logo_name)
        profile_pic_url = store.url(filename)
        companyupdate=CompanyInfoM.objects.get(id=id)
        companyupdate.name=name
        companyupdate.address=address
        companyupdate.phone=phone
        companyupdate.Fax=fax
        companyupdate.email=email
        companyupdate.logo=filename
        companyupdate.save()
        messages.success(request, 'Data Updated')
    else:
        companyupdate = CompanyInfoM.objects.get(id=id)
        companyupdate.name = name
        companyupdate.address = address
        companyupdate.phone = phone
        companyupdate.Fax = fax
        companyupdate.email = email
        companyupdate.logo=companyupdate.logo
        companyupdate.save()
        messages.success(request, 'Data Updated')
    return redirect('/companyinfo/')
@login_required(login_url="/Loging/")
def companyinfodeleteV(request,id=0):
    if id !=0:
        companydelete=CompanyInfoM.objects.get(pk=id)
        companydelete.delete()
    return redirect('/companyinfo/')


@login_required(login_url="/Loging/")
def EntryV(request):
    company = CompanyInfoM.objects.all()
    client=clientInformation.objects.all()
    producer=producerinformatio.objects.all()
    entry = entryinfo.objects.all()
    return render(request,'accounts/Entry.html', {'client':client,'producer':producer,'entry':entry,'company':company})


@login_required(login_url="/Loging/")
def EntrysaveV(request):

    if request.method == 'POST':
        innumber = request.POST.get('Innumber')
        Idate = request.POST['idate']
        if not Idate:
            a = None
        else:
            a=datetime.datetime.strptime(Idate, '%Y-%m-%d')
        ddate = request.POST['Ddate']
        if not ddate:
            b=None
        else:
            b = datetime.datetime.strptime(ddate, '%Y-%m-%d')

        cname = request.POST.get('cname')
        pname = request.POST.get('pname')
        amount = request.POST.get('amount')
        Codate = request.POST['codate']
        if not Codate:
            c=None
        else:
            c = datetime.datetime.strptime(Codate, '%Y-%m-%d')
        ramount = request.POST.get('ramount')
        if not ramount:
            ram=0
        else:
            ram=ramount
        pret=request.POST.get('pret')
        if not pret:
            pre=0
        else:
            pre=pret

        abc=clientInformation.objects.get(id=cname)
        abcs=producerinformatio.objects.get(id=pname)
        data = entryinfo(Invoice_no=innumber,Invoice_date=a,Delivery_Date=b,Collection_date=c,
                                  Client_Name=abc,Producer_Name=abcs,Amount=amount,Received_Amount=ram,Product_return=pre)
        data.save()
        messages.success(request, 'Data save')

    return redirect('/Entry/')

@login_required(login_url="/Loging/")
def EntryeditV(request,id=0):
    company = CompanyInfoM.objects.all()
    entry = entryinfo.objects.all()
    if id != 0:
        entryedit=entryinfo.objects.filter(pk=id)
    else:
        messages.error(request, 'Data not found')
    return render(request, 'accounts/Entryedit.html', {'entry':entry,'entryedit':entryedit,'company':company})


@login_required(login_url="/Loging/")
def EntryupdateV(request):
    if request.method == 'POST':
        innumber = request.POST.get('Innumber')
        id = request.POST.get('id')
        Idate = request.POST['idate']
        if not Idate:
            a = None
        else:
            a = datetime.datetime.strptime(Idate, '%Y-%m-%d')
        ddate = request.POST['Ddate']
        if not ddate:
            b = None
        else:
            b = datetime.datetime.strptime(ddate, '%Y-%m-%d')

        cname = request.POST.get('cname')
        pname = request.POST.get('pname')
        amount = request.POST.get('amount')
        Codate = request.POST['codate']
        if not Codate:
            c = None
        else:
            c = datetime.datetime.strptime(Codate, '%Y-%m-%d')
        ramount = request.POST.get('ramount')
        if not ramount:
            ram = 0
        else:
            ram = ramount
        pret = request.POST.get('pret')
        if not pret:
            pre = 0
        else:
            pre = pret
        abc = clientInformation.objects.get(id=cname)
        abcs = producerinformatio.objects.get(id=pname)
        entry=entryinfo.objects.get(pk=id)
        entry.Invoice_no=innumber
        entry.Invoice_date=a
        entry.Delivery_Date=b
        entry.Collection_date=c
        entry.Client_Name=abc
        entry.Producer_Name=abcs
        entry.Amount=amount
        entry.Received_Amount=ram
        entry.Product_return=pre
        entry.save()
        messages.success(request, 'Data Updated')
    return redirect('/Entry/')



@login_required(login_url="/Loging/")
def entrydeleteV(request,id=0):
    if id !=0:
        entry=entryinfo.objects.get(pk=id)
        entry.delete()
    return redirect('/Entry/')


@login_required(login_url="/Loging/")
def ClientinfoV(request):
    company = CompanyInfoM.objects.all()
    client=clientInformation.objects.all()
    return render(request,'admin/clientinfo.html',{'client':client,'company':company})



@login_required(login_url="/Loging/")
def ClientinfosaveV(request):
    if request.method=='POST':
        name=request.POST.get('cname')
        address=request.POST.get('caddress')
        phone=request.POST.get('cmobile')

        data=clientInformation(name=name,address=address,phone=phone)
        data.save()
        messages.success(request, 'Data save')
        return redirect('/Client/information/')
    else:
        messages.success(request, 'Data Not save')
        return redirect('/Client/information/')


@login_required(login_url="/Loging/")
def ClientinfoeditV(request,id=0):
    company = CompanyInfoM.objects.all()
    client = clientInformation.objects.all()
    if id != 0:
        clientedit = clientInformation.objects.filter(pk=id)
    else:
        messages.error(request, 'Data not found')
    return render(request, 'admin/clientinfoedit.html', {'clientedit': clientedit,'client':client,'company':company})

@login_required(login_url="/Loging/")
def ClientinfoupdateV(request):
    id = request.POST.get('cid')
    name = request.POST.get('cname')
    address = request.POST.get('caddress')
    phone = request.POST.get('cmobile')
    if request.method =='POST':
        client=clientInformation.objects.get(id=id)
        client.name=name
        client.address=address
        client.phone=phone

        client.save()
        messages.success(request, 'Data Updated')
    else:

        messages.success(request, 'Data Not Updated')
    return redirect('/Client/information/')

@login_required(login_url="/Loging/")
def ClientinfodeleteV(request,id=0):
    if id !=0:
        companydelete=clientInformation.objects.get(pk=id)
        companydelete.delete()
    return redirect('/Client/information/')

@login_required(login_url="/Loging/")
def ProducerinfoV(request):
    company = CompanyInfoM.objects.all()
    producer=producerinformatio.objects.all()
    return render(request,'admin/producer.html',{'producer':producer,'company':company})


@login_required(login_url="/Loging/")
def ProducerinfosaveV(request):
    if request.method=='POST':
        name=request.POST.get('pname')
        designation=request.POST.get('pdesignation')
        address=request.POST.get('paddress')
        phone=request.POST.get('pmobile')

        data=producerinformatio(name=name,designation=designation,address=address,phone=phone)
        data.save()
        messages.success(request, 'Data save')
        return redirect('/Producer/information/')
    else:
        messages.success(request, 'Data Not save')
        return redirect('/Producer/information/')


@login_required(login_url="/Loging/")
def ProducerinfoeditV(request,id=0):
    company = CompanyInfoM.objects.all()
    producer = producerinformatio.objects.all()
    if id != 0:
        pro = producerinformatio.objects.filter(pk=id)
    else:
        messages.error(request, 'Data not found')
    return render(request, 'admin/produceredit.html', {'producer': producer,'pro':pro,'company':company})

@login_required(login_url="/Loging/")
def ProducerinfoupdateV(request):
    id = request.POST.get('pid')
    name = request.POST.get('pname')
    designation = request.POST.get('pdesignation')
    address = request.POST.get('paddress')
    phone = request.POST.get('pmobile')
    if request.method =='POST':
        producer=producerinformatio.objects.get(id=id)
        producer.name=name
        producer.name=designation
        producer.address=address
        producer.phone=phone

        producer.save()
        messages.success(request, 'Data Updated')
    else:

        messages.success(request, 'Data Not Updated')
    return redirect('/Producer/information/')

@login_required(login_url="/Loging/")
def ProducerinfodeleteV(request,id=0):
    if id !=0:
        companydelete=producerinformatio.objects.get(pk=id)
        companydelete.delete()
    return redirect('/Client/information/')




@login_required(login_url="/Loging/")
def CreportV(request):

    invoice_date=request.POST.get('idate')
    a = datetime.datetime.strptime(invoice_date, '%Y-%m-%d')
    invoice_edate=request.POST.get('edate')
    client=request.POST.get('cname')
    b = datetime.datetime.strptime(invoice_edate, '%Y-%m-%d')
    company=CompanyInfoM.objects.all()

    entry = entryinfo.objects.raw('select id,Invoice_no,(amount-Received_Amount) as dues from accounting_entryinfo where Invoice_date between %s  and %s and Client_Name_id=%s',[invoice_date,invoice_edate,client])
    entrysum = entryinfo.objects.raw('select id,Invoice_no,sum(amount) as amount,sum(Received_Amount) as ra, sum(amount-Received_Amount) as due, sum(Product_return) as Product_return from accounting_entryinfo where Invoice_date between %s  and %s and Client_Name_id=%s',[invoice_date,invoice_edate,client])
    template_path = 'pdfReport/ClientWisereport.html'
    context = {'entry': entry,'invoice_date':invoice_date,'invoice_edate':invoice_edate,'entrysum':entrysum,'company':company}
    response = HttpResponse(content_type='application/pdf')
    #for downlode
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url="/Loging/")
def client_wiseV(request):
    company = CompanyInfoM.objects.all()
    client = clientInformation.objects.all()
    return render(request,'accounts/Clientwise.html',{'client':client,'company':company})


@login_required(login_url="/Loging/")
def Producer_wiseV(request):
    company = CompanyInfoM.objects.all()
    producer = producerinformatio.objects.all()
    return render(request,'accounts/Producerwise.html',{'producer':producer,'company':company})


@login_required(login_url="/Loging/")
def preportV(request):

    invoice_date = request.POST.get('idate')
    a = datetime.datetime.strptime(invoice_date, '%Y-%m-%d')
    invoice_edate = request.POST.get('edate')
    producer = request.POST.get('cname')
    b = datetime.datetime.strptime(invoice_edate, '%Y-%m-%d')
    company=CompanyInfoM.objects.all()
    entry = entryinfo.objects.raw('select id,*,(amount-Received_Amount) as dues,Product_return from accounting_entryinfo where Invoice_date between %s  and %s and producer_Name_id=%s',[invoice_date, invoice_edate, producer])
    entrysum = entryinfo.objects.raw('select id,sum(amount) as amount,sum(Received_Amount) as ra, sum(amount-received_amount) as due, sum(Product_return) as Product_return from accounting_entryinfo where Invoice_date between %s  and %s and producer_Name_id=%s',[invoice_date, invoice_edate, producer])
    template_path = 'pdfReport/ProducertWisereport.html'
    context = {'entry': entry, 'invoice_date': invoice_date, 'invoice_edate': invoice_edate,'entrysum':entrysum,'company':company}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required(login_url="/Loging/")
def CollectionReportV(request):
    company = CompanyInfoM.objects.all()
    return render(request,'accounts/Collection.html',{'company':company})


@login_required(login_url="/Loging/")
def collectionV(request):
    invoice_date = request.POST.get('idate')
    invoice_edate = request.POST.get('edate')
    company=CompanyInfoM.objects.all()
    entry = entryinfo.objects.raw('select a.id,a.Invoice_no as Invoice_no,a.Invoice_date as Invoice_date,a.Delivery_Date as Delivery_Date,a.Collection_date as Collection_date,a.Client_Name_id as Client_Name_id,a.Producer_Name_id as Producer_Name_id, x.amount as Amount,a.Received_Amount as Received_Amount,x.Received_Amount as Total_Collection, x.due,x.Product_return from'
                                    '( SELECT id,Invoice_no,Invoice_date,Delivery_Date,Collection_date,Client_Name_id,Producer_Name_id,sum(Amount) as amount,sum(Received_Amount) as Received_Amount  from accounting_entryinfo '
                                    'where Collection_date BETWEEN %s and %s '
                                    'group by Invoice_no) a '
                                    'left join '
                                    '(SELECT Invoice_no,sum(Amount) as amount,sum(Received_Amount) as Received_Amount,sum(amount-Received_Amount) as due,sum(Product_return) as Product_return  from accounting_entryinfo '
                                    'group by Invoice_no) x '
                                    'on a.Invoice_no =x.Invoice_no',[invoice_date, invoice_edate])
    template_path = 'pdfReport/collection.html'
    context = {'entry': entry, 'invoice_date': invoice_date, 'invoice_edate': invoice_edate,'company':company}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url="/Loging/")
def DuesReportV(request):
    company = CompanyInfoM.objects.all()
    return render(request,'accounts/Dues.html',{'company':company})


@login_required(login_url="/Loging/")
def DuesV(request):
    invoice_date = request.POST.get('idate')
    a=datetime.datetime.strptime(invoice_date, '%Y-%m-%d')
    invoice_edate = request.POST.get('edate')
    b=datetime.datetime.strptime(invoice_edate, '%Y-%m-%d')
    company = CompanyInfoM.objects.all()
    entry = entryinfo.objects.raw(
        'select a.id,a.Invoice_no as Invoice_no,a.Invoice_date as Invoice_date,a.Delivery_Date as Delivery_Date,a.Collection_date as Collection_date,a.Client_Name_id as Client_Name_id,a.Producer_Name_id as Producer_Name_id, x.amount as Amount,a.Received_Amount as Received_Amount,x.Received_Amount as Total_Collection,x.Total_dues as Total_dues,x.Product_return from'
        '( SELECT id,Invoice_no,Invoice_date,Delivery_Date,Collection_date,Client_Name_id,Producer_Name_id,sum(Amount) as amount,sum(Received_Amount) as Received_Amount  from accounting_entryinfo '
        'where Collection_date BETWEEN %s and %s '
        'group by Invoice_no) a '
        'left join '
        '(SELECT Invoice_no,sum(Amount) as amount,sum(Received_Amount) as Received_Amount,sum(Amount)-sum(Received_Amount) as Total_dues,sum(Product_return) as Product_return  from accounting_entryinfo '
        'group by Invoice_no) x '
        'on a.Invoice_no =x.Invoice_no', [a, b])
    template_path = 'pdfReport/Duesreport.html'
    context = {'entry': entry, 'invoice_date': invoice_date, 'invoice_edate': invoice_edate,'company':company}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def LogingV(request):
    company = CompanyInfoM.objects.all()
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['pass']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if 'next' in request.POST:
                # return redirect(request.POST.get('next'))
                return redirect('/')
            else:
                return redirect('/')
        else:
            messages.info(request,'User is not valide')
            return redirect('/Loging/')
    else:
        return render(request,'loging.html',{'company':company})



def logoutV (request):
    auth.logout(request)
    return redirect('/')
@login_required(login_url="/Loging/")
def SingupV(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name already taken')
                return redirect('/Singup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'E-Mail already taken')
                return redirect('/Singup/')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'password donot match')
            return redirect('/Singup/')
    else:
        return render(request,'admin/singup.html')

def partpayment(request):
    if request.method=='POST':
        inv=request.POST.get('search')
        call=entryinfo.objects.raw('SELECT DISTINCT id,* from accounting_entryinfo'
                                    ' WHERE Invoice_no = %s '
                                    'group by Invoice_no',[inv])
        return render(request,'accounts/partpayment.html',{'call':call})
    return render(request, 'accounts/partpayment.html')

def paymentsave(request):
    if request.method == 'POST':
        innumber = request.POST.get('Innumber')
        Idate = request.POST['idate']
        if not Idate:
            a = None
        else:
            a = datetime.datetime.strptime(Idate, '%Y-%m-%d')
        ddate = request.POST['Ddate']
        if not ddate:
            b = None
        else:
            b = datetime.datetime.strptime(ddate, '%Y-%m-%d')

        cname = request.POST.get('cname')
        pname = request.POST.get('pname')
        Codate = request.POST['codate']
        if not Codate:
            c = None
        else:
            c = datetime.datetime.strptime(Codate, '%Y-%m-%d')
        ramount = request.POST.get('ramount')
        if not ramount:
            ram=0
        else:
            ram=ramount
        preturn=request.POST.get('preturn')
        if not preturn:
            pret=0
        else:
            pret=preturn

        abc = clientInformation.objects.get(id=cname)
        abcs = producerinformatio.objects.get(id=pname)
        data = entryinfo(Invoice_no=innumber, Invoice_date=a, Delivery_Date=b, Collection_date=c,
                         Client_Name=abc, Producer_Name=abcs,Amount=0, Received_Amount=ram,Product_return=pret)
        data.save()
        messages.success(request, 'Data save')
    return redirect('/part/payment/')


# from django.http import HttpResponse
# from django.views.generic import View
#
# from .utils import render_to_pdf #created in step 4
#
# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(),
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('pdf/invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')
#
#
#
#
#
#
