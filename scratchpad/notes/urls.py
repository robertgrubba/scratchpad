from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from notes import views
#from ingredient.views import IngredientListView

app_name='notes'

urlpatterns = [
        path('', views.CategoryListView.as_view(), name='categories'),
        path('/category/create', views.CategoryCreateView.as_view(), name='category_create'),
        path('/category/<slug:slug>', views.CategoryDetailView.as_view(), name='category'),
        path('/topic/new', views.TopicCreateView.as_view(), name='topic_create'),
        path('/topic/<slug:slug>', views.TopicDetailView.as_view(), name='topic'),
        path('/note/new', views.NoteCreateView.as_view(), name='note_create'),
        path('/note/update/<int:pk>', views.NoteUpdateView.as_view(), name='note_update'),
        path('/note/delete/<int:pk>', views.NoteDeleteView.as_view(), name='note_delete'),
        path('/attachement/add/<int:id>', views.AttachementCreateView.as_view(), name='attachement_create'),
        ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


