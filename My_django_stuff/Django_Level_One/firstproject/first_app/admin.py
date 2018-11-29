from django.contrib import admin

# Register your models here.
#snoel - register the model ===========================================
from first_app.models import AccessRecord, Topic, Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

# =====================================================================
