from django.apps import AppConfig
from sklearn.externals import joblib
import os
from django.conf import settings

class PredConfig(AppConfig):
    name = 'pred'
    path1 = os.path.join(settings.MODELS, 'restrevclass.mdl')
    path2 = os.path.join(settings.MODELS, 'restrevcv.mdl')

    classifier = joblib.load(path1)
    countvec = joblib.load(path2)