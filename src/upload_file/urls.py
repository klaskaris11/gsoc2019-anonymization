from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from .views import (document_preview, document_list, document_delete,
                    document_download, delete_anonymized_words, delete_user_dictionary, delete_excluded_words, delete_user_exclusions)
# from filetransfers.api import serve_file

# document app
app_name = 'documents'
urlpatterns = [
    re_path(r'preview/(?P<id>[0-9]+)',
            document_preview, name='document-preview'),
    re_path(r'delete/(?P<id>[0-9]+)',
            document_delete, name='document-delete'),
    re_path(r'download/(?P<id>[0-9]+)',
            document_download, name='document-download'),
    re_path(r'delete_anonymized_words/(?P<id>[0-9]+)',
            delete_anonymized_words, name='document-delete-anonymized-words'),
    re_path(r'delete_excluded_words/(?P<id>[0-9]+)',
            delete_excluded_words, name='document-delete-excluded-words'),
    re_path(r'user_dictionary/delete/(?P<word>.*)',
            delete_user_dictionary, name='document-delete-user-dictionary-words'),
    re_path(r'user_exclude_dictionary/delete/(?P<word>.*)',
            delete_user_exclusions, name='document-delete-user-exclude-dictionary-words'),


    path('list/', document_list, name='document-list')
]
