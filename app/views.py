from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from app.models import Tvshow

def index(request):
    return redirect('/shows')

def shows(request):
    if request.method == 'GET':
        contexto = {
            'shows': Tvshow.objects.all()
        }
        return render(request, 'shows.html', contexto)    

def nuevo(request):
    return render(request, 'nuevo.html')

def editar(request, id):
    print(f"=== EDITAR Id del Show : {id} ===")
    tvshow_m = Tvshow.objects.get(id=id)
    contexto = {
        "id": tvshow_m.id,
        "titulo": tvshow_m.titulo,
        "network": tvshow_m.network,
        # "libera": tvshow_m.libera,
        "descri": tvshow_m.descri
    }
    return render(request, 'editar.html', contexto)

def mostrar(request, id):
    print(f"=== MOSTRAR Id del Show : {id} ===")
    tvshow_m = Tvshow.objects.get(id=id)
    contexto = {
        "id": tvshow_m.id,
        "titulo": tvshow_m.titulo,
        "network": tvshow_m.network,
        # "libera": tvshow_m.libera,
        "descri": tvshow_m.descri,
        "ultima": tvshow_m.updated_at
    }
    return render(request, 'mostrar.html', contexto) 

def borrar(request, id):
    print(f"Eliminación TVShow: {id}")

    tvshow_objeto = Tvshow.objects.get(id=id)
    # tvshow_objeto.delete()
    messages.warning(request, f"TV Show {tvshow_objeto.titulo} Eliminado OK")

    return redirect('/shows')
    # return render(request, 'shows.html')

def crear_show(request):
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)

        newshow = Tvshow.objects.create(
            titulo = request.POST['titulo'],
            network = request.POST['network'],
            # libera = request.POST['release'],
            descri = request.POST['descripcion']
        )
        messages.success(request, f"TV Show {newshow.titulo} Creado OK")
        messages.warning(request, f"TV Show {newshow.titulo} Creado OK")
        show_id = newshow.id
        print(f"=== Id del Show :{show_id} ===")
        return redirect(f"/shows/{show_id}")

def actualizar_show(request, id):
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        print(f"=== ACTUALIZAR Id del Show : {id} ===")

        show_id = id
        tvshow_objeto = Tvshow.objects.get(id=show_id)
        tvshow_objeto.titulo = request.POST['titulo']
        tvshow_objeto.network = request.POST['network']
        # tvshow_objeto.libera = request.POST['release'],
        tvshow_objeto.descri = request.POST['descripcion']
        tvshow_objeto.save()
        
        messages.warning(request, f"TV Show {tvshow_objeto.titulo} Actualizado OK")
        print(f"=== Id del Show :{show_id} ===")
        return redirect(f"/shows/{show_id}")