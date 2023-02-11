from django.contrib import admin
from django.urls import path, include ,re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from blockchain import views
from django.contrib import admin
#from django.conf.urls import 
from blockchain.views import *  

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
