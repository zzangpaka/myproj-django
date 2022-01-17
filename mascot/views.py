import json

from django.http import HttpResponse
from rest_framework import viewsets
from mascot.serializers import CharacterSerializer
from mascot.models import Character


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


def character_list(request):
    qs = Character.objects.all()
    data = [
        {
            "id": character.id,
            "region": character.region,
            "city": character.city,
            "charming": character.charming,
            "name": character.name,
            "explain": character.explain,
            "photo": character.photo,
        }
        for character in qs
    ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)