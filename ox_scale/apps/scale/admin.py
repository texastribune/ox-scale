from __future__ import unicode_literals

from django.contrib import admin

from . import models
from .utils import import_from_csv


class QuestionInline(admin.TabularInline):
    extra = 0
    model = models.Question
    readonly_fields = ('question', 'choices', 'impressions', 'clicks', )


class QuestionSetAdmin(admin.ModelAdmin):
    inlines = (QuestionInline, )
    list_display = ('__unicode__', 'created_at', 'uuid', )
    readonly_fields = ('owner', 'question_count', )

    def get_queryset(self, request):
        qs = super(QuestionSetAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        """Save the file while throwing away the file."""
        csv_file = form.files['input_file']
        if not obj.name:
            obj.name = unicode(csv_file)
        obj.input_file = None  # we don't actually want the input file
        obj.owner = request.user
        obj.save()
        csv_file.seek(0)  # reset file pointer, not sure why I have to do this.
        import_from_csv(obj, csv_file)
        obj.question_count = obj.questions.count()
        obj.save()
admin.site.register(models.QuestionSet, QuestionSetAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'set', 'impressions', 'clicks', )
    readonly_fields = ('set', 'choices', 'impressions', 'clicks', )
    search_fields = ('question', )

    def get_queryset(self, request):
        qs = super(QuestionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(set__owner=request.user)
admin.site.register(models.Question, QuestionAdmin)
