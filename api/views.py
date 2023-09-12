from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Chiste
from .serializers import ChisteSerializer
from rest_framework import viewsets
from requests import get

class ChisteViwset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin , mixins.DestroyModelMixin, viewsets.GenericViewSet):

    serializer_class = ChisteSerializer
    queryset = Chiste.objects.all()
        
    def list(self, request, *args, **kwargs):
        chuck = self.request.query_params.get('chuck', None)
        if chuck is not None:
            response = get('https://api.chucknorris.io/jokes/random')
            data = response.json()
            return Response({'id':0,'texto': data['value']})
        else:
            chiste = Chiste.objects.order_by('?').first()
            serializer = self.serializer_class(chiste)
            return Response(serializer.data)
        
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"message":"Chiste creado correctamente"}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({"message":"Chiste editado correctamente"})


    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message":"Chiste eliminado correctamente"})