# Google Summer Of Code 2019 :sunny:

### Anonymisation Through Data Encryption of Sensitive Data in ODT and Text Files in Greek Language

## Problem Statement
Over the past year, great importance has been attached to information anonymisation from governments all around the world. The GDPR defines pseudonymization and the processing of personal data in such a way that the data can no longer be attributed to a specific data subject without the use of additional information. Although the GDPR has been implemented since 2018 no reliable infrastructure exists in Greece to encrypt sensitive documents. It is therefore necessary to develop a product specifically for users of the Greek language that can safely and promptly anonymize their data in order for it to abide to the GDPR.

## Abstract
I propose the creation of a LibreOffice extension as well as a web GUI that will anonymize information in any legal document given. All sensitive information should be easily anonymized through this open-source tool. 

On the subject of the creation of the anonymizer I suggest the following metrics. First of all, given any document the anonymizer should encrypt any greek entity in the file from a standard token vocabulary set. The user will be able to add specific arguments for entities to be anonymized (in addition to the standard ones) and he will be given the option to choose for an additional encryption. I believe that the LibreOffice extension as well as the web GUI should be user-friendly so customizable technologies should be used.


## Wiki 
An extended documentation has been written to [wiki pages](https://github.com/eellak/gsoc2019-anonymization/wiki)
in order the service to be understandable and maintainable.


## Technologies used

#### Anonymizer Service
 The anonymizer service uses the following libraries: [argparse](https://docs.python.org/3/library/argparse.html), [json](https://docs.python.org/3/library/json.html), [termcolor](https://pypi.org/project/termcolor/).
#### Web GUI
 The web GUI uses the following libraries: [django](https://www.djangoproject.com/), [bootstrap](https://getbootstrap.com/), [requests](https://pypi.org/project/requests/), [crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html), [django-form-utils](https://pypi.org/project/django-form-utils/).
#### LibreOffice Extension
The libreoffice extension uses the following libraries: [uno](https://wiki.openoffice.org/wiki/Uno), [json](https://docs.python.org/3/library/json.html), [pynput](https://pypi.org/project/pynput/).

## Future work 
- Improvements in user interface.

- Extending Web GUI, so that it can be hosted in VM and serve multiple clients at the same time.

- Creating API.

- Machine learning techniques to identify sensitive information in text.

- Resolving any open issues.


For more information you can visit [future work](https://github.com/eellak/gsoc2019-anonymization/wiki/Future-Work) in wiki pages.

## How to install
1) git clone https://github.com/klaskaris11/gsoc2019-anonymization.git
2) cd gsoc2019-anonymization/
3) Create venv (virtualenv venv)
4) source venv/bin/activate
5) pip install -r requirements.txt
6) python manage.py migrate
7) python manage.py runserver

## Final Report Gist
You can find the final report [here](https://gist.github.com/DimitrisKatsiros/cf6ad8e338a545a74306e0a52d2bfe26).

## Contributors
- Google Summer of Code participant: Dimitrios Katsiros

- Mentor: Kostas Papadimas

- Mentor: Panos Louridas

- Mentor: Iraklis Varlamis

- Organization: [GFOSS](https://gfoss.eu/)
 
## License
This project is open source as a part of the Google Summer of Code Program. Here, the MIT license is adopted. For more information see [LICENSE](https://github.com/eellak/gsoc2019-anonymization/blob/master/LICENSE).
