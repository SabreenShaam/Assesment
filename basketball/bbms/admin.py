from django.apps import apps
from django.contrib import admin

apps_config = apps.get_app_config('bbms')
models = apps_config.get_models()

for model in models:
    admin.site.register(model)
