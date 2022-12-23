from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from audio_app.views import *
from .views import create_account, log_in

urlpatterns = [
    path("", index_render, name="index"), #Instruction  + Disclaimer
    path("register/", create_account, name="register"),
    path("login/", log_in, name="login"),
    path('', include("django.contrib.auth.urls")), ## logout url
    path("listen/", listen, name="listen"),
    path("listen/<str:category>", listen_category, name="listen_category"),
    path("upload/", file_upload, name="upload"),
    path("delete_file/<int:file_id>", file_delete, name="delete"),
    path("admin/", admin.site.urls),
    path("about/", about_render, name="about"),
    path("background/", background_render, name="background"),
    path("sponsors/", sponsors_render, name="sponsors"),
    path("instructions/", instructions_render, name="instructions"),
    path("disclaimer/", disclaimer_render, name="disclaimer"),
    path("chatbot/", chatbot_render, name="chatbot"),
    path("createPlaylist/", createPlaylist, name="createPlaylist"),
    path("deletePlaylist/<int:playlistId>", deletePlaylist, name="deletePlaylist"),
    path("listen/playlist/<int:playlistId>", listenPlaylist, name="listenPlaylist"),
    path("addToPlaylist/<int:fileId>/<str:fileName>", addToPlaylist, name="addToPlaylist"),
    path("removeFromPlaylist/<int:playlistId>/<int:fileId>", removeFromPlaylist, name="removeFromPlaylist"),
]

# Only add this when we in debug mode and do not have nginx to serve these items
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)