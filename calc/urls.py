from django.urls import path
from . import views


app_name='calc'
urlpatterns=[
    path('sum/',views.SumView.as_view(),name='sum'),
    path('history/',views.HistoryView.as_view(),name='history'),
    path('total/',views.TotalView.as_view(),name='total')
]