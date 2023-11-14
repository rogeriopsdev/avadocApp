from django.shortcuts import render, redirect, get_object_or_404
from avadocApp.forms import DiscenteForm,AvadocForm, DiarioForm,ComponenteForm
from .models import Discente, Docente,Diario,Curso,Campi,Componente,Nivel,Avadoc


# Create your views here.
def index(request):
    avaliados=Avadoc.objects.all().filter(id_docente__id_docente=1)

    #docentes = Diario.objects.all() and Discente.objects.all().filter(turma_discente='turma_diario')

    discentes = Discente.objects.all()
    for dis in discentes:
        turma =dis.turma_discente
    docentes = Diario.objects.all().filter(turma_diario=turma)

    return render(request, 'avadoc/index.html',{'avaliados':avaliados, 'docentes':docentes, 'discentes':discentes})

def new_discente(request):

    form = DiscenteForm(request.POST)
    if request.method == 'POST':
        form = DiscenteForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = DiscenteForm()

    return render(request, 'avadoc/new_discente.html',{'form':form})


def ver_discente(request):
    discentes = Discente.objects.all()[:100]
    return render(request,'avadoc/ver_discente.html',{'discentes':discentes})

# Docente
docente=[]
def ver_docente(request):
    docente =Docente.objects.values('id_docente','nome_docente','cod_docente')
    diario =Diario.objects.values('nome_curso_diario','nome_diario_componente','periodo_diario')

    docentes =docente.union(diario)

   #docentes =Docente.objects.all().filter(cod_docente=siape)

    #discentes = Discente.objects.all()
    #for dis in discentes:
     #   turma = dis.turma_discente
    #docente = Diario.objects.all().filter(turma_diario=turma)
    #docentes = Docente.objects.all()
    return render(request,'avadoc/ver_docente.html',{'docentes':docentes})






#campi
def ver_campi(request):
    campi = Campi.objects.all()
    return render(request,'avadoc/ver_campi.html',{'campi':campi})
#componente
def ver_componente(request):
    comp = Componente.objects.all()
    return render(request,'avadoc/ver_componente.html',{'comp':comp})
#dirio
def ver_diario(request):
    diarios = Diario.objects.all()
    return render(request,'avadoc/ver_diario.html',{'diarios':diarios})
#curso
def ver_curso(request):
    cursos= Curso.objects.all()
    return render(request,'avadoc/ver_curso.html',{'cursos':cursos})

#base
def base(request):
    return render(request,'avadoc/base.html')
# avadoc


def avadoc(request):
    formulario = AvadocForm(request.POST)
    if request.method == "POST":
        formulario = AvadocForm(request.POST, request.FILES)
        if formulario.is_valid():
            obj =formulario.save()
            obj.save()
            formulario = AvadocForm()
    return render(request, 'avadoc/avalia_doc.html', {'formulario': formulario})



def avalia(request, id_docente):
    docente= get_object_or_404(Docente,pk=id_docente)
    form = AvadocForm(instance=docente)
    if request.method=="POST":
        form =AvadocForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return redirect('ver_docente')
        else:
            return render(request, 'avadoc/avalia.html', {'form': form, 'docente': docente})
    else:
        return render(request, 'avadoc/avalia.html', {'form': form, 'docente': docente})


def ver_avalia(request):
    avas = Avadoc.objects.all()

    return render(request, 'avadoc/ver_avalia.html',{'avas':avas})


#---------individual-----

def avindividual(request, id_docente):

    #avas = Avadoc.objects.all()
    #id_docente = request.GET.get('search')
    avaliados=Docente.objects.all()
    #avas=Docente.objects.filter(avadoc__id_docente=id_docente) #and Avadoc.objects.all().filter(id_docente__cod_docente=id_docente)

    avas=Avadoc.objects.filter(id_docente__id_docente=id_docente) #and Avadoc.objects.all().filter(id_docente__cod_docente=id_docente)
    assiduidade =Avadoc.objects.all().filter(id_docente__id_docente=id_docente)

    planejamento =0
    aulas =0
    avaliacao =0
    postura =0
    assi_total = 0
    pontulidade=0
    m_assiduidade=0
    m_planejamento = 0
    m_aulas = 0
    m_avaliacao = 0
    m_postura = 0
    m_pontualidade=0
    m_geral =0

    for dado in assiduidade:
        assi_total += int(dado.assid_avadoc)
        pontulidade += int(dado.pont_avadoc)
        planejamento += int(dado.plan_avadoc)
        aulas += int(dado.realiza_avadoc)
        avaliacao+= int(dado.avaliacao_avadoc)
        postura+= int(dado.postura_avadoc)
        qtd = assi_total.bit_length()

    qt = len(assiduidade)

    m_assiduidade = ((assi_total)/(qt))
    m_pontualidade = ((pontulidade)/(qt))
    m_planejamento = ((planejamento)/(qt))
    m_aulas = ((aulas)/(qt))
    m_avaliacao = ((avaliacao)/(qt))
    m_postura = ((postura)/(qt))
    m_geral=(m_assiduidade+m_pontualidade+m_planejamento+m_aulas+m_avaliacao+m_postura)/6

    print(m_assiduidade)
    print(m_geral)

    context={'avas': avas,
             'avaliados':avaliados,
             'assi_total':assi_total,
             'pontulidade':pontulidade,
             'planejamento':planejamento,
             'aulas':aulas,
             'avaliacao':avaliacao,
             'postura':postura,
             'm_assiduidade':m_assiduidade,
             'm_pontualidade':m_planejamento,
             'm_planejamento':m_pontualidade,
             'm_aulas':m_aulas,
             'm_avaliacao':m_avaliacao,
             'm_postura':m_postura,
             'qt':qt,
             'm_geral':m_geral,
                          }
    return render(request, 'avadoc/ver_avindivual.html',context)

def new_componente(request):

    form = ComponenteForm(request.POST)
    if request.method == 'POST':
        form = ComponenteForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = DiscenteForm()

    return render(request, 'avadoc/new_componente.html',{'form':form})


def filtro_avalia(request):
    docentes = Diario.objects.all().filter(Discente.objects.all().filter(turma_discente='turma_diario'))
    for d in docentes:
        f= d.turma_diario
        print(f)

    return render(request, 'avadoc/index.html',{'f':f})
