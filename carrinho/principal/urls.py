from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^end=(?P<idusuario>[-\w ]+)/$', views.fim, name="Fim"),
    url(r'^id=(?P<idusuario>[-\w ]+)/$', views.total, name="Total"),
    url(r'^Produtos/id=(?P<idusuario>[-\w ]+)/$', views.produtos, name="Produtos"),
    url(r'^id=(?P<idusuario>[-\w. ]+)/nome=(?P<nome>[-\w ]+)/$', views.login, name="Login"),
    url(r'^Finalizar/', views.finalizar, name="Finalizar"),
    url(r'^Limpar/', views.limpar, name="Limpar"),
    url(r'^$', views.carrinho, name="Carrinho"),
    url(r'^Adicionar/', views.adiciona, name="Adicionar"),
    url(r'^Remover/', views.remove, name="Remover"),
    url(r'^fila/', views.fila, name="Fila"),
    url(r'^filaPreferencial/', views.filaPref, name="FilaPref"),
    url(r'^id=(?P<idusuario>[-\w ]+)/$', views.produtos, name="Produtos"),
    url(r'^logout/', views.logout, name="Logout"),
    url(r'^mapa', views.mapa, name="mapa"),
]
