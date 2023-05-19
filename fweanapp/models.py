from django.db import models
from django.contrib.auth.models import User, Group
from django.db import models
# from multiselectfield import MultiSelectField
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import pre_save
from .utils import unique_slug_generator,slugify,random_string_generator

from froala_editor.fields import FroalaField

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def get_month(self):
        return self.updated_at.strftime('%b')

    def get_date(self):
        return self.updated_at.strftime('%d')

    def get_year(self):
        return self.updated_at.strftime('%Y')

    def get_week(self):
        return self.updated_at.strftime('%a')

    def get_time(self):
        return self.updated_at.strftime('%I'":"'%M%p')

    class Meta:
        abstract = True


class Organization(TimeStamp):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='organization')
    address = models.CharField(max_length=500)
    profile_image = models.ImageField(upload_to='organization')
    contact_no = models.CharField(max_length=200)
    alt_contact_no = models.CharField(max_length=200, null=True, blank=True)
    map_location = models.CharField(max_length=2000, null=True, blank=True)
    email = models.EmailField()
    alt_email = models.EmailField(null=True, blank=True)
    slogan = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=200, null=True, blank=True)
    viber = models.CharField(max_length=200, null=True, blank=True)
    terms_and_conditions = models.TextField(null=True, blank=True)
    introduction = models.TextField()

    mission = models.CharField(max_length=1000, null=True, blank=True)
    mission_icon = models.ImageField(upload_to='organization')
    vision = models.CharField(max_length=1000, null=True, blank=True)
    vision_icon = models.ImageField(upload_to='organization')
    goal = models.CharField(max_length=1000, null=True, blank=True)
    goal_icon = models.ImageField(upload_to='organization')

    geographical_title = models.CharField(max_length=200, null=True, blank=True)
    geographical_description  = FroalaField(options={
    'toolbarInline': True,
  })
    geographical_image = models.ImageField(upload_to='geographical',)
    district_reached = models.IntegerField(default=0)
    no_of_members = models.IntegerField(default=0)
    no_project_accomplished = models.IntegerField(default=0)
    def __str__(self):
        return self.name



# class OrganzationStructure(TimeStamp):
#     pass
#
#


class OfficeTime(TimeStamp):
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=200)
    
    def __str__(self):
        return self.day

class Donors(TimeStamp):
    title = models.CharField(max_length=100)
    slug =models.SlugField(unique=True, null=True, editable=False, blank=True,max_length=100)
    logo = models.ImageField(upload_to='Donors')
    description = FroalaField(options={
        'toolbarInline': True,
    })
    date = models.DateField(default=timezone.now)
    link = models.CharField(max_length=200,default='')
    def __str__(self):
        return self.title
    
    def get_active(self):
        return Projects.objects.filter(partner=self,is_active=True,accomplished=False)    


class Programmes(TimeStamp):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True,editable=False, blank=True,max_length=100)
    image = models.ImageField(upload_to='Programmes')
    description = FroalaField(options={
        'toolbarInline': True,
    })
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.title



class Projects(TimeStamp):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True,editable=False, blank=True,max_length=100)
    partner = models.ForeignKey(Donors,on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='Projects')
    description = FroalaField(options={
        'toolbarInline': True,
    })
    accomplished = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

# class GeographicalCoverage(TimeStamp):
#     pass


class SuccessStories(TimeStamp):
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True,max_length=100)
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="successstories")
    image2 = models.ImageField(upload_to="successstories", null=True, blank=True)
    image3 = models.ImageField(upload_to="successstories", null=True, blank=True)
    description = FroalaField(options={
        'toolbarInline': True,
    })
    date = models.DateField(default=timezone.now)
    
    view_count = models.BigIntegerField(default=0)
    
    def add_view(self):
        if self.view_count is not None:
            self.view_count += 1
        else:
            self.view_count = 0
    
    def __str__(self):
        return self.title

class ImageAlbum(TimeStamp):
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True,max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery",null=False,blank=False)
    description = FroalaField(options={
        'toolbarInline': True,
    },)

    def get_photos(self):
        return ImageMedia.objects.filter(album=self)



    def __str__(self):
        return self.title


class ImageMedia(TimeStamp):
    title = models.CharField(max_length=200,null=True, blank=True)
    album = models.ForeignKey(ImageAlbum, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.album.title


#
# class NewsAndMedia(TimeStamp):
#     pass
#
#
class Videos(TimeStamp):
    video_url = models.URLField()
    video_id = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='video thumbnail',null=True,blank=True)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from urllib import parse
        url = self.video_url
        url_parsed = parse.urlparse(url)
        qsl = parse.parse_qs(url_parsed.query)
        print(qsl)
        if qsl:
            self.video_id = qsl['v'][0]

        super(Videos, self).save(*args, **kwargs)

class Subscriber(TimeStamp):
    email = models.EmailField(unique=True)
    
    is_viewed = models.BooleanField(default=False)
    
    def add_view(self):
        self.is_viewed = True
        
    def __str__(self):
        return self.email


class Faq(TimeStamp):
    question = models.CharField(max_length=500)
    answer = FroalaField(options={
    'toolbarInline': True,
  })

    def __str__(self):
        return self.question



class FooterImportantLinks(TimeStamp):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title
#
# class FweanInMedia(TimeStamp):
#     pass


class AboutUs(TimeStamp):
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True,max_length=100)
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='Aboutus',null=True,blank=True)
    description = FroalaField(options={
    'toolbarInline': True,
  })

    def __str__(self):
        return self.title

class Blog(TimeStamp):
    slug = models.SlugField(unique=True, null=True,editable=False, blank=True,max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Blog',null=True,blank=True)
    description = FroalaField(options={
        'toolbarInline': True,
    })
    view_count = models.BigIntegerField(default=0)
    date = models.DateField(default=timezone.now)
    def add_view(self):
        if self.view_count is not None:
            self.view_count += 1
        else:
            self.view_count = 0

    def __str__(self):
        return self.title


class BlogComments(TimeStamp):
    publish = models.BooleanField(default=False)
    name = models.CharField(max_length=150)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    email = models.EmailField()
    comment = models.TextField()

    # def save(self, *args, **kwargs):
    #     self.is_active = False
    #     super(BlogComments, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Slider(TimeStamp):
    image1 = models.ImageField(upload_to='Sliders')
    image2 = models.ImageField(upload_to='Sliders')
    image3 = models.ImageField(upload_to='Sliders')
    image4 = models.ImageField(upload_to='Sliders',null=True,blank=True)
    image5 = models.ImageField(upload_to='Sliders',null=True,blank=True)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title


class UpcomingEvents(TimeStamp):
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True,max_length=100)
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="Events")
    image2 = models.ImageField(upload_to="Events",null=True,blank=True)
    image3 = models.ImageField(upload_to="Events",null=True,blank=True)
    description = FroalaField(options={
        'toolbarInline': True,
    })
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True,blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title




class NewsandMedia(TimeStamp):
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True,max_length=100)
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="News")
    image2 = models.ImageField(upload_to="News",null=True,blank=True)
    description = FroalaField(options={
    'toolbarInline': True,
  })
    location = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title



class SocialMediaNewsFeeds(TimeStamp):
    title = models.CharField(max_length=200)
    source = FroalaField(options={
        'toolbarInline': True,
    })
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.title


class BoardExecutiveMembers(TimeStamp):
    executive_member_name = models.CharField(max_length=200)
    executive_member_designation = models.CharField(max_length=200)
    executive_member_image = models.ImageField(upload_to="BoardMembers")

    def __str__(self):
        return self.executive_member_name

class BoardVicePresidents(TimeStamp):
    vice_president_name = models.CharField(max_length=200)
    vice_president_designation = models.CharField(max_length=200)
    vice_president_image = models.ImageField(upload_to="BoardMembers")

    def __str__(self):
        return self.vice_president_name + 'id is: ' + str(self.id)


class BoardImmediatePastPresident(TimeStamp):
    immediate_past_president_name = models.CharField(max_length=200)
    immediate_past_president_designation = models.CharField(max_length=200)
    immediate_past_president_image = models.ImageField(upload_to="BoardMembers")

    def __str__(self):
        return self.immediate_past_president_name


class BoardMembers(TimeStamp):
    president_name = models.CharField(max_length=200)
    president_designation = models.CharField(max_length=200)
    president_image = models.ImageField(upload_to="BoardMembers")
    vice_presidents = models.ManyToManyField(BoardVicePresidents)
    executive_members = models.ManyToManyField(BoardExecutiveMembers)
    immediate_past_presidents = models.ManyToManyField(BoardImmediatePastPresident)

    general_secretary_name = models.CharField(max_length=200)
    general_secretary_designation = models.CharField(max_length=200)
    general_secretary_image = models.ImageField(upload_to="BoardMembers")

    secretary_name = models.CharField(max_length=200)
    secretary_designation = models.CharField(max_length=200)
    secretary_image = models.ImageField(upload_to="BoardMembers")

    treasurer_name = models.CharField(max_length=200)
    treasurer_designation = models.CharField(max_length=200)
    treasurer_image = models.ImageField(upload_to="BoardMembers")


    def __str__(self):
        return self.president_name + ' id is: ' + str(self.id)




class Feedbacks(TimeStamp):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message  = models.TextField()

    def __str__(self):
        return self.full_name
    
    is_viewed = models.BooleanField(default=False)
    
    def add_view(self):
        self.is_viewed = True

class Publication(TimeStamp):
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True,max_length=100)
    image = models.ImageField(upload_to='publications',null=True,blank=True)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents')
    date = models.DateField(default=timezone.now)
    description = FroalaField(options={
        'toolbarInline': True,
    },null=True,blank=True)
    download_count = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.title

    


class MembershipContents(TimeStamp):
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True,max_length=100)
    image = models.ImageField(upload_to='membershipcontents',null=True,blank=True)
    title = models.CharField(max_length=100)
    # file = models.FileField(upload_to='documents')
    date = models.DateField(default=timezone.now)
    description = FroalaField(options={
        'toolbarInline': True,
    })

    def __str__(self):
        return self.title
        


from multiselectfield import MultiSelectField
marital_choices = [('Single','Single'),('Married','Married')]
edu_qualifications = [('Graduate','Graduate'),('Post Graduate','Post Graduate'),('Professional','Professional')]
enterprise_type= [('Manufacturing','Manufacturing'),('Trading','Trading'),('Agriculture','Agriculture'),('Service','Service')]
enterprise_scale= [('Micro/Cottage','Micro/Cottage'),('Small','Small'),('Medium','Medium'),('Large','Large')]
why_do_you_want_to_become_a_member_choices = [('Networking among fellow women.','Networking among fellow women.'),('Business / Profession','Business / Profession.'),('Legal issues','Legal issues.'),('Women issues','Women issues.'),('Opportunities to participate in training programs','Opportunities to participate in training programs.'),('Expert opinion and guidance in your area of activity','Expert opinion and guidance in your area of activity.')]
contributing_to_the_objectives_choices = [('As trainers at (seminars, workshops) etc.','As trainers at seminars, workshops etc.'),('Becoming a part of the organizational structure of FWEAN','Becoming a part of the organizational structure of FWEAN'),('Fund Raising / Sponsoring / Co-sponsoring events','Fund Raising / Sponsoring / Co-sponsoring events'),('Contributing in Newsletter','Contributing in Newsletter'),('Attending seminars, conventions, debates, etc. ','Attending seminars, conventions, debates, etc. '),('Membership Development','Membership Development')]
time_can_you_give_to_FWEAN_activities_choices = [('1-3 hours per week','1-3 hours per week'),('1-3 hours per fortnight','1-3 hours per fortnight'),('1-3 hours per month','1-3 hours per month'),('1-3 hours per quarter','1-3 hours per quarter'),('1-3 hours per half year','1-3 hours per half year'),('1-3 hours per year','1-3 hours per year')]
time_would_yo_prefer_for_fwean_programs_choices = [('Weekdays','Weekdays'),('Weekends','Weekends'),('Morning','Morning'),('Afternoon','Afternoon'),('Evening','Evening')    ]
type_of_programs_would_you_want_in_fwean_choices = [('Entrepreneurial','Entrepreneurial'),('Business Support','Business Support'),('Finance','Finance'),('Marketing','Marketing'),('Advocacy','Advocacy'),('Networking','Networking'),('Economic','Economic'),('Women Issues','Women Issues'),('Social','Social')]
membership_applied_for_choices = [('Individual','Individual'),('Institutional','Institutional')]




from django.core.validators import FileExtensionValidator
class Membership(TimeStamp):

    picture = models.ImageField(upload_to='members')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100,choices=marital_choices,blank=False)
    spouse_name = models.CharField(max_length=100,null=True,blank=True)
    spouse_profession = models.CharField(max_length=100,null=True,blank=True)
    spouse_company_name = models.CharField(max_length=100,null=True,blank=True)
    son_name = models.CharField(max_length=100,null=True,blank=True)
    daughter_name = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    educational_qualification = models.CharField(max_length=100,choices=edu_qualifications, blank=True, null=True)
    edu_qualifications_others = models.TextField(blank=True, null=True)
    #Enterprise
    enterprise_type = models.CharField(max_length=100,choices=enterprise_type, blank=True, null=True)
    enterprise_type_others = models.TextField(blank=True, null=True)
    enterprise_scale = models.CharField(max_length=100,choices=enterprise_scale, blank=False)

    additional_personal_information = models.TextField(null=True, blank=True)
    #Company Detail
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_phone_no = models.CharField(max_length=10)
    company_email = models.EmailField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    designation = models.CharField(max_length=100)
    pan_vat = models.CharField(max_length=20)
    registration_date = models.DateField()
    yearly_turnover = models.CharField(max_length=20)
    current_assets = models.CharField(max_length=20)

    
    correspondence_to_reach = models.CharField(max_length=100,choices=[('Residence','Residence'),('Office','Office')], blank=True, null=True)
    correspondence_to_reach_others = models.TextField(blank=True, null=True)
    
    
    
    
    how_did_you_know_about_fwean = models.TextField()
    why_do_you_want_to_become_a_member = MultiSelectField(choices=why_do_you_want_to_become_a_member_choices)
    why_do_you_want_to_become_a_member_other = models.TextField(blank=True, null=True)

    contributing_to_the_objectives = MultiSelectField(choices=contributing_to_the_objectives_choices)
    contributing_to_the_objectives_other = models.TextField(blank=True, null=True)
    elborate_on_your_choices = models.TextField()
    time_can_you_give_to_fwean_activities = models.CharField(max_length=100,choices=time_can_you_give_to_FWEAN_activities_choices, blank=False)
    time_would_yo_prefer_for_fwean_programs = models.CharField(max_length=100,choices=time_would_yo_prefer_for_fwean_programs_choices)
    type_of_programs_would_you_want_in_fwean = MultiSelectField(choices=type_of_programs_would_you_want_in_fwean_choices)
    type_of_programs_would_you_want_in_fwean_others = models.TextField(blank=True, null=True)
    membership_proposed_by = models.CharField(max_length=100)
    membership_applied_for = models.CharField(max_length=100,choices=membership_applied_for_choices)
    
    
    registration_certificate = models.FileField(upload_to='membership_documents' )
    pan_vat_certificate = models.FileField(upload_to='membership_documents' )
    citizenship_passport = models.FileField(upload_to='membership_documents' )
    cv = models.FileField(upload_to='membership_documents' )
    tax_clearance = models.FileField(upload_to='membership_documents' )

    def __str__(self):
        return self.name

    def get_organization(self):
        return MembershipOrganization.objects.filter(membership=self)
        
    


class MembershipOrganization(TimeStamp):
    title = models.CharField(max_length=200,null=True, blank=True)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE,related_name='membership')
    name_of_other_org = models.TextField()
    designation_of_other_org = models.TextField()

    def __str__(self):
        return self.name_of_other_org


class EmailRecipients(TimeStamp):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name            
        

class Carrer(TimeStamp):
    
    slug = models.SlugField(unique=True, null=True, editable=False,blank=True, max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='career')
    description = description = FroalaField(options={
        'toolbarInline': True,
    })
    
    date = models.DateField(default=timezone.now)
    view_count = models.BigIntegerField(default=0)
    

    def add_view(self):
        if self.view_count is not None:
            self.view_count += 1
        else:
            self.view_count = 0

    def __str__(self):
        return self.title

        
        

def all_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(all_pre_save, sender=AboutUs)
pre_save.connect(all_pre_save, sender=Programmes)
pre_save.connect(all_pre_save, sender=Projects)
pre_save.connect(all_pre_save, sender=SuccessStories)
pre_save.connect(all_pre_save, sender=NewsandMedia)
pre_save.connect(all_pre_save, sender=UpcomingEvents)
pre_save.connect(all_pre_save, sender= Publication)
pre_save.connect(all_pre_save, sender= Blog)
pre_save.connect(all_pre_save, sender= Donors)
pre_save.connect(all_pre_save, sender= ImageAlbum)
pre_save.connect(all_pre_save, sender= MembershipContents)
pre_save.connect(all_pre_save, sender= Carrer)