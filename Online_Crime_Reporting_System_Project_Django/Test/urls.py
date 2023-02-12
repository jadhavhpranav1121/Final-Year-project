from django.contrib import admin
from django.urls import path, include ,re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from blockchain import views
from django.contrib import admin
#from django.conf.urls import 
from blockchain.views import *  
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('404/', TemplateView.as_view(template_name='404.html'), name='404'),
   
    # Not useful

    # path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    # path('about2/', TemplateView.as_view(template_name='about2.html'), name='about1'),
    # path('comingsoon/', TemplateView.as_view(template_name='coming-soon.html'), name='commingsoon'),

    path('our-team/', TemplateView.as_view(template_name='team-details.html'), name='ourteam'),
    path('community/', TemplateView.as_view(template_name='community.html'), name='community'),
    path('faq/', TemplateView.as_view(template_name='faq.html'), name='faq'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('blogdetail/', TemplateView.as_view(template_name='blog-details.html'), name='blog-details'),
    
    path('admin/', admin.site.urls),
    
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('complaints/', include(('complaints.urls', 'complaints'), namespace='complaints')),
    re_path('^get_chain$', views.get_chain, name="get_chain"),
    re_path('^mine_block$', views.mine_block, name="mine_block"),
    re_path('^add_transaction$', views.add_transaction, name="add_transaction"),
    re_path('^is_valid$', views.is_valid, name="is_valid"),
    re_path('^connect_node$', views.connect_node, name="connect_node"),
    re_path('^replace_chain$', views.replace_chain, name="replace_chain"),
]
handler404 = "accounts.views.page_not_found_view"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
