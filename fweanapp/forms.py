from django import forms

from django_summernote.widgets import SummernoteWidget
from .models import *
from froala_editor.widgets import FroalaEditor
from datetime import timedelta




class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter username...',
               'class': 'input100', 'id': 'loginname'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password...',
               'class': 'input100', 'id': 'loginpword'}))



class OrganizationForm(forms.ModelForm):
    geographical_description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Organization
        fields = "__all__"
        exclude = ('vat_pan',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                 'style': 'border: 1px solid gray;',
            }),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),

            'contact_no': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'alt_contact_no': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'map_location': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'pattern': '[\w\.-]+@[\w\.-]+\.\w{2,4}',
                'style': 'border: 1px solid gray;',

            }),
            'alt_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'slogan': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'facebook': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'twitter': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'youtube': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),

            'whatsapp': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'viber': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'mission': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'mission_icon': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'vision': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'vision_icon': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'goal': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'goal_icon': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'profile_image' : forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),

            'terms_and_conditions': SummernoteWidget(),
            'introduction': SummernoteWidget(),
            'style': 'border: 1px solid gray;',

            # 'geographical_description': SummernoteWidget(),
            'geographical_title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),

            'geographical_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            
            'district_reached': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
             'no_of_members': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
             'no_project_accomplished': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
        }


from django.forms.models import inlineformset_factory,formset_factory
ImageMediaFormSet = inlineformset_factory(
    ImageAlbum,ImageMedia, fields=['image','title'],can_delete = True,
    widgets= {
        'image': forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'style': "border: 1px solid gray;",
        }),
        'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Write image caption here..(optional)',
            'style': "border: 1px solid gray;",
        }),

    }
)



class ImageAlbumForm(forms.ModelForm):
    class Meta:
        model = ImageAlbum
        fields = "__all__"
        # exclude = ()
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control col-md-12 font-weight-bold text-dark ',
                'placeholder': 'Desc..',

                "style": "height: 170px; border: 1px solid gray;"
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),


        }



class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = "__all__"
        # exclude = ()
        widgets = {
            'image1': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),'image2': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ' ,
                'style': "border: 1px solid gray;",

            }),'image3': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),'image4': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),'image5': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter slider title'
            }),
            'sub_title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter slider sub-title (optional)'
            }),


        }



class AboutUsForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = AboutUs
        fields = "__all__"
        # exclude = ()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter slider title'


        }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),


        # 'description':SummernoteWidget(),

        }



class ProjectsForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Projects
        fields = "__all__"
        # exclude = ()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter  title'

        }),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),


            'partner': forms.Select(attrs={
                'class': 'form-control singleselect',
                'style': "border: 1px solid gray;",
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control col-md-12 font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'type': 'date',
                'placeholder': 'Check in',

            }),



        }



class ProgrammeForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Programmes
        fields = "__all__"
        # exclude = ()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter title'


        }),
            'date': forms.DateInput(attrs={
                'class': 'form-control col-md-12 font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'type': 'date',
                'placeholder': 'Check in',

            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            # 'description': SummernoteWidget(),


        }


class SuccessStoriesForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = SuccessStories
        fields = "__all__"
        exclude = ('slug','view_count')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter title'


        }),
            'image1': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),
            'image2': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),
            'image3': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),
            # 'description': SummernoteWidget(),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'style': 'border: 1px solid gray;',

            }),


        }


class BlogForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Blog
        fields = "__all__"
        exclude = ['view_count']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title...'

            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',

            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'style': 'border: 1px solid gray;',

            }),


        }

class DonorsForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title...'

            }),

            'logo': forms.ClearableFileInput(attrs={
                'class': 'form-control',

            }),
            'description': SummernoteWidget(),
             'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'style': 'border: 1px solid gray;',

            }),
             'link': forms.URLInput(
                attrs={
                    'type': 'url',
                    'class': 'form-control',
                    'style': 'border: 1px solid gray;',
                    'placeholder':'enter donor website link'

                }
            ),


        }


class FaqForm(forms.ModelForm):
    answer = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Faq
        fields = ['question', 'answer','is_active']
        widgets = {
            # 'answer': SummernoteWidget(),
            'question': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Question'
            }),

        }


class ImportantLinksForm(forms.ModelForm):
    class Meta:
        model = FooterImportantLinks
        fields = ['title', 'link','is_active']
        widgets = {
            'link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'add link'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),


        }

class UpcomingEventsForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = UpcomingEvents
        fields = "__all__"
        # exclude = ()
        widgets = {
            'image1': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }), 'image2': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }), 'image3': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            # 'description': SummernoteWidget

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'style': 'border: 1px solid gray;',

            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'style': 'border: 1px solid gray;',

            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),



        }


class NewsandMediaForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = NewsandMedia
        fields = "__all__"
        # exclude = ()
        widgets = {
            'image1': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }), 'image2': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),


            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter news title',
            }),


            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter location',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control col-md-12 font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'type': 'date',
                'placeholder': 'Check in',

            }),



        }


class SocialMediaNewsForm(forms.ModelForm):
    source = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = SocialMediaNewsFeeds
        fields = ['title', 'source','is_active','date']
        widgets = {
            # 'source': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'style': 'border: 1px solid gray;',
            #     'placeholder': 'Enter iframe source'
            # }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter title'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control col-md-12 font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'type': 'date',
                'placeholder': 'Check in',

            }),


        }


class AdminProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),


        }


class AdminOfficeTimeForm(forms.ModelForm):

    class Meta:
        model = OfficeTime
        fields = ['day','time','is_active']
        widgets = {
            'day': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
            }),


        }




class PasswordUpdateForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter current password',
        'style': 'border: 1px solid gray;',
    }))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter new password',
        'style': 'border: 1px solid gray;',
    }))
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm new password',
        'style': 'border: 1px solid gray;',
    }))

    def clean(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_new_password")
        if (len(new_password) or len(confirm_new_password)) < 8:
            raise forms.ValidationError(
                "Password must be atleast 8 characters long")
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                "New passwords did not match!")



class AdminSubscriberUpdateForm(forms.ModelForm):


    class Meta:
        model = Subscriber
        fields =  ['is_active']


class SubscriberForm(forms.ModelForm):


    class Meta:
        model = Subscriber
        fields = "__all__"
        exclude = ['is_viewed']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control input-lg  ',
                'type': 'email',

                'placeholder': 'Enter Your Email'
            }),

        }

class VideoAddForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = "__all__"
        exclude = ['video_id','thumbnail']
        widgets = {
            # 'thumbnail': forms.ClearableFileInput(attrs={
            #     'class': 'form-control  font-weight-bold text-dark ',
            #     'style': "border: 1px solid gray;",
            #
            # }),

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter title',
            }),


            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter video url',
            }),



        }


class BoardMembersAddForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(BoardMembersAddForm, self).__init__(*args, **kwargs)
    #
    #     # add custom error messages
    #     self.fields['name'].error_messages.update({
    #         'required': 'Some fields are missing',
    #     })

    class Meta:
        model = BoardMembers
        fields = '__all__'
        # exclude = '__all__'
        # exclude= ['vice_president_image','vice_president_designation','vice_president_name','executive_member_designation','executive_member_name','executive_member_image']

        widgets = {
            'president_image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",


            }),

            'president_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter name',
            }),
            'president_designation': forms.TextInput(attrs={
                        'class': 'form-control',
                        'style': 'border: 1px solid gray;',
                        'placeholder': 'Designation',
                    }),
            # 'immediate_past_president_image': forms.ClearableFileInput(attrs={
            #     'class': 'form-control font-weight-bold text-dark ',
            #     'style': "border: 1px solid gray;",
            #
            # }),
            #
            # 'immediate_past_president_name': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'style': 'border: 1px solid gray; ',
            #     'placeholder': 'Enter name',
            # }),
            # 'immediate_past_president_designation': forms.TextInput(attrs={
            #             'class': 'form-control',
            #             'style': 'border: 1px solid gray;',
            #             'placeholder': 'Designation',
            #         }),

            # 'vice_president_image': forms.ClearableFileInput(attrs={
            #     'class': 'form-control  font-weight-bold text-dark ',
            #     'style': "border: 1px solid gray;",
            #
            # }),
            #
            # 'vice_president_name': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'style': 'border: 1px solid gray;',
            #     'placeholder': 'Enter name',
            # }),
            # 'vice_president_designation': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'style': 'border: 1px solid gray;',
            #     'placeholder': 'Designation',
            # }),


            'general_secretary_image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            'general_secretary_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter name',
            }),
            'general_secretary_designation': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Designation',
            }),

            'secretary_image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            'secretary_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter name',
            }),
            'secretary_designation': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Designation',
            }),

            'treasurer_image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            'treasurer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter name',
            }),
            'treasurer_designation': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Designation',
            }),

            'vice_presidents': forms.SelectMultiple(attrs={
                'class': 'form-control multipleselect text-black',
                'placeholder': 'Vice presidents',
                'style': 'min-height: 202px;'

            }),
            'executive_members': forms.SelectMultiple(attrs={
                'class': 'form-control multipleselect',
                'placeholder': 'Executive Members',
            }),
            'immediate_past_presidents': forms.SelectMultiple(attrs={
                'class': 'form-control multipleselect',
                'placeholder': 'Immediate past presidents',
            }),

            # 'executive_member_image': forms.ClearableFileInput(attrs={
            #     'class': 'form-control  font-weight-bold text-dark ',
            #     'style': "border: 1px solid gray;",
            #
            # }),
            #
            # 'executive_member_name': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'style': 'border: 1px solid gray;',
            #     'placeholder': 'Enter name',
            # }),
            # 'executive_member_designation': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'style': 'border: 1px solid gray;',
            #     'placeholder': 'Designation',
            # }),





        }




class BoardVicePresidentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BoardVicePresidentForm, self).__init__(*args, **kwargs)

        # add custom error messages
        self.fields['vice_president_name'].error_messages.update({
            'required': 'Some fields are missing',
        })

    class Meta:
        model = BoardVicePresidents
        fields = ['vice_president_name','vice_president_designation','vice_president_image','is_active']

        widgets = {
            'vice_president_image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            'vice_president_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter vice president name',
            }),
            'vice_president_designation': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Designation',
            }),



        }


class ExecutiveMemberForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(BoardMembersAddForm, self).__init__(*args, **kwargs)
    #
    #     # add custom error messages
    #     self.fields['name'].error_messages.update({
    #         'required': 'Some fields are missing',
    #     })

    class Meta:
        model = BoardExecutiveMembers
        fields = ['executive_member_name','executive_member_designation','executive_member_image','is_active']

        widgets = {




            'executive_member_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter executive member name',
            }),

            'executive_member_designation': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Designation',
            }),

            'executive_member_image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),



        }

class ImmediatePastPresidentForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(BoardMembersAddForm, self).__init__(*args, **kwargs)
    #
    #     # add custom error messages
    #     self.fields['name'].error_messages.update({
    #         'required': 'Some fields are missing',
    #     })

    class Meta:
        model = BoardImmediatePastPresident
        fields = ['is_active','immediate_past_president_name','immediate_past_president_designation','immediate_past_president_image']

        widgets = {




            'immediate_past_president_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter past president name',
            }),

            'immediate_past_president_designation': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Designation',
            }),

            'immediate_past_president_image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),



        }





class FeedBacksForm(forms.ModelForm):



    class Meta:
        model = Feedbacks
        fields = '__all__'
        exclude = ['is_viewed']

        widgets = {




            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter your name',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Email',
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'placeholder': 'Subject',

            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray; height: 200px;",
                'placeholder': 'message',

            }),



        }


class BlogCommentsForm(forms.ModelForm):



    class Meta:
        model = BlogComments
        fields = '__all__'
        exclude = ['blog','publish']

        widgets = {




            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter your name',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Email',
            }),


            'comment': forms.TextInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray; height:100px;",
                'placeholder': "Your comment",

            }),



        }

class BlogCommentsPublishForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ['publish']



class PublicationForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor,required=False)
    watermark = forms.BooleanField(required=False)
    class Meta:
        model = Publication
        fields = '__all__'
        exclude = ['download_count']



        widgets = {




            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter your name',
            }),

             'image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control col-md-12 font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'type': 'date',
                'placeholder': 'Check in',

            }),


            # 'description': forms.TextInput(attrs={
            #     'class': 'form-control  font-weight-bold text-dark ',
            #     'style': "border: 1px solid gray; height:100px;",
            #     'placeholder': "write decesription (optional)",
            #
            # }),



        }


class MembershipContentsForm(forms.ModelForm):
    description = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = MembershipContents
        fields = ['is_active','date','description','title','image']



        widgets = {




            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter title',
            }),

             'image': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),


            'date': forms.DateInput(attrs={
                'class': 'form-control col-md-12 font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'type': 'date',
                'placeholder': 'Check in',

            }),


            # 'description': SummernoteWidget(),



        }



MembershipOrganizationFormSet = inlineformset_factory(
    Membership,MembershipOrganization, fields=['name_of_other_org','designation_of_other_org'],can_delete = True,
    extra=1,  widgets= {
        
        'name_of_other_org': forms.TextInput(attrs={
            'class': 'form-control col-4',
            'placeholder': 'Name of organization',
            'style': "border: 1px solid gray;",
        })
        ,
        'designation_of_other_org': forms.TextInput(attrs={
            'class': 'form-control col-4',
            'placeholder': 'Designation',
            'style': "border: 1px solid gray;",
        }),

    }
)
        
        
        
        
class MembershipForm(forms.ModelForm):

    class Meta:
        model = Membership
        fields = '__all__'
        # exclude = ['membership_proposed_by','membership_applied_for']

        import datetime
        

        widgets = {

             'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),


            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter your name',
            }),

            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'type': 'date',
                'placeholder': 'Date of birth',
                'max':datetime.datetime.now().date(),
                'id': 'datefield'

            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter your address',
            }),
            'fathers_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Father\'s name',
            }),
            'mothers_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Mother\'s name',
            }),

            'marital_status': forms.Select(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'id': "martial_status",

            }),

            'spouse_name': forms.TextInput(attrs={
                'class': 'form-control spouse',
                'style': 'border: 1px solid gray; margin-bottom:7px;',
                'placeholder': 'Spouse\'s name',
                # 'class': "spouse",
            }),
            'spouse_profession': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; margin-bottom:7px;',
                'placeholder': 'Spouse\'s profession',
            }),
            'spouse_company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; margin-bottom:7px;',
                'placeholder': 'Spouse\'s company',
            }),
            'son_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; margin-bottom:7px;',
                'placeholder': 'Son\'s name',
            }),
            'daughter_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; margin-bottom:7px;',
                'placeholder': 'Daughter\'s name',
            }),

            'mobile_no': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'your mobile no.',
                 'oninput':"javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);",
        
                  'maxlength' : 10
            }),
            'phone_no': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'your phone no.',
                 'oninput':"javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);",
        
                  'maxlength' : 10
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Your email',
            }),

            'educational_qualification': forms.Select(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

            'edu_qualifications_others': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; height:80px;',
                'placeholder': 'Please specify',
            }),

            'enterprise_type': forms.Select(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),
            'enterprise_type_others': forms.TextInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray; height:80px;",
                 'placeholder': 'Please specify',

            }),
            'enterprise_scale': forms.Select(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),
            'additional_personal_information': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; height:100px;',
                'placeholder': 'Please specify',
            }),

            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'company name',
            }),
            'company_address': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'company address',
            }),
            'company_phone_no': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'company name',
                'maxlength':10
            }),

            'company_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'company email',
            }),
            'company_website': forms.URLInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'company website',
            }),
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Designation',
            }),

            'pan_vat': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'pan vat no.',
                'maxlength':15
            }),

            'registration_date':  forms.DateInput(attrs={
                'class': 'form-control font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",
                'type': 'date',
                'placeholder': 'Registration Date',
                'max':datetime.datetime.now().date()

            }),

            'yearly_turnover': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Yearly Turnover',
            }),

            'current_assets': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Current Assets',
                'maxlength':15
            }),
            'correspondence_to_reach': forms.Select(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Please Specify',
            }),

            'correspondence_to_reach_others': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; height:80px;',
                'placeholder': 'Please Specify',
            }),
            'name_of_other_org': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; ',
                'placeholder': 'Please Specify',
            }),
            'designation_of_other_org': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; ',
                'placeholder': 'Please Specify',
            }),

            'how_did_you_know_about_fwean': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; height:80px;',
                'placeholder': 'Please Specify',
            }),

             'why_do_you_want_to_become_a_member': forms.CheckboxSelectMultiple( attrs={
                 'class':'checkboxes',
                 'required': True,
                 'autocomplete':'off'
             }),

            'why_do_you_want_to_become_a_member_other': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; height:80px;',
                'placeholder': 'Please Specify',
                
            }),


            
            'contributing_to_the_objectives': forms.CheckboxSelectMultiple( attrs={
                 'class':'checkboxes2',
                 'required': True,  
                 'autocomplete':'off'
             }),



            'contributing_to_the_objectives_other': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; height:80px;',
                'placeholder': 'Please Specify',
                
            }),
            'elborate_on_your_choices': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; height:130px;',
                'placeholder': 'Please Elaborate',
            }),

            'time_can_you_give_to_fwean_activities': forms.Select(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                
            }),
            'time_would_yo_prefer_for_fwean_programs': forms.Select(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
              
            }),

            'type_of_programs_would_you_want_in_fwean': forms.CheckboxSelectMultiple( attrs={
                 'class':'checkboxes3',
                 #'required': True,  
                 'autocomplete':'off'
             }),

            'type_of_programs_would_you_want_in_fwean_others': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray; height:100px;',
                'placeholder': 'Please Specify',
            }),


            'membership_proposed_by': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Please Specify',
            }),



            'membership_applied_for': forms.Select(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
              
            }),




             'registration_certificate': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),


              'pan_vat_certificate': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

           

             'citizenship_passport': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

             'cv': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),

              'tax_clearance': forms.ClearableFileInput(attrs={
                'class': 'form-control  font-weight-bold text-dark ',
                'style': "border: 1px solid gray;",

            }),




            # 'why_do_you_want_to_become_a_member': forms.SelectMultiple(attrs={
            #     'class': 'form-control  font-weight-bold text-dark ',
            #     'style': "border: 1px solid gray;",
            #     'type':'checkbox'
            #
            # }),
            # 'date': forms.DateInput(attrs={
            #     'class': 'form-control col-md-12 font-weight-bold text-dark ',
            #     'style': "border: 1px solid gray;",
            #     'type': 'date',
            #     'placeholder': 'Check in',

            # }),




        }

    def clean_picture(self):
       picture = self.cleaned_data.get("picture")
       if picture:
            if picture.size > 2*1024*1024:
                raise forms.ValidationError("Image file too large. Please upload your image less than 2 MB.")
            return picture
       else:
            raise forms.ValidationError("Couldn't read uploaded image")
            
            
            
class EmailRecipientsForm(forms.ModelForm):
    class Meta:
        model = EmailRecipients
        fields = "__all__"
        # exclude = ['video_id','thumbnail']
        widgets = {
            # 'thumbnail': forms.ClearableFileInput(attrs={
            #     'class': 'form-control  font-weight-bold text-dark ',
            #     'style': "border: 1px solid gray;",
            #
            # }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Enter name',
            }),


             'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid gray;',
                'placeholder': 'Email',
            }),



        }             