from django.contrib import admin

from apps.users.models import User, MassMedia, Participant, ParticipationSector, Industry, DopParticipant


admin.site.register(User)
admin.site.register(MassMedia)
admin.site.register(Participant)
admin.site.register(ParticipationSector)
admin.site.register(Industry)
admin.site.register(DopParticipant)