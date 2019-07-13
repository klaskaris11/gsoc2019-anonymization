import os
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.shortcuts import render
from .models import Document
from django.conf import settings
from os import system as runShell
import subprocess

# from .forms import ModelFormWithFileField
# from .models import ModelWithFileField

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file


def handle_uploaded_file(f, name='temp.txt'):
    script_dir = os.path.dirname(__file__)
    rel_path = "documents/" + name
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            print('valid form')
            uploaded_file = request.FILES['file']
            handle_uploaded_file(
                request.FILES['file'], name=uploaded_file.name)
            # request.session['file'] = request.FILES['file']
            print(uploaded_file.name)
            request.session['file'] = uploaded_file.name
            print(uploaded_file.size)
            return HttpResponseRedirect('/document/preview')
        else:
            print('not valid form')
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})


def document_preview(request):
    print('document_previewed')

    text = ''
    file = os.path.join(os.path.dirname(__file__),
                        'documents/' + request.session['file'])
    directory = os.path.dirname(__file__)
    command = 'cd ' + directory
    runShell(command)
    command = 'cd ..'
    # command = 'cd /home/dimitris/Documents/gsoc2019-anonymization/src'
    runShell(command)
    runShell('pwd')
    command = ('python3 -m anonymizer_service -i upload_file/documents/' +
               request.session['file'])
    runShell(command)

    file_type = request.session['file'][-3:]
    tmp = request.session['file']
    l = len(tmp)
    anonymized_file_name = tmp[0:(l-4)] + '_anonymized' + tmp[(l-4):l]
    anonymized_file = os.path.join(os.path.dirname(__file__),
                                   'documents/' + anonymized_file_name)

    if file_type == 'odt':
        # Convert odt to text just to preview
        # text = ///
        file_error = False
    elif file_type == 'txt':
        with open(file, mode='r') as f:
            text = f.read()
        with open(anonymized_file, mode='r') as f:
            text_anonymized = f.read()

        file_error = False
    else:
        text = 'This file can not be supported.'
        file_error = True

    document = {
        'name': request.session['file'],
        'text': text,
        'type': file_type,
        'error': file_error
    }

    document_anonymized = {
        'name': anonymized_file_name,
        'text': text_anonymized,
        'type': file_type,
        'error': file_error
    }

    context = {
        'document': document,
        'document_anonymized': document_anonymized

    }
    return render(request, 'document_preview.html', context)
