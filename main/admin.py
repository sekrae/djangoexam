from django.contrib import admin
from .models import Worker, Document, Project, Membership, Customer, VIPClient
from datetime import date
from .forms import WorkerForm




@admin.display(description='experience_year')
def get_work_year(obj):
    work_year = date.today().year - obj.worker.year
    return work_year

def get_link(obj): 
    return "Подробнее"

class WorkerAdmin(admin.ModelAdmin):
    form = WorkerForm
    list_display = ('fullname', 'work_position', get_work_year, get_link)
    search_fields = ('name',)
    list_display_links = (get_link,)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('get_fullname', 'inn', 'card_id')

    @admin.display(description='fullname')
    def get_fullname(self, obj):
        return obj.worker.fullname



admin.site.register(Worker, WorkerAdmin)
admin.site.register(Document, DocumentAdmin)