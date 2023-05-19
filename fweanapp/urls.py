from django.urls import path

from .views import *
from django.conf.urls import handler404
handler404 = error_404_view
from froala_editor import views
app_name = "fweanapp"

urlpatterns = [


path('admin-site/login/', AdminLoginView.as_view(), name = 'adminlogin'),
path('fwean-admin/profile-<int:pk>/',AdminProfileView.as_view(), name="adminprofile"),
path('fwean-admin/<int:pk>/update/', AdminProfileUpdateView.as_view(), name = 'adminprofileupdate'),
path('fwean-admin/changepassword/',AdminPasswordUpdateView.as_view(), name="adminpasswordchange"),
path('logout/', AdminLogoutView.as_view(), name="adminlogout"),
path('admin-dashboard/',AdminDashboardView.as_view(), name = 'admindashboard'),


path('admin/organization/create/', AdminOrganizationCreateView.as_view(), name = 'adminorganizationcreate'),
path('admin/organization/update/<int:pk>/', AdminOrganizationUpdateView.as_view(), name = 'adminorganizationupdate'),
path('admin/organization/detail/<int:pk>/', AdminOrganizationDetailView.as_view(), name = 'adminorganizationdetail'),


path('admin/image-album/add/', ImageAlbumAddView.as_view(), name = 'imagealbumadd'),
path('admin/imagealbum/list/', ImageAlbumListView.as_view(), name = 'imagealbumlist'),
path('admin/imagealbum/<int:pk>/detail/', ImageAlbumDetailView.as_view(), name = 'adminimagealbumdetail'),
path('admin/imagealbum/<int:pk>/update/', ImageAlbumUpdateView.as_view(), name = 'adminimagealbumupdate'),
path('admin/imagealbum/<int:pk>/delete/', ImageAlbumDeleteView.as_view(), name = 'adminimagealbumdelete'),


path('admin/imagemedia/<int:pk>/delete/', ImageMediaDeleteView.as_view(), name = 'adminimagemediadelete'),


path('admin/image-slider/add/', SliderCreateView.as_view(), name = 'adminislidercreate'),
path('admin/image-slider/list/', SliderListView.as_view(), name = 'adminsliderlist'),
path('admin/image-slider/<int:pk>/detail/', SliderDetailView.as_view(), name = 'adminsliderdetail'),
path('admin/image-slider/<int:pk>/update/', AdminSliderUpdateView.as_view(), name = 'adminsliderupdate'),
path('admin/image-slider/<int:pk>/delete/', AdminSliderDeleteView.as_view(), name = 'adminsliderdelete'),




path('admin/aboutus/add/', AdminAboutUsCreateView.as_view(), name = 'adminaboutuscreate'),
path('admin/aboutus/list/', AdminAboutUsListView.as_view(), name = 'adminaboutuslist'),
path('admin/aboutus/<int:pk>/detail/', AdminAboutUsDetailView.as_view(), name = 'adminaboutusdetail'),
path('admin/aboutus/<int:pk>/update/', AdminAboutUsUpdateView.as_view(), name = 'adminaboutusupdate'),
path('admin/aboutus/<int:pk>/delete/', AdminAboutUsDeleteView.as_view(), name = 'adminaboutusdelete'),

#projects
path('admin/project/add/', AdminProjectsCreateView.as_view(), name = 'adminprojectcreate'),
path('admin/project/list/', AdminProjectsListView.as_view(), name = 'adminprojectlist'),
path('admin/project/<int:pk>/detail/', AdminProjectsDetailView.as_view(), name = 'adminprojectdetail'),
path('admin/project/<int:pk>/update/', AdminProjectsUpdateView.as_view(), name = 'adminprojectupdate'),
path('admin/project/<int:pk>/delete/', AdminProjectsDeleteView.as_view(), name = 'adminprojectdelete'),

#programmes
path('admin/programmes/add/', AdminProgrammesCreateView.as_view(), name = 'adminprogrammecreate'),
path('admin/programmes/list/', AdminProgrammesListView.as_view(), name = 'adminprogrammelist'),
path('admin/programmes/<int:pk>/detail/', AdminProgrammesDetailView.as_view(), name = 'adminprogrammedetail'),
path('admin/programmes/<int:pk>/update/', AdminProgrammesUpdateView.as_view(), name = 'adminprogrammeupdate'),
path('admin/programmes/<int:pk>/delete/', AdminProgrammesDeleteView.as_view(), name = 'adminprogrammedelete'),

#successstories
path('admin/success-stories/add/', AdminSuccessStoriesCreateView.as_view(), name = 'adminsuccessstoriescreate'),
path('admin/success-stories/list/', AdminSuccessStoriesListView.as_view(), name = 'adminsuccessstorieslist'),
path('admin/success-stories/<int:pk>/detail/', AdminSuccessStoriesDetailView.as_view(), name = 'adminsuccessstoriesdetail'),
path('admin/success-stories/<int:pk>/update/', AdminSuccessStoriesUpdateView.as_view(), name = 'adminsuccessstoriesupdate'),
path('admin/success-stories/<int:pk>/delete/', AdminSuccessStoriesDeleteView.as_view(), name = 'adminsuccessstoriesdelete'),

#Subscriber

path('admin/subscribers/', AdminSubscribersListView.as_view(), name = 'adminsubscriberlist'),
path('admin/subscriber/<int:pk>/delete/', AdminSubscriberDeleteView.as_view(), name = 'adminsubscriberdelete'),
path('admin/subscriber/<int:pk>/update/', AdminSubscriberUpdateView.as_view(), name = 'adminsubscriberupdate'),

#Blog
path('admin/blog/add/', AdminBlogCreateView.as_view(), name = 'adminblogcreate'),
path('admin/blog/list/', AdminBlogListView.as_view(), name = 'adminbloglist'),
path('admin/blog/<int:pk>/detail/', AdminBlogDetailView.as_view(), name = 'adminblogdetail'),
path('admin/blog/<int:pk>/update/', AdminBlogUpdateView.as_view(), name = 'adminblogupdate'),
path('admin/blog/<int:pk>/delete/', AdminBlogDeleteView.as_view(), name = 'adminblogdelete'),


#Donors
path('admin/donor/add/', AdminDonorsCreateView.as_view(), name = 'admindonorcreate'),
path('admin/donor/list/', AdminDonorsListView.as_view(), name = 'admindonorlist'),
path('admin/donor/<int:pk>/detail/', AdminDonorsDetailView.as_view(), name = 'admindonordetail'),
path('admin/donor/<int:pk>/update/', AdminDonorsUpdateView.as_view(), name = 'admindonorupdate'),
path('admin/donor/<int:pk>/delete/', AdminDonorsDeleteView.as_view(), name = 'admindonordelete'),

#Faq
path('admin/faq/add/', AdminFAQCreateView.as_view(), name = 'adminfaqcreate'),
path('admin/faq/list/', AdminFAQListView.as_view(), name = 'adminfaqlist'),
path('admin/faq/<int:pk>/detail/', AdminFAQDetailView.as_view(), name = 'adminfaqdetail'),
path('admin/faq/<int:pk>/update/', AdminFAQUpdateView.as_view(), name = 'adminfaqupdate'),
path('admin/faq/<int:pk>/delete/', AdminFAQDeleteView.as_view(), name = 'adminfaqdelete'),

#Important Links

#Faq
path('admin/important-links/add/', AdminImportantLinksCreateView.as_view(), name = 'adminimportantlinkscreate'),
path('admin/important-links/list/', AdminImportantLinksListView.as_view(), name = 'adminimportantlinkslist'),
# path('admin/important-links/<int:pk>/detail/', AdminImportantLinksDetailView.as_view(), name = 'adminfaqdetail'),
path('admin/important-links/<int:pk>/update/', AdminImportantLinksUpdateView.as_view(), name = 'adminimportantlinksupdate'),
path('admin/important-links/<int:pk>/delete/', AdminImportantLinksDeleteView.as_view(), name = 'adminimportantlinksdelete'),



#Upcoming Events
path('admin/upcoming-event/add/', AdminUpcomingEventsCreateView.as_view(), name = 'adminupcomingeventcreate'),
path('admin/upcoming-event/list/', AdminUpcomingEventsListView.as_view(), name = 'adminupcomingeventlist'),
path('admin/upcoming-event/<int:pk>/detail/', AdminUpcomingEventsDetailView.as_view(), name = 'adminupcomingeventdetail'),
path('admin/upcoming-event/<int:pk>/update/', AdminUpcomingEventsUpdateView.as_view(), name = 'adminupcomingeventupdate'),
path('admin/upcoming-event/<int:pk>/delete/', AdminUpcomingEventsDeleteView.as_view(), name = 'adminupcomingeventdelete'),


#News and Media
path('admin/news/add/', AdminNewsandMediaCreateView.as_view(), name = 'adminnewscreate'),
path('admin/news/list/', AdminNewsandMediaListView.as_view(), name = 'adminnewslist'),
path('admin/news/<int:pk>/detail/', AdminNewsandMediaDetailView.as_view(), name = 'adminnewsdetail'),
path('admin/news/<int:pk>/update/', AdminNewsandMediaUpdateView.as_view(), name = 'adminnewsupdate'),
path('admin/news/<int:pk>/delete/', AdminNewsandMediaDeleteView.as_view(), name = 'adminnewsdelete'),



#SocialMedia NewsFeeds
path('admin/socialmedia-newsfeed/add/', AdminSocialMediaNewsCreateView.as_view(), name = 'adminsocialmedia-newsfeedcreate'),
path('admin/socialmedia-newsfeed/list/', AdminSocialMediaNewsListView.as_view(), name = 'adminsocialmedia-newsfeedlist'),
path('admin/socialmedia-newsfeed/<int:pk>/detail/', AdminSocialMediaNewsDetailView.as_view(), name = 'adminsocialmedia-newsfeeddetail'),
path('admin/socialmedia-newsfeed/<int:pk>/update/', AdminSocialMediaNewsUpdateView.as_view(), name = 'adminsocialmedia-newsfeedupdate'),
path('admin/socialmedia-newsfeed/<int:pk>/delete/', AdminSocialMediaNewsDeleteView.as_view(), name = 'adminsocialmedia-newsfeeddelete'),


#Admin Videos
path('admin/videos/add/', AdminVideosCreateView.as_view(), name = 'adminvideocreate'),
path('admin/videos/list/', AdminVideosListView.as_view(), name = 'adminvideolist'),
path('admin/videos/<int:pk>/detail/', AdminVideosDetailView.as_view(), name = 'adminvideodetail'),
path('admin/videos/<int:pk>/update/', AdminVideosUpdateView.as_view(), name = 'adminvideoupdate'),
path('admin/videos/<int:pk>/delete/', AdminVideosDeleteView.as_view(), name = 'adminvideodelete'),


#BoardMembers
path('admin/board-members/add/', AdminBoardMembersAddView.as_view(), name = 'boardmembersadd'),
path('admin/board-members/', AdminBoardMembersListView.as_view(), name = 'adminboardmemberlist'),
path('admin/board-members/<int:pk>/detail/', AdminVideosDetailView.as_view(), name = 'adminboardmembersdetail'),
path('admin/board-members/<int:pk>/update/', AdminBoardMembersUpdateView.as_view(), name = 'adminboardmembersupdate'),
path('admin/board-members/<int:pk>/delete/', AdminVideosDeleteView.as_view(), name = 'aadminvideodelete'),


#Vice Presidents
path('admin/vice-president/add/', BoardVicePresidentsAddView.as_view(), name = 'adminboardvicepresidentadd'),
path('admin/vice-president/list/', BoardVicePresidentslistView.as_view(), name = 'adminboardvicepresidentlist'),
# path('admin/board-members/<int:pk>/detail/', AdminVideosDetailView.as_view(), name = 'adminboardmembersdetail'),
path('admin/vice-president/<int:pk>/update/', BoardVicePresidentsUpdateView.as_view(), name = 'adminvicepresidentupdate'),
path('admin/vice-president/<int:pk>/delete/', BoardVicePresidentsDeleteView.as_view(), name = 'adminvicepresidentdelete'),

#Executive Members
path('admin/executive-members/add/', BoardExecutiveMembersAddView.as_view(), name = 'adminexecutivemembersadd'),
path('admin/executive-members/list/', BoardExecutiveMemberslistView.as_view(), name = 'adminexecutivememberlist'),
# path('admin/board-members/<int:pk>/detail/', AdminVideosDetailView.as_view(), name = 'adminboardmembersdetail'),
path('admin/executive-members/<int:pk>/update/', BoardExecutiveMembersUpdateView.as_view(), name = 'adminexecutivemembersupdate'),
path('admin/executive-members/<int:pk>/delete/', BoardExecutiveMembersDeleteView.as_view(), name = 'adminexecutivemembersdelete'),

#Immediate Past President
path('admin/past-president/add/', BoardImmediatePastPresidentsAddView.as_view(), name = 'adminimmediatepastpresidentadd'),
path('admin/past-president/list/', BoardImmediatePastPresidentlistView.as_view(), name = 'adminimmediatepastpresidentlist'),
# path('admin/board-members/<int:pk>/detail/', AdminVideosDetailView.as_view(), name = 'adminboardmembersdetail'),
path('admin/past-president/<int:pk>/update/', BoardImmediatePastPresidentsUpdateView.as_view(), name = 'adminimmediatepastpresidentupdate'),
path('admin/past-president/<int:pk>/delete/', BoardImmediatePastPresidentDeleteView.as_view(), name = 'adminimmediatepastpresidentdelete'),


# path('toggle', BoardImmediatePastPresidentDeleteView.as_view(), name = 'adminimmediatepastpresidentdelete'),

#Admin FeedBacks
path('admin/feedbacks/',AdminFeedbacksListView.as_view(),name='adminfeedbackslist'),
path('admin/feedbacks/<int:pk>/detail/',AdminFeedbacksDetailView.as_view(),name='adminfeedbacksdetail'),
path('admin/feedbacks/<int:pk>/delete/',AdminFeedbacksDeleteView.as_view(),name='adminfeedbackdelete'),

# Admin Publications
path('admin/publications/add/', AdminPublicationCreateView.as_view(), name = 'adminpublicationadd'),
path('admin/publications/', AdminPublicationListView.as_view(), name = 'adminpublicationlist'),
path('admin/publications/<int:pk>/detail/', AdminPublicationDetailView.as_view(), name = 'adminpublicationdetail'),
path('admin/publications/<int:pk>/update/', AdminPublicationUpdateView.as_view(), name = 'adminpublicationsupdate'),
path('admin/publications/<int:pk>/delete/', AdminPublicationDeleteView.as_view(), name = 'adminpublicationdelete'),

#Blog Comments

path('admin/blog-comments/', AdminBlogCommentListView.as_view(), name = 'adminblogcommentslist'),
path('admin/blog-comments/update/<int:pk>/', AdminBlogCommentUpdate.as_view(), name = 'adminblogcommentupdate'),
path('admin/blog-comments-delete/<int:pk>/delete/', AdminBlogCommentDeleteView.as_view(), name = 'adminblogcommentdelete'),

#Membership Contents Add

path('admin/membership-contents/add/',AdminMembershipContentsCreateView.as_view(),name= 'adminmembershipcontentscreate'),
path('admin/membership-contents/',AdminMembershipContentsListView.as_view(),name= 'adminmembershipcontentlist'),
path('admin/membership-contents/detail/<int:pk>/',AdminMembershipContentsDetailView.as_view(),name= 'adminmembershipcontentdetail'),
path('admin/membership-contents/update/<int:pk>/',AdminMembershipContentsUpdateView.as_view(),name= 'adminmembershipcontentupdate'),
path('admin/membership-contents/dalete/<int:pk>/',AdminMembershipContentsDeleteView.as_view(),name= 'adminmembershipcontentdelete'),



#Admin Membership

path('admin/blog-comments/', AdminBlogCommentListView.as_view(), name = 'adminblogcommentslist'),
path('admin/blog-comments/update/<int:pk>/', AdminBlogCommentUpdate.as_view(), name = 'adminblogcommentupdate'),
path('admin/blog-comments-delete/<int:pk>/delete/', AdminBlogCommentDeleteView.as_view(), name = 'adminblogcommentdelete'),


path('admin/membership-form/', AdminMembershipFormListView.as_view(), name = 'adminmembershipformlist'),

path('admin/membership-form/<int:pk>/detail/', AdminMembershipFormDetailView.as_view(), name = 'adminmembershipfromdetail'),
path('admin/membership-form/<int:pk>/documents/', AdminMembershipFormDocumentsDetailView.as_view(), name = 'adminmembershipdocumentsdetail'),
path('admin/membership-form/<int:pk>/delete/', AdminMembershipFormDeleteView.as_view(), name = 'adminmembershipformdelete'),





#Admin Email Recipent
path('admin/email-recipent/add/', AdminEmailRecipentCreateView.as_view(), name = 'adminemailrecipentcreate'),
path('admin/email-recipent/list/', AdminEmailRecipentListView.as_view(), name = 'adminemailrecipentlist'),
path('admin/email-recipent/<int:pk>/detail/', AdminEmailRecipentDetailView.as_view(), name = 'adminemailrecipentdetail'),
path('admin/email-recipent/<int:pk>/update/', AdminEmailRecipentUpdateView.as_view(), name = 'adminemailrecipentupdate'),
path('admin/email-recipent/<int:pk>/delete/', AdminEmailRecipentDeleteView.as_view(), name = 'adminemailrecipentdelete'),
path('admin/office-time/add/', AdminOfficeTimeAddView.as_view(), name = 'adminofficetimeadd'),
path('admin/office-time/list/', AdminOfficeTimeListView.as_view(), name = 'adminofficetimelist'),
path('admin/office-time/update/<int:pk>/', AdminOfficeTimeUpdateView.as_view(), name = 'adminofficetimeupdate'),
path('admin/office-time/<int:pk>/delete/', AdminOfficeTimeDeleteView.as_view(), name = 'adminofficetimedelete'),






#CLient Urls
path('',ClientIndexView.as_view(), name = 'indexpage' ),
path('contact-us/',ClientContactUsView.as_view(), name = 'clientcontactus'),


path('about-us/<slug:slug>/',ClientAboutUsView.as_view(), name = 'clientaboutus'),
# path('about-us/<int:pk>/',ClientAboutUsListView.as_view(), name = 'clientaboutus'),
path('about-us/<slug:slug>/detail',ClientAboutUsDetailView.as_view(), name = 'clientaboutusdetail'),
path('news-and-events/',ClientNewsandEventsListView.as_view(), name = 'clientnewsandeventslist'),
path('news-and-events/<slug:slug>/detail/',ClientNewsandEventsDetailView.as_view(), name = 'clientnewsandeventsdetail'),

#Upcoming
path('upcoming-events/',ClientUpcomingEventsListView.as_view(), name = 'clientupcomingeventlist'),
path('upcoming-events/<slug:slug>/',ClientUpcomingEventsDetailView.as_view(), name = 'clientupcomingeventdetail'),

#Programmes
path('programmes/',ClientProgrammeListView.as_view(), name = 'clientprogrammes'),
path('program/<slug:slug>/detail/',ClientProgrammeDetailView.as_view(), name = 'clientprogrammedetail'),

#Subscriber
path('subscribe/', SubscribeCreateView.as_view(), name = 'subscribercreate'),

#image album
path('image-albums/',ClientImageAlbumListView.as_view(),name= 'clientimagealbumlist'),
path('image-gallery/<slug:slug>/',ClientImageGalleryView.as_view(),name= 'clientimagegallery'),


path('faqs/',ClientFaqView.as_view(),name= 'clientfaq'),

path('project-partners/',ClientProjectsPartnersListView.as_view(),name= 'clientprojectpartners'),
path('project/list/<slug:slug>/',ClientProjectsListView.as_view(),name= 'clientprojectlist'),
path('ongoing-projects/',ClientOngoingProjectsListView.as_view(),name= 'clientongoingprojectlist'),
path('accomplished-projects/',ClientAccomplishedProjectsListView.as_view(),name= 'clientaccomplishedprojectlist'),
path('project-detail/<slug:slug>/',ClientProjectDetailView.as_view(),name= 'clientprojectdetail'),


#Video gallery
path('videos/',ClientVideoGalleryListView.as_view(),name= 'clientvideogallery'),

path('success-stories/',ClientSuccessStoriesListView.as_view(),name= 'clientsuccessstorieslist'),
path('success-stories/<slug:slug>/',ClientSuccessStoriesDetailView.as_view(),name= 'clientsuccessstoriesdetail'),


path('donors/',ClientDonorListView.as_view(),name= 'clientdonorlist'),
path('donor/<slug:slug>/',ClientDonorDetailView.as_view(),name= 'clientdonordetail'),

path('board-members/',ClientBoardMembersView.as_view(),name= 'clientboardmembers'),


path('blogs/',ClientBlogListView.as_view(),name= 'clientbloglist'),
path('blog/<slug:slug>/',ClientBlogDetailView.as_view(),name= 'clientblogdetail'),
path('blog/comment/<slug:slug>/',ClientBlogCommentCreateView.as_view(),name= 'clientblogcomment'),
path('feedbacks/',ClientFeedbackView.as_view(),name= 'clientfeedbacks'),
path('publications/',ClientPublicationView.as_view(),name= 'clientpublication'),
path('publications/<slug:slug>/',ClientPublicationDetailView.as_view(),name= 'clientpublicationdetail'),
path('introduction/',ClientIntroductionView.as_view(),name= 'clientintroduction'),
path('geographical-coverage/',GeographicalCoverageView.as_view(),name= 'geographicalcoverage'),
# path('membership-form/',ClientMembershipFormView.as_view(),name= 'membershipform'),
# path('search/',SearchView.as_view(),name= 'search'),
path('membership/<slug:slug>/',ClientMembershipContentsView.as_view(),name= 'clientmembershipcontentsview'),

path('publication-downloaded/<slug:slug>/',ClientPublicationDownloadCounter.as_view(),name= 'publicationcounter'),
# path('membership-form/',ClientMembershipFormView.as_view(),name= 'membershipform'),

]
