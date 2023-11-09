from django.conf import settings
from django.shortcuts import render
import segno
#import io
import os
import random
#from datetime import datetime
#from .models import Qrgen
from qrgen.models import Qrgen
# Create your views here.


def qrgen_home(request):
    # basic_qrcode.py
    
    #out = io.BytesIO()
    
    #carica_qr = Qrgen.objects.create(titolo='qrtest', image=qrout)
    
    #image = base64.b64encode(qrout).decode()
    # restituisce in output il dizionario utilizzando il template project_index.html
    return render(request, "qrgen/home.html")
    #return render(request, 'qrgen/home.html', {'qrcode2': image})
    #return HttpResponse(image, content_type="image/png")


def qrgen_result(request):
    
    # recupero variabili da pagina home.html
    content_fromhtml = request.POST.get('content','')
    backcolor_fromhtml = request.POST.get('backcolor','value')
    datacolor_fromhtml = request.POST.get('datacolor','value')

    # utilizzo variabili per generare qrcode
    qrcode = segno.make(str(content_fromhtml))
    
    # immagine salvata (in sovrascrittura) nella cartella uploads
    path = os.path.join(settings.MEDIA_ROOT, 'qrgen_images/qrgen.png')
    qrcode.save(path, kind='png', scale=10,dark=datacolor_fromhtml,light=backcolor_fromhtml)
    
    # update del record nel db tramite modello definito in models.py
    Qrgen.objects.filter(pk=1).update(contenuto=content_fromhtml)

    # viene recuperato record 1 nella tabella
    qrgen = Qrgen.objects.get(pk=1)
    context = {

        "qrgen": qrgen

    }

    # restituisce in output il dizionario utilizzando il template project_detail.html
    return render(request, "qrgen/result.html", context)