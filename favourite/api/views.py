from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .serializers import FavouriteListCreateAPISerializer, FavouriteAPISerializer
from comment.models import Comment
from favourite.api.permissions import IsOwner
from favourite.api.paginations import FavouritePagination
from rest_framework.mixins import UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from favourite.models import Favourite
from rest_framework.permissions import IsAuthenticated

class FavouriteListCreateAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListCreateAPISerializer
    pagination_class = FavouritePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user = self.request.user)

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)


class FavouriteAPIView(RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'pk'
    permission_classes =  [IsOwner]


class FavouriteAllAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

