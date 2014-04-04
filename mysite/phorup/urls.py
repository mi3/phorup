from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('phorup.views',
    
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name='homepage'),    
    
    #url(r'^$', 'list_view', name="blog_index"),
#    url(r'^posts/(?P<post_id>\d+)/$',
#        'detail_view',
#        name="blog_detail"),
#    url(r"^add_comment/(\d+)/$", 
#        "add_comment",
#        name="comment_it"),
#    url(r"^delete_comment/(\d+)/$", 
#        "delete_comment",
#        name="remove_comment"),
#    url(r"^delete_comment/(\d+)/(\d+)/$", 
#        "delete_comment"),
    
    #url(r"^profile/(\d+)/$", "profile"),

)

