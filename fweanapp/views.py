from django.core.files.base import endswith_cr
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.views.generic import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
import datetime

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mass_mail,send_mail
import json
from django.core import mail
from django.http import JsonResponse
import requests
from django.contrib import messages

from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from asgiref.sync import sync_to_async
import asyncio

from django.core.mail import EmailMessage



class AdminLoginView(FormView):
    template_name = "admintemplates/adminlogin.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("fweanapp:admindashboard")


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password = password)

        # print(user)
        if user is not None :
            login(self.request,user)
        else:
            return render(self.request, self.template_name,{
                'form' : form,
                'error' : 'invalid credentials'
            })
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org'] = Organization.objects.first()

        return context

    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET['next']
        else:
            return self.success_url





class AdminLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('fweanapp:adminlogin')



class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            pass
        else:
            return redirect('/admin-site/login/?next=' + request.path)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org'] = Organization.objects.first()
        context['vicepresidentform'] = BoardVicePresidentForm
        context['immediatepastpresidentsform'] = ImmediatePastPresidentForm
        context['executivemembersform'] = ExecutiveMemberForm
        context['feedbacks'] = Feedbacks.objects.all()
        context['feedbacks_unread'] = Feedbacks.objects.filter(is_viewed=False).order_by('created_at')[:3]
        context['membershipcontents'] = MembershipContents.objects.all()
        context['newsandevents'] = NewsandMedia.objects.all()
        context['importantlinks'] = FooterImportantLinks.objects.all()
        context['faqs'] = Faq.objects.all()
        context['donors'] = Donors.objects.all()
        context['blogs'] = Blog.objects.all()
        context['subscribers'] = Subscriber.objects.all()
        context['subscribers_unread'] = Subscriber.objects.filter(is_viewed=False).order_by('created_at')[:3]
        notification_count = (Subscriber.objects.filter(is_viewed=False).count() + Feedbacks.objects.filter(is_viewed=False).count() )
        context['notification_count'] = notification_count
        context['successstories'] = SuccessStories.objects.all()
        context['successstories'] = SuccessStories.objects.all()
        context['programmes'] = Programmes.objects.all()
        context['projects'] = Projects.objects.all()
        context['aboutus'] = AboutUs.objects.all()
        context['imageandvideos'] = ImageAlbum.objects.all()
        context['publications'] = Publication.objects.all()
        context['memcontents'] = MembershipContents.objects.all()
        
        return context


class ClientPublicationDownloadCounter(AdminRequiredMixin,View):
    def get(self, request,*args,**kwargs):
        # print(self.kwargs)
        publication = get_object_or_404(Publication,slug=self.kwargs['slug'])
        
        publication.download_count += 1
        publication.save()
        
        return redirect('fweanapp:clientpublication')


class AdminProfileUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/adminprofileupdate.html"
    form_class = AdminProfileForm
    model = User
    success_message = "Profile updated successfully"

    def get_success_url(self):
        return reverse('fweanapp:adminprofile',
                       kwargs={'pk': self.kwargs['pk']})


class AdminPasswordUpdateView(AdminRequiredMixin, FormView):
    template_name = 'admintemplates/adminpasswordupdate.html'
    form_class = PasswordUpdateForm
    success_url = reverse_lazy("fweanapp:adminlogin")
    success_message = "Password updated successfully. \
                        Please Login to continue."

    def form_valid(self, form):
        current_password = form.cleaned_data['current_password']
        confirm_new_password = form.cleaned_data['confirm_new_password']
        user = authenticate(username=self.request.user.username,
                            password=current_password)
        if user is not None:
            user.set_password(confirm_new_password)
            user.save()
        else:
            return render(self.request, self.template_name, {
                'form': form,
                'orginfo': Organization.objects.first(),
                'admin': self.request.user,
                'error': "Invalid Current Password!"})
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("fweanapp:adminlogin")




class AdminProfileView(AdminRequiredMixin, TemplateView):
    template_name = "admintemplates/adminprofile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admin"] = self.request.user
        return context



class AdminDashboardView(AdminRequiredMixin,TemplateView):

    template_name = 'admintemplates/dashboard.html'





class AdminOrganizationCreateView(AdminRequiredMixin,CreateView):
    template_name = 'admintemplates/organizationadd.html'
    # print(Organization.objects.all())
    model = Organization
    form_class = OrganizationForm
    success_url = reverse_lazy("fweanapp:admindashboard")



class AdminOrganizationUpdateView(AdminRequiredMixin,UpdateView):
    template_name = 'admintemplates/organizationadd.html'
    model = Organization
    form_class = OrganizationForm
    # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminorganizationdetail', kwargs={'pk': self.kwargs['pk']})




class AdminOrganizationDetailView(AdminRequiredMixin,DetailView):
    template_name = 'admintemplates/organizationdetail.html'
    model = Organization



from django.http import HttpResponse, HttpResponseRedirect
class ImageAlbumAddView(AdminRequiredMixin, CreateView):
    model = ImageMedia
    form_class = ImageAlbumForm
    template_name = 'admintemplates/imagealbumadd.html'
    success_url = reverse_lazy('fweanapp:imagealbumlist')

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        imagemedia_form = ImageMediaFormSet()

        return self.render_to_response(
            self.get_context_data(form=form,
                                  imagemedia_form = imagemedia_form,
                                  ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        imagemedia_form = ImageMediaFormSet(self.request.POST , self.request.FILES )
        # print(imagemedia_form.cleaned_data)

        if (form.is_valid() and imagemedia_form.is_valid()):
            return self.form_valid(form, imagemedia_form)
        else:
            return self.form_invalid(form, imagemedia_form)

    def form_valid(self, form, imagemedia_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        # print('=======')
        # print(self.object)
        self.object = form.save()
        imagemedia_form.instance = self.object
        # print('=======')
        # print(self.object)
        imagemedia_form.save()


        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, imagemedia_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  imagemedia_form=imagemedia_form))



class ImageAlbumUpdateView(AdminRequiredMixin, UpdateView):
    model = ImageAlbum
    form_class = ImageAlbumForm
    formset_class = ImageMediaFormSet
    is_update_view = True
    template_name = 'admintemplates/imagealbumadd.html'

    def get_success_url(self):

        return reverse_lazy('fweanapp:imagealbumlist')

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        album = ImageAlbum.objects.get(pk=kwargs.get('pk'))
        # print(album)

        imagemedia_form = ImageMediaFormSet(instance = album)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  imagemedia_form=imagemedia_form,
                                  ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        album = ImageAlbum.objects.get(pk=kwargs.get('pk'))
        imagemedia_form = ImageMediaFormSet(self.request.POST , self.request.FILES, instance = album )
        # print(imagemedia_form.cleaned_data)

        if (form.is_valid() and imagemedia_form.is_valid()):
            return self.form_valid(form, imagemedia_form)
        else:
            return self.form_invalid(form, imagemedia_form)

    def form_valid(self, form, imagemedia_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        # print('=======')
        # print(self.object)
        self.object = form.save()
        imagemedia_form.instance = self.object
        # print('=======')
        # print(self.object)
        imagemedia_form.save()


        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, imagemedia_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  imagemedia_form=imagemedia_form))


class ImageMediaDeleteView(AdminRequiredMixin, DeleteView):
    model = ImageMedia
    success_url = reverse_lazy('fweanapp:imagealbumlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):

        album_id = self.object.album.id
        return reverse_lazy('fweanapp:adminimagealbumdetail', kwargs={'pk': album_id})


class ImageAlbumListView(AdminRequiredMixin, ListView):
    model = ImageAlbum
    context_object_name = 'albums'

    template_name = 'admintemplates/imagealbumlist.html'



class ImageAlbumDetailView(AdminRequiredMixin, DetailView):
    model = ImageAlbum
    template_name = 'admintemplates/imagealbumdetail.html'
    success_url = reverse_lazy('fweanapp:imagealbumlist')

    context_object_name = 'albumdetail'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['imagemedias'] = ImageMedia.objects.filter(album__id=self.kwargs.get('pk'))

        return context



class ImageAlbumDeleteView(AdminRequiredMixin, DeleteView):
    model = ImageAlbum
    # template_name = 'admintemplates/adminimagealbumdelete.html'
    success_url = reverse_lazy('fweanapp:imagealbumlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class SliderCreateView(AdminRequiredMixin,CreateView):
    model = Slider
    template_name = 'admintemplates/slideradd.html'
    form_class = SliderForm
    success_url = reverse_lazy('fweanapp:adminsliderlist')



class SliderListView(AdminRequiredMixin, ListView):
    model = Slider
    context_object_name = 'sliders'
    template_name = 'admintemplates/sliderlist.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.first()

        return context


class SliderDetailView(AdminRequiredMixin, DetailView):
    model = Slider
    template_name = 'admintemplates/sliderdetail.html'
    success_url = reverse_lazy('fweanapp:sliderdetail')

    context_object_name = 'sliderdetail'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['imagemedias'] = ImageMedia.objects.filter(album__id=self.kwargs.get('pk'))

        return context


class AdminSliderUpdateView(AdminRequiredMixin,UpdateView):
    model = Slider
    form_class = SliderForm
    template_name = 'admintemplates/slideradd.html'
    # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminsliderlist')



class AdminSliderDeleteView(AdminRequiredMixin, DeleteView):
    model = Slider
    success_url = reverse_lazy('fweanapp:adminsliderlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


    






class AdminAboutUsCreateView(AdminRequiredMixin,CreateView):
    model = AboutUs
    template_name = 'admintemplates/aboutusadd.html'
    form_class = AboutUsForm
    success_url = reverse_lazy('fweanapp:adminaboutuslist')



class AdminAboutUsListView(AdminRequiredMixin, ListView):
    model = AboutUs
    context_object_name = 'aboutus'
    template_name = 'admintemplates/aboutuslist.html'



class AdminAboutUsDetailView(AdminRequiredMixin, DetailView):
    model = AboutUs
    template_name = 'admintemplates/aboutusdetail.html'
    success_url = reverse_lazy('fweanapp:adminaboutusdetail')

    context_object_name = 'aboutusdetail'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['imagemedias'] = ImageMedia.objects.filter(album__id=self.kwargs.get('pk'))

        return context


class AdminAboutUsUpdateView(AdminRequiredMixin,UpdateView):
    model = AboutUs
    form_class = AboutUsForm
    template_name = 'admintemplates/aboutusadd.html'
    # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminaboutuslist')



class AdminAboutUsDeleteView(AdminRequiredMixin, DeleteView):
    model = AboutUs
    success_url = reverse_lazy('fweanapp:adminaboutuslist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)




class AdminProjectsCreateView(AdminRequiredMixin,CreateView):
    model = Projects
    template_name = 'admintemplates/projectadd.html'
    form_class = ProjectsForm
    success_url = reverse_lazy('fweanapp:adminprojectlist')
  


class AdminProjectsListView(AdminRequiredMixin, ListView):
    model = Projects
    context_object_name = 'project_list'
    template_name = 'admintemplates/projectlist.html'



class AdminProjectsDetailView(AdminRequiredMixin, DetailView):
    model = Projects
    template_name = 'admintemplates/projectdetail.html'
    success_url = reverse_lazy('fweanapp:adminprojectdetail')
 
    context_object_name = 'projectdetail'




class AdminProjectsUpdateView(AdminRequiredMixin,UpdateView):
    model = Projects
    form_class = ProjectsForm
    template_name = 'admintemplates/projectadd.html'
    # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminprojectlist')



class AdminProjectsDeleteView(AdminRequiredMixin, DeleteView):
    model = Projects
    success_url = reverse_lazy('fweanapp:adminprojectlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



#Programmes
class AdminProgrammesCreateView(AdminRequiredMixin,CreateView):
    model = Programmes
    template_name = 'admintemplates/programmeadd.html'
    form_class = ProgrammeForm
    success_url = reverse_lazy('fweanapp:adminprogrammelist')



class AdminProgrammesListView(AdminRequiredMixin, ListView):
    model = Programmes
    context_object_name = 'programme_list'
    template_name = 'admintemplates/programmelist.html'



class AdminProgrammesDetailView(AdminRequiredMixin, DetailView):
    model = Programmes
    template_name = 'admintemplates/programmedetail.html'
    success_url = reverse_lazy('fweanapp:adminprogrammedetail')

    context_object_name = 'programmedetail'




class AdminProgrammesUpdateView(AdminRequiredMixin,UpdateView):
    model = Programmes
    form_class = ProgrammeForm
    template_name = 'admintemplates/programmeadd.html'
    # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminprogrammelist')



class AdminProgrammesDeleteView(AdminRequiredMixin, DeleteView):
    model = Programmes
    success_url = reverse_lazy('fweanapp:adminprogrammelist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



#SuccessStories




class AdminSuccessStoriesCreateView(AdminRequiredMixin,CreateView):
    model = SuccessStories
    template_name = 'admintemplates/successstoriesadd.html'
    form_class = SuccessStoriesForm
    success_url = reverse_lazy('fweanapp:adminsuccessstorieslist')

    def form_valid(self, form):
   
        obj = form.save()
        url = reverse('fweanapp:clientsuccessstoriesdetail', kwargs={'slug':obj.slug})
        if obj.is_active == True:
               
            client_email = []
            for user in Subscriber.objects.filter(is_active=True):
                client_email.append(user.email)
            subject = "New Success Story"
            message = "We have just added a new success story in our site. You can view it from this link: " + "https://fwean.org.np"+ url
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, client_email)
        
            
            # #Async function for sending email to subscribers when adding new success story.
            # async def asyncsuccstoriesfun(url):
            #     subscribers = await sync_to_async(list)(Subscriber.objects.all())
            #     # email_list =  [subscriber.email for subscriber in subscribers]
            #     email_list =  ['pallav.adhikari@fwean.org.np']
            #     print(email_list)
            #     print('email is now sending')
            #     subject = "New Success Story (FWEAN)"
            #     sender = settings.EMAIL_HOST_USER
            #     message = "We have just added a new success story in our site. You can view it from this link: " + "https://fwean.org.np"+ url
            #     a_send_mail = sync_to_async(send_mail, thread_sensitive=False)
            #     asyncio.create_task(a_send_mail(subject,message,sender,email_list)) 
            #     print('email sent successfully')   


            # asyncio.run(asyncsuccstoriesfun(url))
        
        return super().form_valid(form)


class AdminSuccessStoriesListView(AdminRequiredMixin, ListView):
    model = SuccessStories
    context_object_name = 'successstories_list'
    template_name = 'admintemplates/successstorieslist.html'



class AdminSuccessStoriesDetailView(AdminRequiredMixin, DetailView):
    model = SuccessStories
    template_name = 'admintemplates/successstoriesdetail.html'
    success_url = reverse_lazy('fweanapp:adminsuccessstoriesdetail')

    context_object_name = 'successstoriesdetail'




class AdminSuccessStoriesUpdateView(AdminRequiredMixin,UpdateView):
    model = SuccessStories
    form_class = SuccessStoriesForm
    template_name = 'admintemplates/successstoriesadd.html'
    # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminsuccessstorieslist')



class AdminSuccessStoriesDeleteView(AdminRequiredMixin, DeleteView):
    model = SuccessStories
    success_url = reverse_lazy('fweanapp:adminsuccessstorieslist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



#Subscriber
class AdminSubscribersListView(AdminRequiredMixin,ListView):
    template_name = 'admintemplates/subscriberslist.html'
    model = Subscriber
    context_object_name = 'subscriberslist'

     # custom method
    def dispatch(self, request, *args, **kwargs):
        ob = Subscriber.objects.all()
        # print(ob)
        for obj in ob:
            # print(obj)
            obj.is_viewed = True
            obj.save()
        
        return super(AdminSubscribersListView, self).dispatch(request, *args, **kwargs)

class AdminSubscriberDeleteView(AdminRequiredMixin,DeleteView):
    model = Subscriber
    success_url = reverse_lazy('fweanapp:adminsubscriberlist')


    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)



class AdminSubscriberUpdateView(AdminRequiredMixin,UpdateView):
    model = Subscriber
    template_name = 'admintemplates/adminsubscriberupdate.html'
    form_class = AdminSubscriberUpdateForm
    success_url = reverse_lazy('fweanapp:adminsubscriberlist')

#Async function for sending email to subscribers when adding new blog.
# async def asyncfun(url):
            
#             subscribers = await sync_to_async(list)(Subscriber.objects.all())
#             email_list =  [subscriber.email for subscriber in subscribers]
#             # print(email_list)
#             # print('email is now sending')
#             subject = "New Blog (FWEAN)"
#             sender = settings.EMAIL_HOST_USER
#             message = "We have just published a new blog in our site. You can view it from this link: " + "https://fwean.org.np"+ url
#             a_send_mail = sync_to_async(send_mail, thread_sensitive=False)
#             asyncio.create_task(a_send_mail(subject,message,sender,email_list)) 
#             # print('email sent successfully')


class AdminBlogCreateView(AdminRequiredMixin, CreateView):
    template_name = 'admintemplates/adminblogcreate.html'
    form_class = BlogForm
    success_url = reverse_lazy('fweanapp:adminbloglist')

    def form_valid(self, form):

        obj = form.save()
        url = reverse('fweanapp:clientblogdetail', kwargs={'slug':obj.slug})
        if obj.is_active == True:
            client_email = []
            for user in Subscriber.objects.filter(is_active=True):
                client_email.append(user.email)
            subject = "New Blog"
            message = "We have just posted a new blog in our site. You can view it from this link: " + "https://fwean.org.np"+ url
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, client_email)
        
        return super().form_valid(form)


    

class AdminBlogListView(AdminRequiredMixin, ListView):
    template_name = 'admintemplates/adminbloglist.html'
    model = Blog
    context_object_name = 'bloglist'


class AdminBlogDetailView(AdminRequiredMixin, DetailView):
    template_name = 'admintemplates/adminblogdetail.html'
    model = Blog
    context_object_name = 'blogdetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = BlogComments.objects.filter(blog_id = self.kwargs['pk'])


        return context


class AdminBlogUpdateView(AdminRequiredMixin, UpdateView):
    template_name = 'admintemplates/adminblogcreate.html'
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('fweanapp:adminbloglist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(id=self.kwargs['pk'])

        return context

class AdminBlogCommentListView(AdminRequiredMixin, ListView):
    template_name = 'admintemplates/blogcommentlist.html'
    model = BlogComments
    context_object_name = 'blog_comments'



class AdminBlogCommentUpdate(AdminRequiredMixin, UpdateView):
    template_name = 'admintemplates/adminblogcommentcreate.html'
    model = BlogComments
    form_class = BlogCommentsPublishForm
    success_url = reverse_lazy('fweanapp:adminblogcommentslist')


class AdminBlogCommentDeleteView(AdminRequiredMixin, DeleteView):
    model = BlogComments
    success_url = reverse_lazy('fweanapp:adminblogcommentslist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class AdminBlogDeleteView(AdminRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('fweanapp:adminbloglist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



# Donors
class AdminDonorsCreateView(AdminRequiredMixin,CreateView):
    model = Donors
    template_name = 'admintemplates/donorsadd.html'
    form_class = DonorsForm
    success_url = reverse_lazy('fweanapp:admindonorlist')



class AdminDonorsListView(AdminRequiredMixin, ListView):
    model = Donors
    context_object_name = 'donors_list'
    template_name = 'admintemplates/donorslist.html'



class AdminDonorsDetailView(AdminRequiredMixin, DetailView):
    model = Donors
    template_name = 'admintemplates/donorsdetail.html'
    success_url = reverse_lazy('fweanapp:admindonordetail')

    context_object_name = 'donorsdetail'




class AdminDonorsUpdateView(AdminRequiredMixin,UpdateView):
    model = Donors
    form_class = DonorsForm
    template_name = 'admintemplates/donorsadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:admindonorlist')



class AdminDonorsDeleteView(AdminRequiredMixin, DeleteView):
    model = Donors
    success_url = reverse_lazy('fweanapp:admindonorlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

#FAQ

class AdminFAQCreateView(AdminRequiredMixin,CreateView):
    model = Faq
    template_name = 'admintemplates/faqadd.html'
    form_class = FaqForm
    success_url = reverse_lazy('fweanapp:adminfaqlist')



class AdminFAQListView(AdminRequiredMixin, ListView):
    model = Faq
    context_object_name = 'faq_list'
    template_name = 'admintemplates/faqlist.html'

class AdminFAQDetailView(AdminRequiredMixin, DetailView):
    model = Faq
    template_name = 'admintemplates/faqdetail.html'
    context_object_name = 'faqdetail'


class AdminFAQUpdateView(AdminRequiredMixin,UpdateView):
    model = Faq
    form_class = FaqForm
    template_name = 'admintemplates/faqadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:adminfaqlist')



class AdminFAQDeleteView(AdminRequiredMixin, DeleteView):
    model = Faq
    success_url = reverse_lazy('fweanapp:adminfaqlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#Footer Quick Links

class AdminImportantLinksCreateView(AdminRequiredMixin,CreateView):
    model = FooterImportantLinks
    template_name = 'admintemplates/importantlinksadd.html'
    form_class = ImportantLinksForm
    success_url = reverse_lazy('fweanapp:adminimportantlinkslist')




class AdminImportantLinksListView(AdminRequiredMixin, ListView):
    model = FooterImportantLinks
    context_object_name = 'importantlinks_list'
    template_name = 'admintemplates/importantlinkslist.html'




class AdminImportantLinksUpdateView(AdminRequiredMixin,UpdateView):
    model = FooterImportantLinks
    form_class = ImportantLinksForm
    template_name = 'admintemplates/importantlinksadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:adminimportantlinkslist')



class AdminImportantLinksDeleteView(AdminRequiredMixin, DeleteView):
    model = FooterImportantLinks
    success_url = reverse_lazy('fweanapp:adminimportantlinkslist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)





# Upcoming Events
class AdminUpcomingEventsCreateView(AdminRequiredMixin,CreateView):
    model = UpcomingEvents
    template_name = 'admintemplates/upcomingeventsadd.html'
    form_class = UpcomingEventsForm
    success_url = reverse_lazy('fweanapp:adminupcomingeventlist')



class AdminUpcomingEventsListView(AdminRequiredMixin, ListView):
    model = UpcomingEvents
    context_object_name = 'upcomingevents_list'
    template_name = 'admintemplates/upcomingeventslist.html'



class AdminUpcomingEventsDetailView(AdminRequiredMixin, DetailView):
    model = UpcomingEvents
    template_name = 'admintemplates/upcomingeventsdetail.html'
    success_url = reverse_lazy('fweanapp:adminupcomingeventsdetail')

    context_object_name = 'upcomingeventsdetail'




class AdminUpcomingEventsUpdateView(AdminRequiredMixin,UpdateView):
    model = UpcomingEvents
    form_class = UpcomingEventsForm
    template_name = 'admintemplates/upcomingeventsadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:adminupcomingeventlist')



class AdminUpcomingEventsDeleteView(AdminRequiredMixin, DeleteView):
    model = UpcomingEvents
    success_url = reverse_lazy('fweanapp:adminupcomingeventlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



# News and Media.

#Async function for sending email to subscribers when adding new blog.

# async def asyncnewsfun(url):
#     subscribers = await sync_to_async(list)(Subscriber.objects.all())
#     email_list =  [subscriber.email for subscriber in subscribers]
#     # print(email_list)
#     # print('email is now sending')
#     subject = "New news (FWEAN)"
#     sender = settings.EMAIL_HOST_USER
#     message = "We have just published a new news in our site. You can view it from this link: " + "https://fwean.org.np"+ url
#     a_send_mail = sync_to_async(send_mail, thread_sensitive=False)
#     asyncio.create_task(a_send_mail(subject,message,sender,email_list)) 
#     #print('email sent successfully')


class AdminNewsandMediaCreateView(AdminRequiredMixin,CreateView):
    model = NewsandMedia
    template_name = 'admintemplates/newsadd.html'
    form_class = NewsandMediaForm
    success_url = reverse_lazy('fweanapp:adminnewslist')

    

    def form_valid(self, form):
        # print('===============')
        obj = form.save()
        # print(obj.is_active)
        url = reverse('fweanapp:clientnewsandeventsdetail', kwargs={'slug':obj.slug})
        if obj.is_active == True:
            client_email = []
            for user in Subscriber.objects.filter(is_active=True):
                client_email.append(user.email)
            subject = "New news article"
            message = "We have just posted a new news article in our site. You can view it from this link: " + "https://fwean.org.np"+ url
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, client_email)
        
        return super().form_valid(form)
        
        
class AdminNewsandMediaListView(AdminRequiredMixin, ListView):
    model = NewsandMedia
    context_object_name = 'news_list'
    template_name = 'admintemplates/newslist.html'



class AdminNewsandMediaDetailView(AdminRequiredMixin, DetailView):
    model = NewsandMedia
    template_name = 'admintemplates/newsdetail.html'
    context_object_name = 'newsdetail'




class AdminNewsandMediaUpdateView(AdminRequiredMixin,UpdateView):
    model = NewsandMedia
    form_class = NewsandMediaForm
    template_name = 'admintemplates/newsadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:adminnewslist')



class AdminNewsandMediaDeleteView(AdminRequiredMixin, DeleteView):
    model = NewsandMedia
    success_url = reverse_lazy('fweanapp:adminnewslist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)




# Social Media News
class AdminSocialMediaNewsCreateView(AdminRequiredMixin,CreateView):
    model = SocialMediaNewsFeeds
    template_name = 'admintemplates/socialmedianewsadd.html'
    form_class = SocialMediaNewsForm
    success_url = reverse_lazy('fweanapp:adminsocialmedia-newsfeedlist')



class AdminSocialMediaNewsListView(AdminRequiredMixin, ListView):
    model = SocialMediaNewsFeeds
    context_object_name = 'socialmedia_news_list'
    template_name = 'admintemplates/socialmedianewslist.html'



class AdminSocialMediaNewsDetailView(AdminRequiredMixin, DetailView):
    model = SocialMediaNewsFeeds
    template_name = 'admintemplates/socialmedianewsdetail.html'
    context_object_name = 'socialmedianewsdetail'




class AdminSocialMediaNewsUpdateView(AdminRequiredMixin,UpdateView):
    model = SocialMediaNewsFeeds
    form_class = SocialMediaNewsForm
    template_name = 'admintemplates/socialmedianewsadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:adminsocialmedia-newsfeedlist')



class AdminSocialMediaNewsDeleteView(AdminRequiredMixin, DeleteView):
    model = SocialMediaNewsFeeds
    success_url = reverse_lazy('fweanapp:adminsocialmedia-newsfeedlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# Admin Videos
class AdminVideosCreateView(AdminRequiredMixin,CreateView):
    model = Videos
    template_name = 'admintemplates/videosadd.html'
    form_class = VideoAddForm
    success_url = reverse_lazy('fweanapp:adminvideolist')



class AdminVideosListView(AdminRequiredMixin, ListView):
    model = Videos
    context_object_name = 'videos_list'
    template_name = 'admintemplates/videoslist.html'



class AdminVideosDetailView(AdminRequiredMixin, DetailView):
    model = Videos
    template_name = 'admintemplates/videosdetail.html'
    context_object_name = 'videosdetail'




class AdminVideosUpdateView(AdminRequiredMixin,UpdateView):
    model = Videos
    form_class = VideoAddForm
    template_name = 'admintemplates/videosadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:adminvideolist')



class AdminVideosDeleteView(AdminRequiredMixin, DeleteView):
    model = SocialMediaNewsFeeds
    success_url = reverse_lazy('fweanapp:adminvideolist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


from django.forms import modelformset_factory
# Admin Boardmembers

class AdminBoardMembersListView(AdminRequiredMixin, ListView):
    model = BoardMembers
    context_object_name = 'board_member_list'
    template_name = 'admintemplates/boardmemberlist.html'

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        context['boardmembers'] = BoardMembers.objects.first()
        context['vicepresidents'] = BoardVicePresidents.objects.filter(boardmembers=BoardMembers.objects.first())
        context['executivemembers'] = BoardExecutiveMembers.objects.filter(boardmembers=BoardMembers.objects.first())
        context['immediatepastpresident'] = BoardImmediatePastPresident.objects.filter(boardmembers=BoardMembers.objects.first())

        return context



class AdminBoardMembersDetailView(AdminRequiredMixin, DetailView):
    model = Videos
    template_name = 'admintemplates/adminboardmemberdetail.html'
    context_object_name = 'boardmemberdetail'


class AdminBoardMembersAddView(AdminRequiredMixin, CreateView):
    model = BoardMembers
    form_class = BoardMembersAddForm
    template_name = 'admintemplates/boardmembersadd.html'
    success_url = reverse_lazy('fweanapp:admindashboard')



class AdminBoardMembersUpdateView(AdminRequiredMixin, UpdateView):
    model = BoardMembers
    form_class = BoardMembersAddForm
    template_name = 'admintemplates/boardmembersadd.html'

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminboardmemberlist')




class BoardVicePresidentsAddView(AdminRequiredMixin, CreateView):
    model = BoardVicePresidents
    form_class = BoardVicePresidentForm
    template_name = 'admintemplates/boardvicepresidentsadd.html'

    def get_success_url(self, **kwargs):
        if BoardMembers.objects.first():

            return reverse('fweanapp:adminboardmembersupdate',
                           kwargs={'pk': BoardMembers.objects.first().id})
        else:
            return reverse_lazy('fweanapp:adminboardmemberlist')



class BoardVicePresidentsUpdateView(AdminRequiredMixin, UpdateView):
    model = BoardVicePresidents
    form_class = BoardVicePresidentForm
    template_name = 'admintemplates/boardvicepresidentsadd.html'
    def get_success_url(self):

        return reverse_lazy('fweanapp:adminboardmemberlist')


class BoardVicePresidentslistView(AdminRequiredMixin, ListView):
    model = BoardVicePresidents
    # form_class = BoardVicePresidentForm
    context_object_name = 'vicepresident_list'
    template_name = 'admintemplates/boardvicepresidentslist.html'



# class BoardVicePresidentsUpdateView(AdminRequiredMixin, UpdateView):
#     model = BoardVicePresidents
#     form_class = BoardVicePresidentForm
#     template_name = 'admintemplates/boardvicepresidentsadd.html'
#     def get_success_url(self):
#
#         return reverse_lazy('fweanapp:adminboardmemberlist')



class BoardVicePresidentsDeleteView(AdminRequiredMixin, DeleteView):
    model = BoardVicePresidents
    success_url = reverse_lazy('fweanapp:adminboardvicepresidentlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

#BoardExecutiveMembers

class BoardExecutiveMembersAddView(AdminRequiredMixin, CreateView):
    model = BoardExecutiveMembers
    form_class = ExecutiveMemberForm
    template_name = 'admintemplates/boardexecutivememberadd.html'

    def get_success_url(self, **kwargs):
        if BoardMembers.objects.first():

            return reverse('fweanapp:adminboardmembersupdate',
                           kwargs={'pk': BoardMembers.objects.first().id})
        else:
            return reverse_lazy('fweanapp:adminboardmemberlist')



class BoardExecutiveMembersUpdateView(AdminRequiredMixin, UpdateView):
    model = BoardExecutiveMembers
    form_class = ExecutiveMemberForm
    template_name = 'admintemplates/boardexecutivememberadd.html'

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminboardmemberlist')

class BoardExecutiveMemberslistView(AdminRequiredMixin, ListView):
    model = BoardExecutiveMembers
    # form_class = BoardVicePresidentForm
    context_object_name = 'executive_members'
    template_name = 'admintemplates/boardexecutivememberlist.html'


class BoardExecutiveMembersDeleteView(AdminRequiredMixin, DeleteView):
    model = BoardExecutiveMembers
    success_url = reverse_lazy('fweanapp:adminboardmemberlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)




class BoardImmediatePastPresidentsAddView(AdminRequiredMixin, CreateView):
    model = BoardImmediatePastPresident
    form_class = ImmediatePastPresidentForm
    template_name = 'admintemplates/boardimmediatepastpresidentsadd.html'

    def get_success_url(self,**kwargs):

        if BoardMembers.objects.first():

            return reverse('fweanapp:adminboardmembersupdate',
                       kwargs={'pk': BoardMembers.objects.first().id})
        else:
            return reverse_lazy('fweanapp:adminboardmemberlist')


class BoardImmediatePastPresidentlistView(AdminRequiredMixin, ListView):
    model = BoardImmediatePastPresident
    # form_class = BoardVicePresidentForm
    context_object_name = 'past_president'
    template_name = 'admintemplates/boardimmediatepastpresidentslist.html'

class BoardImmediatePastPresidentsUpdateView(AdminRequiredMixin, UpdateView):
    model = BoardImmediatePastPresident
    template_name = 'admintemplates/boardimmediatepastpresidentsadd.html'
    form_class = ImmediatePastPresidentForm

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminboardmemberlist')



class BoardImmediatePastPresidentDeleteView(AdminRequiredMixin, DeleteView):
    model = BoardImmediatePastPresident
    success_url = reverse_lazy('fweanapp:adminboardmemberlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



class AdminFeedbacksListView(AdminRequiredMixin,ListView):
    model = Feedbacks
    template_name = 'admintemplates/adminfeedbacklist.html'
    context_object_name = 'feedback_list'


class AdminFeedbacksDetailView(AdminRequiredMixin,DetailView):
    model = Feedbacks
    template_name = 'admintemplates/adminfeedbackdetail.html'
    context_object_name = 'feedback_detail'
    
    
    def get_object(self):
        obj = super().get_object()
        obj.is_viewed = True
        obj.save()
        return obj

class AdminFeedbacksDeleteView(AdminRequiredMixin,DeleteView):
    model = Feedbacks
    success_url = reverse_lazy('fweanapp:adminfeedbackslist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

# Admin Publications

class AdminPublicationCreateView(AdminRequiredMixin,CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'admintemplates/adminpublicationcreate.html'
    success_url = reverse_lazy('fweanapp:adminpublicationlist')

    def form_valid(self, form):

        a = form.cleaned_data['watermark']
        if self.request.method == 'POST' and 'file' in self.request.FILES and a == True:

            pdf_file = self.request.FILES['file']

            watermark = 'media/watermark/watermark.pdf'
            merged = pdf_file

            with open(watermark, "rb") as watermark_file:
                input_pdf = PdfFileReader(pdf_file)
                watermark_pdf = PdfFileReader(watermark_file)
                watermark_page = watermark_pdf.getPage(0)
                output = PdfFileWriter()

                for i in range(input_pdf.getNumPages()):
                    pdf_page = input_pdf.getPage(i)
                    pdf_page.mergePage(watermark_page)
                    output.addPage(pdf_page)

                # with open(merged, "wb") as merged_file:
                output.write(merged)
                # print(merged)

            obj = form.save(commit=False)
            obj.file = merged

        return super().form_valid(form)




class AdminPublicationUpdateView(AdminRequiredMixin,UpdateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'admintemplates/adminpublicationcreate.html'
    success_url = reverse_lazy('fweanapp:adminpublicationlist')


    def form_valid(self, form):

        # print('==============')
        # print(form.cleaned_data['watermark'])
        a = form.cleaned_data['watermark']
        if self.request.method == 'POST' and 'file' in self.request.FILES and a == True :

            pdf_file = self.request.FILES['file']

            watermark = 'media/watermark/watermark.pdf'

            merged = pdf_file

            with open(watermark, "rb") as watermark_file:
                input_pdf = PdfFileReader(pdf_file)
                watermark_pdf = PdfFileReader(watermark_file)
                watermark_page = watermark_pdf.getPage(0)
                output = PdfFileWriter()

                for i in range(input_pdf.getNumPages()):
                    pdf_page = input_pdf.getPage(i)
                    pdf_page.mergePage(watermark_page)
                    output.addPage(pdf_page)

                # with open(merged, "wb") as merged_file:
                output.write(merged)
                # print(merged)

            obj = form.save(commit=False)
            obj.file = merged

        return super().form_valid(form)



class AdminPublicationListView(AdminRequiredMixin,ListView):
    model = Publication
    template_name = 'admintemplates/adminpublicationlist.html'
    context_object_name = 'publication_list'


class AdminPublicationDetailView(AdminRequiredMixin,DetailView):
    model = Publication
    template_name = 'admintemplates/adminpublicationdetail.html'
    context_object_name = 'publication_detail'


class AdminPublicationDeleteView(AdminRequiredMixin,DeleteView):
    model = Publication
    success_url = reverse_lazy('fweanapp:adminpublicationlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)





class AdminMembershipContentsCreateView(AdminRequiredMixin,CreateView):
    model = MembershipContents
    template_name = 'admintemplates/membershipcontentsadd.html'
    form_class = MembershipContentsForm
    success_url = reverse_lazy('fweanapp:adminmembershipcontentlist')



class AdminMembershipContentsListView(AdminRequiredMixin, ListView):
    model = MembershipContents
    context_object_name = 'membershipcontentlist'
    template_name = 'admintemplates/membershipcontentlist.html'



class AdminMembershipContentsDetailView(AdminRequiredMixin, DetailView):
    model = MembershipContents
    template_name = 'admintemplates/membershipcontentdetail.html'
    # success_url = reverse_lazy('fweanapp:adminaboutusdetail')

    context_object_name = 'adminmembershipcontentdetail'


    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #     context['imagemedias'] = ImageMedia.objects.filter(album__id=self.kwargs.get('pk'))
    #
    #     return context


class AdminMembershipContentsUpdateView(AdminRequiredMixin,UpdateView):
    model = MembershipContents
    form_class = MembershipContentsForm
    template_name = 'admintemplates/membershipcontentsadd.html'
    # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

    def get_success_url(self):

        return reverse_lazy('fweanapp:adminmembershipcontentlist')



class AdminMembershipContentsDeleteView(AdminRequiredMixin, DeleteView):
    model = MembershipContents
    success_url = reverse_lazy('fweanapp:adminmembershipcontentlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)




# class AdminNoticeCreateView(AdminRequiredMixin,CreateView):
#     model = Notice
#     template_name = 'admintemplates/adminnoticeadd.html'
#     form_class = NoticeForm
#     success_url = reverse_lazy('fweanapp:adminnoticelist')



# class AdminNoticeListView(AdminRequiredMixin, ListView):
#     model = Notice
#     context_object_name = 'noticelist'
#     template_name = 'admintemplates/adminnoticelist.html'



# class AdminNoticeDetailView(AdminRequiredMixin, DetailView):
#     model = Notice
#     template_name = 'admintemplates/adminnoticedetail.html'
#     # success_url = reverse_lazy('fweanapp:adminaboutusdetail')

#     context_object_name = 'adminnoticedetail'



# class AdminNoticeUpdateView(AdminRequiredMixin,UpdateView):
#     model = Notice
#     form_class = NoticeForm
#     template_name = 'admintemplates/adminnoticeadd.html'
#     # success_url = reverse_lazy("fweanapp:adminorganizationdetail")

#     def get_success_url(self):

#         return reverse_lazy('fweanapp:adminnoticelist')



# class AdminNoticeDeleteView(AdminRequiredMixin, DeleteView):
#     model = Notice
#     success_url = reverse_lazy('fweanapp:adminnoticelist')

#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)





# class AdminMembershipListView(AdminRequiredMixin,ListView):
#     model = Publication
#     template_name = 'admintemplates/adminpublicationlist.html'
#     context_object_name = 'publication_list'


# class AdminMembershipDetailView(AdminRequiredMixin,DetailView):
#     model = Publication
#     template_name = 'admintemplates/adminpublicationdetail.html'
#     context_object_name = 'publication_detail'





class AdminMembershipFormListView(AdminRequiredMixin, ListView):

    model = Membership
    template_name = 'admintemplates/adminmembershipformlist.html'
    context_object_name = 'membership_form_list'



class AdminMembershipFormDetailView(AdminRequiredMixin,DetailView):
    model = Membership
    template_name = 'admintemplates/adminmembershipformdetail.html'
    context_object_name = 'membership_detail'
    def get(self, request, *args, **kwargs):
        
        data = {
             'membership_detail': Membership.objects.get(id=self.kwargs['pk']),
             'memberships' : MembershipOrganization.objects.filter(membership__id=self.kwargs.get('pk')),
            #  'amount': 39.99,
            # 'customer_name': 'Cooper Mann',
            # 'order_id': 1233434,
            'margin-bottom': '0.75in', 
            'footer-right': '[page] of [topage]',
            'app_url' : request.META['HTTP_HOST']
        }
        print(data)
        pdf = render_to_pdf('admintemplates/adminmembershipformdetail.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
   

class AdminMembershipFormDeleteView(AdminRequiredMixin, DeleteView):
    model = Membership
    success_url = reverse_lazy('fweanapp:adminmembershipformlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)





# Admin Email Recipent
class AdminEmailRecipentCreateView(AdminRequiredMixin,CreateView):
    model = EmailRecipients
    template_name = 'admintemplates/emailrecipentsadd.html'
    form_class = EmailRecipientsForm
    success_url = reverse_lazy('fweanapp:adminemailrecipentlist')



class AdminEmailRecipentListView(AdminRequiredMixin, ListView):
    model = EmailRecipients
    context_object_name = 'adminemailrecipent_list'
    template_name = 'admintemplates/emailrecipentslist.html'



class AdminEmailRecipentDetailView(AdminRequiredMixin, DetailView):
    model = EmailRecipients
    template_name = 'admintemplates/emailrecipentdetail.html'
    context_object_name = 'email_recipentdetail'




class AdminEmailRecipentUpdateView(AdminRequiredMixin,UpdateView):
    model = EmailRecipients
    form_class = EmailRecipientsForm
    template_name = 'admintemplates/emailrecipentsadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:adminemailrecipentlist')



class AdminEmailRecipentDeleteView(AdminRequiredMixin, DeleteView):
    model = EmailRecipients
    success_url = reverse_lazy('fweanapp:adminemailrecipentlist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class AdminMembershipFormDocumentsDetailView(AdminRequiredMixin,DetailView):

    model = Membership
    template_name = 'admintemplates/adminmembershipformdocumentsdetail.html'
    context_object_name = 'membershipdocuments' 


class AdminOfficeTimeAddView(AdminRequiredMixin,CreateView):
    model = OfficeTime
    template_name = 'admintemplates/adminofficetimeadd.html'
    form_class = AdminOfficeTimeForm 
    success_url = reverse_lazy('fweanapp:adminofficetimelist')


class AdminOfficeTimeListView(AdminRequiredMixin, ListView):
    model = OfficeTime
    context_object_name = 'adminofficetime_list'
    template_name = 'admintemplates/officetimelist.html'



class AdminOfficeTimeDeleteView(AdminRequiredMixin, DeleteView):
    model = OfficeTime
    success_url = reverse_lazy('fweanapp:adminofficetimelist')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



class AdminOfficeTimeUpdateView(AdminRequiredMixin,UpdateView):
    model = OfficeTime
    form_class = AdminOfficeTimeForm
    template_name = 'admintemplates/adminofficetimeadd.html'


    def get_success_url(self):

        return reverse_lazy('fweanapp:adminofficetimelist')





#Client views
def error_404_view(request,exception):
    # print('===')
    context = {
        'org': Organization.objects.first()
    }

    return render(request, '404.html',context, status=404)



class ClientRequiredMixin(object):

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['org'] = Organization.objects.first()
        context['donors'] = Donors.objects.filter(is_active=True).order_by('-date')
        context['successstoriesbase'] = SuccessStories.objects.filter(is_active=True).order_by('-date')
        context['successstorieslatestfive'] = SuccessStories.objects.filter(is_active=True).order_by('-date')[:5]
        context['ongoingprojects'] = Projects.objects.filter(accomplished=False,is_active=True)
        context['ongoingprojectshome'] = Projects.objects.filter(accomplished=False,is_active=True).order_by('-date')[:5]
        context['projectpartnersongoingprojects'] = Donors.objects.filter(projects__accomplished=False, is_active=True,projects__is_active=True).order_by('-date').distinct()


        context['successstorieshomepage'] = SuccessStories.objects.filter(is_active=True).order_by('-date')[:4]


        context['accomplishedprojects'] = Projects.objects.filter(accomplished=True,is_active=True)
        context['faqs'] = Faq.objects.filter(is_active=True)
        context['slider'] = Slider.objects.first()
        context['sliders'] = Slider.objects.all()
        context['subscribeform'] = SubscriberForm
        context['aboutuslist'] = AboutUs.objects.filter(is_active=True).order_by('-id')
        context['socialmedia_newsfeeds'] = SocialMediaNewsFeeds.objects.filter(is_active=True)
        context['newsandevents'] = NewsandMedia.objects.filter(is_active=True).order_by('-date')[:3]
        context['allnewsandevents'] = NewsandMedia.objects.filter(is_active=True).order_by('date')[:3]
        context['latestnews'] = NewsandMedia.objects.filter(is_active=True).order_by('-date')[:5]
        context['recentblogs'] = Blog.objects.filter(is_active=True).order_by('-date')[:3]
        context['moreblogs'] = Blog.objects.filter(is_active=True).order_by('id')[:3]

        context['importantlinks'] = FooterImportantLinks.objects.filter(is_active=True)
        context['upcomingeventshomepage'] = UpcomingEvents.objects.filter(is_active=True).order_by('-start_date')[:3]
        context['upcomingevents'] = UpcomingEvents.objects.filter(is_active=True).order_by('start_date')[:3]
        # context['publications'] = Publication.objects.filter(is_active=True).order_by('-date')
        context['recent_publications'] = Publication.objects.filter(is_active=True).order_by('-date')[:4]
        context['programmes'] = Programmes.objects.filter(is_active=True).order_by('date')
        context['moreprogrammes'] = Programmes.objects.filter(is_active=True).order_by('date')[:3]
        context['donor_list_datewise'] = Donors.objects.filter(is_active=True).order_by('-date')
        context['imagealbum_last'] = ImageAlbum.objects.last()
        context['office_time'] = OfficeTime.objects.all().filter(is_active=True)
        context['membershipcontentshomepage'] = MembershipContents.objects.filter(is_active=True).order_by('-date')
        # context['noticeshome'] = Notice.objects.filter(is_active=True).order_by('-date')
        return context




class ClientIndexView(ClientRequiredMixin,TemplateView):

    template_name = 'clienttemplates/home.html'


class ClientContactUsView(ClientRequiredMixin,TemplateView):
    template_name = 'clienttemplates/contactus.html'



class ClientAboutUsView(ClientRequiredMixin,TemplateView):
    template_name = 'clienttemplates/clientaboutus.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['aboutus'] = AboutUs.objects.first()

        return context

# class ClientAboutUsListView(ClientRequiredMixin,ListView):
#     model = AboutUs
#     context_object_name = 'aboutus_list'
#     template_name = 'clienttemplates/clientbase.html'
#
#
#
class ClientAboutUsDetailView(ClientRequiredMixin,DetailView):
    template_name = 'clienttemplates/clientaboutus.html'
    # context_object_name = 'aboutus'
    model = AboutUs

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        context['aboutus'] = AboutUs.objects.get(slug=slug)

        return context


class ClientNewsandEventsListView(ClientRequiredMixin,ListView):
    template_name = 'clienttemplates/clienteventlist.html'
    context_object_name = 'newsandeventlist'
    model = NewsandMedia
    queryset = NewsandMedia.objects.filter(is_active=True).order_by('-date')

    paginate_by = 5





class ClientNewsandEventsDetailView(ClientRequiredMixin,DetailView):
    template_name = 'clienttemplates/clienteventdetail.html'
    context_object_name = 'clienteventdetail'
    model = NewsandMedia



class ClientUpcomingEventsListView(ClientRequiredMixin,ListView):
    template_name = 'clienttemplates/clientupcomingeventlist.html'
    context_object_name = 'upcomingeventlist'
    model = UpcomingEvents
    queryset = UpcomingEvents.objects.filter(is_active=True).order_by('-start_date')
    paginate_by = 4


class ClientUpcomingEventsDetailView(ClientRequiredMixin,DetailView):
    template_name = 'clienttemplates/clientupcomingeventdetail.html'
    context_object_name = 'clientupcomingeventdetail'
    model = UpcomingEvents



#Async function for sending email to user when they subscribe.
# async def asyncsubscriberfun(email):
#     # print('email is now sending')
#     subject = 'Subscription'
#     sender = settings.EMAIL_HOST_USER
#     message =  "Thank you! You are subscribed to our latest news and updates (FWEAN Nepal)."
#     a_send_mail = sync_to_async(send_mail, thread_sensitive=False)
#     asyncio.create_task(a_send_mail(subject,
#                       message,
#                       sender,
#                       [email],
#                       fail_silently=False))


class SubscribeCreateView(SuccessMessageMixin, CreateView):
    template_name = "clienttemplates/clientbase.html"
    form_class = SubscriberForm
    success_url = reverse_lazy('fweanapp:indexpage')
    # success_message = "Thank you for subscribing us!!!"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        if Subscriber.objects.filter(email=email).exists():
            print('==================')

            data = {
                'error': "You have already subscribed!!"
            }


            return JsonResponse(data)
        else:
            
            # async def asyncsubscriberfun(email):
            #     # print('email is now sending')
            #     subject = 'Subscription'
            #     sender = settings.EMAIL_HOST_USER
            #     message =  "Thank you! You are subscribed to our latest news and updates (FWEAN Nepal)."
            #     a_send_mail = sync_to_async(send_mail, thread_sensitive=False)
            #     asyncio.create_task(a_send_mail(subject,
            #           message,
            #           sender,
            #           [email],
            #           fail_silently=False))
            
            
            # asyncio.run(asyncsubscriberfun(email))
            form.save()
            subject = 'Subscription'
            from_email = settings.EMAIL_HOST_USER
            contact_message = "Thank you! You are subscribed to our latest news and updates (FWEAN Nepal)."
            send_mail(subject,
                      contact_message,
                      from_email,
                      [email],
                      fail_silently=False)
            
            data = {
                'success': "Thank you for subscribing us!"
            }
            
            return JsonResponse(data)


        return super().form_valid(form)



class ClientImageAlbumListView(ClientRequiredMixin,ListView):
    template_name = 'clienttemplates/clientimagealbumlist.html'
    model = ImageAlbum


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albumslists'] = ImageAlbum.objects.filter(is_active=True).order_by('-id')

        return context


class ClientImageGalleryView(ClientRequiredMixin,DetailView):
    model = ImageAlbum
    template_name = 'clienttemplates/clientimagegallery.html'
    context_object_name = 'albumdetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = ImageMedia.objects.filter(album__slug=self.kwargs['slug'])


        return context


class ClientFaqView(ClientRequiredMixin,TemplateView):
    template_name = 'clienttemplates/clientfaq.html'


class ClientProjectsPartnersListView(ClientRequiredMixin,ListView):
    model = Donors
    template_name = 'clienttemplates/projectpartnerslist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['donors1'] = Donors.objects.filter(is_active=True).exclude(projects__isnull=True).order_by('-date')
        print(Donors.objects.exclude(projects__isnull=True))
        return context


class ClientProjectDetailView(ClientRequiredMixin,DetailView):
    model = Projects
    template_name = 'clienttemplates/clientprojectdetail.html'
    context_object_name = 'project'




class ClientProjectsListView(ClientRequiredMixin,DetailView):
    model = Donors
    template_name = 'clienttemplates/projectlist.html'
    # paginate_by = 5
    context_object_name = 'donor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context['accomplished'] = Projects.objects.filter(partner=self.object).filter(accomplished=True,is_active=True).order_by('-date')
        context['ongoing'] = Projects.objects.filter(partner=self.object).filter(accomplished=False,is_active=True).order_by('-date')

        return context


class ClientOngoingProjectsListView(ClientRequiredMixin,ListView):
    model = Projects
    context_object_name = 'ongoing'
    queryset = Projects.objects.filter(accomplished=False,is_active=True).order_by('-date')
    template_name = 'clienttemplates/projectsbystatuslist.html'
    paginate_by = 5



class ClientAccomplishedProjectsListView(ClientRequiredMixin,ListView):
    model = Projects
    context_object_name = 'accomplished'
    template_name = 'clienttemplates/projectsbystatuslist.html'
    queryset = Projects.objects.filter(accomplished=True,is_active=True).order_by('-date')
    paginate_by = 5

class ClientVideoGalleryListView(ClientRequiredMixin,ListView):
    model = Videos
    # context_object_name = 'videos_list'
    template_name = 'clienttemplates/clientvideogallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['thumbnail'] = Videos.objects.first()
        context['videos_list'] = Videos.objects.filter(is_active=True).order_by('-id')

        return context



#Client Successstories

class ClientSuccessStoriesListView(ClientRequiredMixin,ListView):
    model = SuccessStories
    context_object_name = 'successstorieslist'
    template_name = 'clienttemplates/clientsuccessstorieslist.html'

    queryset = SuccessStories.objects.filter(is_active=True).order_by('-date')
    paginate_by = 6



class ClientSuccessStoriesDetailView(ClientRequiredMixin,DetailView):
    model = SuccessStories
    template_name = 'clienttemplates/clientsucessstoriesdetail.html'
    context_object_name = 'successstory'

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj


class ClientBoardMembersView(ClientRequiredMixin,TemplateView):
    template_name = 'clienttemplates/clientboardmembers.html'

    def get_context_data(self, **kwargs):
        a = BoardMembers.objects.first()
        context = super().get_context_data(**kwargs)
        context['boardmembers'] = BoardMembers.objects.first()
        context['vicepresidents'] = a.vice_presidents.filter(is_active=True)
        context['past_presidents'] = a.immediate_past_presidents.filter(is_active=True)
        context['executivemembers'] = a.executive_members.filter(is_active=True)

        return context


class ClientBlogListView(ClientRequiredMixin,ListView):
    template_name = 'clienttemplates/bloglist.html'
    model = Blog
    context_object_name = 'blog_list'
    queryset = Blog.objects.all().order_by('-date')
    paginate_by = 6


class ClientBlogDetailView(ClientRequiredMixin,DetailView):
    template_name = 'clienttemplates/blogdetail.html'
    model = Blog
    context_object_name = 'blog_detail'

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = BlogCommentsForm
        context['blogcomments'] = BlogComments.objects.filter(blog_id=self.object.id).filter(publish=True)


        return context


class ClientBlogCommentCreateView(ClientRequiredMixin,CreateView):
    template_name = 'clienttemplates/blogdetail.html'
    model = BlogComments
    form_class = BlogCommentsForm

    def get_success_url(self):
        return reverse_lazy('fweanapp:clientblogdetail', kwargs={'slug': self.kwargs['slug']})

    def form_valid(self, form):
        print(self.object)
        form.instance.blog = Blog.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)


class ClientFeedbackView(ClientRequiredMixin,CreateView):
    template_name = 'clienttemplates/feedbacks.html'
    form_class = FeedBacksForm
    model = Feedbacks
    success_url = reverse_lazy('fweanapp:clientfeedbacks')


    def form_valid(self, form):
        
        data = form.cleaned_data
        # print(data)
             
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data1 = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data1)
        result = r.json()


        ''' End reCAPTCHA validation '''
        if result['success']:
            feedback = Feedbacks.objects.create(
            full_name = data['full_name'],
            email = data['email'],
            subject = data['subject'],
            message = data['message']

        )
            feedback.save()
            messages.success(self.request, ('Thank you we have received your feedback'))
            
            admin_email = User.objects.filter(is_superuser=True).first().email
            
            client_email = data['email']
            client_subject = data['subject']
            client_message = 'From: '+ form.cleaned_data['full_name'] + '\n'+ '\n'+ form.cleaned_data['message']
            host_email = admin_email
            host_message = "Thank you for your feedback."
            host_subject = "Automated Reply"
            sender = settings.EMAIL_HOST_USER
            datatuple = (
            (client_subject, client_message, client_email, [host_email]),
            (host_subject, host_message, sender, [client_email]),
            )
            send_mass_mail(datatuple)
            
            
        else:
            messages.warning(self.request,('Invalid reCAPTCHA. Please try again'))

        
        return redirect('fweanapp:clientfeedbacks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['feedbackform'] = FeedBacksForm
        return context


from io import BytesIO

from django.template.loader import get_template

from xhtml2pdf import pisa
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ClientPublicationView(ClientRequiredMixin,ListView):
    template_name = 'clienttemplates/publications.html'
    model = Publication
    queryset = Publication.objects.filter(is_active=True).order_by('-date')
    paginate_by = 5
    context_object_name = 'publications'



import subprocess
class ClientPublicationDetailView(ClientRequiredMixin, DetailView):
    template_name = 'clienttemplates/clientpublicationdetail.html'
    model = Publication
    context_object_name = 'publication_detail'

    # def get(self, request, *args, **kwargs):
    #     # with open('media/documents/PALLAV.pdf', 'rb') as pdf_document:
    #
    #     path = "media/documents/PALLAV.pdf"
    #     a = subprocess.call(["pdf2htmlEX", path], shell=False)
    #     print(a)
    #     # return HttpResponse('Hello')



    # def pdf_view(request):
    #     with open('media\documents\PALLAV-ADHIKAR-CV-pdf', 'r') as pdf:
    #         response = HttpResponse(pdf.read(), content_type='application/pdf')
    #         response['Content-Disposition'] = 'inline;filename=some_file.pdf'
    #         return response


class ClientIntroductionView(ClientRequiredMixin,TemplateView):
    template_name = 'clienttemplates/introduction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['feedbackform'] = FeedBacksForm
        return context


class ClientProgrammeListView(ClientRequiredMixin,ListView):
    model = Programmes
    context_object_name = 'programme_list'
    template_name = 'clienttemplates/programmelist.html'
    queryset = Programmes.objects.filter(is_active=True).order_by('-date')
    paginate_by = 4



class ClientProgrammeDetailView(ClientRequiredMixin,DetailView):
    model = Programmes
    context_object_name = 'programmedetail'
    template_name = 'clienttemplates/programmedetail.html'


class GeographicalCoverageView(ClientRequiredMixin,TemplateView):
    template_name = 'clienttemplates/geographicalcoverage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['feedbackform'] = FeedBacksForm
        return context


class ClientDonorListView(ClientRequiredMixin,ListView):
    model = Donors
    context_object_name = 'donor_lists'
    queryset =  Donors.objects.filter(is_active=True).order_by('-id')
    template_name = 'clienttemplates/donorlist.html'
    # paginate_by = 6


class ClientDonorDetailView(ClientRequiredMixin,DetailView):
    model = Donors
    context_object_name = 'donordetail'
    template_name = 'clienttemplates/donordetail.html'
    
class ClientMembershipContentsView(ClientRequiredMixin, DetailView):
    template_name = 'clienttemplates/clientmembershipcontents.html'
    model = MembershipContents
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        context['membershipcontents'] = MembershipContents.objects.get(slug=slug)
        return context
        

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')
# class ClientMembershipFormView(ClientRequiredMixin,CreateView):
#     model = Membership
#     form_class = MembershipForm
#     template_name = 'clienttemplates/membershipform.html'
#     success_url = reverse_lazy('fweanapp:membershipform')



#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests and instantiates blank versions of the form
#         and its inline formsets.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         membershiporganization_form = MembershipOrganizationFormSet()

#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   membershiporganization_form = membershiporganization_form,
#                                   ))

#     def post(self, request, *args, **kwargs):
#         """
#         Handles POST requests, instantiating a form instance and its inline
#         formsets with the passed POST variables and then checking them for
#         validity.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         membershiporganization_form = MembershipOrganizationFormSet(self.request.POST, self.request.FILES )
#         # print(imagemedia_form.cleaned_data)

#         if (form.is_valid() and membershiporganization_form.is_valid()):
#             return self.form_valid(form, membershiporganization_form)
#         else:
#             return self.form_invalid(form, membershiporganization_form)
    
#     def form_valid(self, form, membershiporganization_form):
#         """
#         Called if all forms are valid. Creates a Recipe instance along with
#         associated Ingredients and Instructions and then redirects to a
#         success page.
#         """
        
#         self.object = form.save()
#         membershiporganization_form.instance = self.object
#         membershiporganization_form.save()

                      
#         membership_detail= Membership.objects.get(id=self.object.id)
           

#         data1 = {
#              'membership_detail': Membership.objects.get(id=self.object.id),
#              'memberships' : MembershipOrganization.objects.filter(membership__id=self.object.id),
#              'app_url' : self.request.META['HTTP_HOST']
            
#         }
       
#         template = get_template('admintemplates/adminmembershipformdetail.html')

#         html  = template.render(data1)
#         result = BytesIO()
#         name1 = Membership.objects.get(id=self.object.id)
       
#         admin_email = User.objects.filter(is_superuser=True).first().email
#         pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)#, link_callback=fetch_resources)
#         pdf = result.getvalue()
#         filename = name1.name +' '+'membership form.pdf' 
#         to_emails = [admin_email]

#         a = EmailRecipients.objects.all()
        
#         # email_recipents = []
#         for b in a:
#             to_emails.append(b.email)
#         print(to_emails)     



#         subject = "New application for Membership"
#         email = EmailMessage(subject, name1.name + ' ' +"Membership form and required documents.", from_email=settings.EMAIL_HOST_USER, to=to_emails)
#         email.attach(filename, pdf, "application/pdf")
#         email.attach(membership_detail.registration_certificate.name, membership_detail.registration_certificate.read())
#         email.attach(membership_detail.pan_vat_certificate.name, membership_detail.pan_vat_certificate.read())
#         email.attach(membership_detail.citizenship_passport.name, membership_detail.citizenship_passport.read())
#         email.attach(membership_detail.tax_clearance.name, membership_detail.tax_clearance.read())
#         email.attach(membership_detail.cv.name, membership_detail.cv.read())

#         email.send(fail_silently=False)

#         email2 =  EmailMessage('Membership form (FWEAN)', 'Thank you! your membership request form has beed received (FWEAN)', from_email=settings.EMAIL_HOST_USER, to=[name1.email])
#         email2.send(fail_silently=False)

#         messages.success(self.request, ('Thank you! we have received your submission'))
#         return HttpResponseRedirect(self.get_success_url())

#     def form_invalid(self, form, membershiporganization_form):
#         """
#         Called if a form is invalid. Re-renders the context data with the
#         data-filled forms and errors.
#         """
#         # print('Form Invalid===============================')
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   membershiporganization_form=membershiporganization_form))      


def csrf_failure(request, reason=""):
   
    return render(request,"clienttemplates/csrf.html")




        