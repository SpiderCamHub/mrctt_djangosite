from django.shortcuts import render

from projects.models import Project

# funzione che restituisce una vista generale della tabella


def project_home(request):

    # fa una query per ottenere tutti i record nella tabella Project
    projects = Project.objects.all()

    # crea un dizionario Python con  il risultato della query
    # https://realpython.com/python-dicts/
    context = {

        "projects": projects

    }

    # restituisce in output il dizionario utilizzando il template project_index.html
    return render(request, "projects/home.html", context)

# funzione che restituisce una vista dettagliata di un record della tabella


def project_detail(request, pk):

    # fa una query per ottenere un record specifico della tabella
    project = Project.objects.get(pk=pk)

    context = {

        "project": project

    }

    # restituisce in output il dizionario utilizzando il template project_detail.html
    return render(request, "projects/detail.html", context)

def project_link(request, link):

    # fa una query per ottenere un record specifico della tabella
    project = Project.objects.get(link=link)

    newurl = link

    # restituisce in output il dizionario utilizzando il template project_detail.html
    return render(request, link+"/home.html")
