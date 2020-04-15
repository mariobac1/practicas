from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from ingenierias.models import IngenieriaGSM, IngenieriaUMTS, IngenieriaLTE
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
#import xlwt
#from django.contrib.auth.models import User

import xlsxwriter
#import StringIO
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
adjunto1 = 0
adjunto2 = 0
adjunto3 = 0
def welcome(request):
    if request.user.is_authenticated:
        ahora=datetime.datetime.now()
        return render(request,"busqueda_ingenierias.html", {"ahora":ahora})
    return redirect('/login')

def login(request):
    form = AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "login.html",{'form':form})

def logut(request):
    do_logout(request)
    return redirect('/')



def WriteExcel(tecnologia,sitio):
    #output=StringIO.StringIO()
    if tecnologia==2:
        nombre='/home/mariobac1/ingenieriaGSM.xlsx'
    if tecnologia==3:
        nombre='/home/mariobac1/ingenieriaUMTS.xlsx'
    if tecnologia==4:
        nombre='/home/mariobac1/ingenieriaLTE.xlsx'
    
    sitios=sitio.replace(",","")
    sitios=sitios.replace(" ","")
    workbook= xlsxwriter.Workbook(nombre)
    worksheet= workbook.add_worksheet('ingenierias')
    row_num= 0
    num= 0
    a=0
    b=4
    header = workbook.add_format({
        'bg_color': '#00FF00',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
        })
    if tecnologia==2:
        columns= ['Sector', 'Btsname', 'Cellname','CellID', 'Latitud','Longitud',
        'SiteName','FrequencyBand','TRXs','AntennaType','AntennaHeight','Azimuth',
        'MechDownTilt','ElecDownTilt','SiteType','BSCID','MCC','MNC','LAC','RAC','BCCHFD',
        'TCH','BSICbaseoctal','NCC','BCC','HSN','MAIO','PowerW','PowerdBm','Departamento',
        'Municipio','Area','Encargado','Telefono','RET','Ganancia','Apertura']
        

    if tecnologia==3:
        columns= ['NodeBName','Cellname', 'Latitud','Longitud','SiteCommonName',
        'SiteName','RNC','RNCID','CELLID', 'LAC','RAC','SAC','URAID','UARFCNUPLINK','UARFCNDOWNLINK','PSC',
        'CPICHPOWER','AntennaType','AntennaHeight','Azimuth','MechDownTilt','ElecDownTilt','SiteType',
        'RET','IPCKL','Departamento','Municipio','Area','Encargado','Telefono','RET','Ganancia','Apertura']
        
    
    if tecnologia==4:
        columns= ['EnodeBName','CellIndex','Cell','Nombre','Latitud',
        'Longitud','Departamento','Municipio','Area', 'Encargado','Telefono',
        'Azimuth','AntennaHeight','MechDownTilt','ElecDownTilt','PCI','MinRootSequency','TAC','TAL',
        'EARFCN_DL','EARFCN_UL','RSpower','AntennaType','RET','Estructura','Ganancia','Apertura']
        

    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],header)

    for y in sitios:
        celdas=sitios[a:b]
        if celdas !='':
            a +=4
            b +=4
            print(celdas)
            if tecnologia==2:
                data= IngenieriaGSM.objects.filter(Cellname__icontains=celdas).values_list('Sector', 'Btsname', 'Cellname','CellID', 'Latitud','Longitud',
                'SiteName','FrequencyBand','TRXs','AntennaType','AntennaHeight','Azimuth',
                'MechDownTilt','ElecDownTilt','SiteType','BSCID','MCC','MNC','LAC','RAC','BCCHFD',
                'TCH','BSICbaseoctal','NCC','BCC','HSN','MAIO','PowerW','PowerdBm','Departamento',
                'Municipio','Area','Encargado','Telefono','RET','Ganancia','Apertura')

            if tecnologia==3:
                data= IngenieriaUMTS.objects.filter(Cellname__icontains=celdas).values_list('NodeBName','Cellname', 'Latitud','Longitud','SiteCommonName',
                'SiteName','RNC','RNCID','CELLID', 'LAC','RAC','SAC','URAID','UARFCNUPLINK','UARFCNDOWNLINK','PSC',
                'CPICHPOWER','AntennaType','AntennaHeight','Azimuth','MechDownTilt','ElecDownTilt','SiteType',
                'RET','IPCKL','Departamento','Municipio','Area','Encargado','Telefono','RET','Ganancia','Apertura')

            if tecnologia==4:
                data= IngenieriaLTE.objects.filter(EnodeBName__icontains=celdas).values_list('EnodeBName','CellIndex','Cell','Nombre','Latitud',
                'Longitud','Departamento','Municipio','Area', 'Encargado','Telefono',
                'Azimuth','AntennaHeight','MechDownTilt','ElecDownTilt','PCI','MinRootSequency','TAC','TAL',
                'EARFCN_DL','EARFCN_UL','RSpower','AntennaType','RET','Estructura','Ganancia','Apertura')
            for row in data:
                row_num += 1
                for col_num in range(len(row)):
                    worksheet.write(row_num, col_num, row[col_num])
            formato = workbook.add_format()
            formato.set_num_format('00.0')
            if tecnologia==2:
                for row in data:
                    num +=1
                    #formato = workbook.add_format()
                    #formato.set_num_format('00.0')
                    worksheet.write(num, 28, row[28], formato)
                    formato2 = workbook.add_format()
                    formato2.set_num_format('00')
                    worksheet.write(num,22, row[22], formato2)

            if tecnologia==3:
                for row in data:
                    num +=1
                    #formato = workbook.add_format()
                    #formato.set_num_format('00.0')
                    worksheet.write(num, 16, row[16], formato)
            
            if tecnologia==4:
                for row in data:
                    num +=1
                    #formato = workbook.add_format()
                    #formato.set_num_format('00.0')
                    worksheet.write(num, 21, row[21], formato)
    
    workbook.close()
    xlsx_data= 1
    return xlsx_data

'''def export_users_xls(request):
    response =HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']= 'attachment; filename="ingenierias.xls' 
    wb= xlwt.Workbook(encoding='utf-8')
    ws= wb.add_sheet('users')

    row_num= 0
    font_style= xlwt.XFStyle()
    font_style.font.bold= True

    columns= ['Sector','bts name','cell name',' latitud', 'powerdBm']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle() 
    #rows = IngenieriaGSM.objects.filter(Cellname__icontains="2181").values_list('Sector', 'Btsname', 'Cellname', 'Latitud','PowerdBm')
    rows = IngenieriaGSM.objects.all().values_list('Sector', 'Btsname', 'Cellname', 'Latitud','PowerdBm')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save('/home/mariobac1/excel.xls')
    wb.save(response)
    return response'''

'''def export_users_xls(request):
    response =HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']= 'attachment; filename="users.xls' 
    wb= xlwt.Workbook(encoding='utf-8')
    ws= wb.add_sheet('users')

    row_num= 0
    font_style= xlwt.XFStyle()
    font_style.font.bold= True

    columns= ['Username','First name','Last name','Email address']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle() 
    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response'''


#@login_required
'''def busqueda_ingenierias(request):
    ahora=datetime.datetime.now()
    return render(request,"busqueda_ingenierias.html", {"ahora":ahora})'''

@login_required
def search(request):
    global adjunto1, adjunto2, adjunto3    
    if request.GET["sitio"]:
        #if request.GET["tecnologia"]:
        #tecnologia=request.GET.get("tecnologia",False)
        tecno1=request.GET.get("tecno2g",False)
        tecno2=request.GET.get("tecno3g",False)
        tecno3=request.GET.get("tecno4g",False)
        ahora=datetime.datetime.now()
        sitio=request.GET["sitio"]
        if tecno1 !="2" and tecno2 !="3" and tecno3 !="4":
            mesage= "<h1>seleccione una tecnologia</h1>"
            return HttpResponse(mesage)

        if tecno1 == "2":
            WriteExcel(2,sitio)
            #ide=IngenieriaGSM.objects.filter(Cellname__icontains=sitio)
        #else:
            #ide = ""

        if tecno2 == "3":
            WriteExcel(3,sitio)
            #ide2=IngenieriaUMTS.objects.filter(Cellname__icontains=sitio)
        #else:
            #ide2 = ""

        if tecno3 == "4":
            WriteExcel(4,sitio)
            #ide3=IngenieriaLTE.objects.filter(EnodeBName__icontains=sitio)
            #ide3='2'
        #else:
            #ide3 = ""
        a=0
        b=4
        name=''
        name2=''
        name3=''
        sitios=sitio.replace(",","")
        sitios=sitios.replace(" ","")
        for y in sitios:
            celdas=sitios[a:b]
            if celdas !='':
                a +=4
                b +=4
                if tecno1=="2":
                    ide= IngenieriaGSM.objects.filter(Cellname__icontains=celdas)
                    for nombre in ide:
                        #name= nombre.SiteName
                        name = name + nombre.SiteName +"  ||  "
                    #nombre = nombre + ide.SiteName 
                else:
                    ide=''
                if tecno2=="3":
                    ide2= IngenieriaUMTS.objects.filter(Cellname__icontains=celdas)
                    for nombre2 in ide2:
                        name2 = name2 + nombre2.SiteName + "||"
                else:
                    ide2=''
                if tecno3=="4":
                    ide3= IngenieriaLTE.objects.filter(EnodeBName__icontains=celdas)
                    for nombre3 in ide3:
                        name3 = name3 + nombre3.Nombre +"||"
                else:
                    ide3=''


        correo_usuario= request.user.email
        mail = EmailMessage(
        'Claro Ingenierias',
        'Se adjunta correo con las ingenierias requeridas este mensaje es automatico, favor no responder.',
        'josepablomarroquin@gmail.com',
        [correo_usuario,'mario.moralesbac1@gmail.com'],
        )
        if tecno1=="2" and name:
            adjunto1= 1
            #mail.attach_file('/home/mariobac1/ingenieriaGSM.xlsx')
        if tecno2=="3" and name2:
            adjunto2= 2
            #mail.attach_file('/home/mariobac1/ingenieriaUMTS.xlsx')
        if tecno3=="4" and name3:
            adjunto3= 3
            #mail.attach_file('/home/mariobac1/ingenieriaLTE.xlsx')
        #mail.send(fail_silently=False)
        return render(request,"resultado.html",{"ahora":ahora,"name":name,"tecno1":tecno1, "name2":name2,"name3":name3,
        "tecno2":tecno2,"tecno3":tecno3, "ide":ide, "ide2":ide2, "ide3":ide3, "query":sitio,"adjunto2":adjunto2 })     
        

    else:
        mensaje="<h1>no se introdujo nada</h1>"
    return HttpResponse(mensaje)

@login_required
def index(request):
    global adjunto1, adjunto2, adjunto3
    correo_usuario= request.user.email
    mail = EmailMessage(
    'Claro Ingenierias',
    'Se adjunta correo con las ingenierias requeridas este mensaje es automatico, favor no responder.',
    'josepablomarroquin@gmail.com',
    [correo_usuario,'mario.moralesbac1@gmail.com'],
    )
    if adjunto1==1:
        mail.attach_file('/home/mariobac1/ingenieriaGSM.xlsx')
        adjunto1= 0
    if adjunto2==2:
        mail.attach_file('/home/mariobac1/ingenieriaUMTS.xlsx')
        adjunto2= 0
    if adjunto3==3:
        mail.attach_file('/home/mariobac1/ingenieriaLTE.xlsx')
        adjunto3= 0
    mail.send(fail_silently=False)
    return render(request, 'index.html')