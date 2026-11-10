# path: función para declarar una ruta URL y a qué vista apunta
from django.urls import path
# views: el módulo con todas las funciones-vista de esta app
from . import views

# urlpatterns: la lista de rutas que Django revisa, en orden, para cada URL
urlpatterns = [
    # '': la página de inicio de la Semana 3; no la borres
    path('', views.inicio, name='inicio'),
    # /servicios/: listado (Semana 3), ahora filtrado por usuario
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
    path('facturas/', views.facturas, name='facturas'),
    path('facturas/nueva/', views.crear_factura, name='crear_factura'),
    path('facturas/<int:pk>/', views.detalle_factura, name='detalle_factura'),
    path('reportes/', views.reportes, name='reportes'),
    path('reportes/<slug:clave>/', views.reporte, name='reporte'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),

]
