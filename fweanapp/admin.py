from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Organization)
admin.site.register(Programmes)
admin.site.register(AboutUs)
admin.site.register(Slider)
admin.site.register(Subscriber)
admin.site.register(FooterImportantLinks)
admin.site.register(Videos)
admin.site.register(BoardMembers)
admin.site.register(BoardImmediatePastPresident)
admin.site.register(BoardVicePresidents)
admin.site.register(BoardExecutiveMembers)
admin.site.register(SuccessStories)
admin.site.register(SocialMediaNewsFeeds)
admin.site.register(NewsandMedia)
admin.site.register(Blog)
# admin.site.register(BlogComments)
admin.site.register(Projects )
admin.site.register(Feedbacks)
admin.site.register(UpcomingEvents)
admin.site.register(Publication)
admin.site.register(Membership)
admin.site.register(MembershipContents)
admin.site.register(OfficeTime)

class ImagemediaInline(admin.TabularInline):
    model = ImageMedia
    extra = 5

class ImageAlbumAdmin(admin.ModelAdmin):
    inlines = [ ImagemediaInline, ]


admin.site.register(ImageAlbum,ImageAlbumAdmin)