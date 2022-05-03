from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pagina_inicial, name ='pagina_inicial'),
    path('pagina_inicial/catalogo/', views.catalogo, name='catalogo'),
    path('pagina_inicial/contato/', views.contato, name='contato'),
    path('pagina_inicial/catalogo/<int:pk>',views.produto_detail_venda, name='produto_detail_venda'),
    path('pagina_inicial/catalogo/<int:pk>/venda',views.venda_pag, name='venda_pag'),
    path('pagina_inicial/catalogo/finalizar',views.finalizar, name='finalizar'),
    path('pagina_inicial/adm/', views.adm, name='adm'),
    path('pagina_inicial/adm/produto_new', views.produto_new, name='produto_new'),
    path('pagina_inicial/adm/lista_edicao', views.lista_edicao, name='lista_edicao'),
    path('pagina_inicial/adm/lista_edicao/<int:pk>', views.produto_detail, name='produto_detail'),
    path('pagina_inicial/adm/lista_edicao/<int:pk>/edit/', views.produto_edit, name='produto_edit'),
       
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)