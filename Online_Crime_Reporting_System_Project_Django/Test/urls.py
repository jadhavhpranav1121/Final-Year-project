from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from blockchain import views
from django.contrib import admin
from django.conf.urls import url
from blockchain.views import *  

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('complaints/', include(('complaints.urls', 'complaints'), namespace='complaints')),
    # path('blockchain/', include(('blockchain.urls', 'blockchain'), namespace='blockchain')),
     url('^get_chain$', views.get_chain, name="get_chain"),
    url('^mine_block$', views.mine_block, name="mine_block"),
    url('^add_transaction$', views.add_transaction, name="add_transaction"),
    url('^is_valid$', views.is_valid, name="is_valid"),
    url('^connect_node$', views.connect_node, name="connect_node"),
    url('^replace_chain$', views.replace_chain, name="replace_chain"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)