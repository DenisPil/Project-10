from django.contrib import admin

# Register your models here.
from .models import User
from .models import Project
from .models import Contributor
from .models import Issue
from .models import Com


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Com)
