from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views import generic
from django.shortcuts import render

from apps.publications.forms import UserMailForm,  MyPublicationForm
from apps.publications.models import Publication, PublicationCategory, UserMail


class PublicationListView(generic.ListView):
    template_name = 'index.html'
    context_objects_name = 'publication_list'

    def get_queryset(self):
        query_params = self.request.GET
        search_world = query_params.get('search_world')
        category_id = query_params.get('category_pk')
        publication_qs = Publication.objects.all()
        if search_world:
            publication_qs = Publication.objects.filter(title__contains=search_world)

        if category_id:
            try:
                category_id=int(category_id)

            except ValueError:
                pass
            else:
             publication_qs = publication_qs.filter(category_id=category_id)
        return publication_qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(PublicationListView, self).get_context_data()
        context['category_list'] = PublicationCategory.objects.all()
        return context


class PublicationDetailView(generic.DetailView):
    template_name = 'single.html'
    context_object_name = 'publication'
    model = Publication
    slug_field = 'id'
    slug_url_kwarg = 'pub_pk'


#cbv

def accept_show_user_mail_form_view(request):
    if request.method == 'GET':
        user_form = UserMailForm()
        response = render(request,'user-email.html',
                      context={'form':user_form})
        return response
    elif request.method == 'POST':
        print(request.POST)
        UserMail.objects.create(name=request.POST['name'],email=request.POST['email'])
        return HttpResponse('<h> вы подписались на рассылку</h1>',status=201)






def show_my_all_publication(request):
    if request.method == 'GET':
        public_form = MyPublicationForm()
        response = render(request,'publication.html',context={'form':public_form})

        return response
    elif request.method == 'POST':
        print(request.POST)
        print('files: ', request.FILES)
        image_file = request.FILES['poster']
        Publication.objects.create(title=request.POST['title'],description=request.POST['description'],poster=image_file)
        return HttpResponse('<h> good job</h1>',status=201)
