from pyclist.admin import BaseModelAdmin, admin_register
from ranking.models import Account, Rating, Statistics, Module
from ranking.management.commands.parse_statistic import Command as parse_stat
from clist.models import Contest


@admin_register(Account)
class AccountAdmin(BaseModelAdmin):
    list_display = ['resource', 'key', '_num_coders']
    search_fields = ['key']
    list_filter = ['resource__host']

    def _num_coders(self, obj):
        return obj.coders.count()


@admin_register(Rating)
class RatingAdmin(BaseModelAdmin):
    list_display = ['contest', 'party']
    search_fields = ['contest__title', 'party__name']
    list_filter = ['party__name', 'contest__host']

    def parse_statistic(self, request, queryset):
        ids = queryset.values_list('contest', flat=True).distinct()
        contests = Contest.objects.filter(id__in=ids)
        count, total = parse_stat().parse_statistic(contests=contests, with_check=False)
        self.message_user(request, "%d of %d parsed." % (count, total))
    parse_statistic.short_description = 'Parse statistic'

    actions = [parse_statistic]


@admin_register(Statistics)
class StatisticsAdmin(BaseModelAdmin):
    list_display = ['account', 'contest', 'place', 'solving', 'upsolving']
    search_fields = ['account__key', 'contest__title']
    list_filter = ['contest__host']
    raw_id_fields = ['account', 'contest']


@admin_register(Module)
class ModuleAdmin(BaseModelAdmin):
    list_display = ['resource',
                    'min_delay_after_end',
                    'max_delay_after_end',
                    'delay_on_error',
                    'delay_on_success',
                    'path']
    search_fields = ['resource__host']
