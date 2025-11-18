from django.shortcuts import render, redirect, get_object_or_404
from .models import Clube
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    clubes = Clube.objects.all()
    return render(request, 'clubes/lista.html', {'clubes': clubes})


@login_required
def adicionar_clube(request):
    if request.method == 'POST':
        Clube.objects.create(
            nome=request.POST['nome'],
            descricao=request.POST['descricao'],
            responsavel=request.user
        )
        return redirect('dashboard')
    return render(request, 'clubes/form.html')


@login_required
def editar_clube(request, clube_id):
    clube = get_object_or_404(Clube, pk=clube_id)
    if request.method == 'POST':
        clube.nome = request.POST['nome']
        clube.descricao = request.POST['descricao']
        clube.save()
        return redirect('dashboard')
    return render(request, 'clubes/form.html', {'clube': clube})


@login_required
def excluir_clube(request, clube_id):
    clube = get_object_or_404(Clube, pk=clube_id)
    if request.method == 'POST':
        clube.delete()
        return redirect('dashboard')
    return render(request, 'clubes/confirmar_exclusao.html', {'clube': clube})
