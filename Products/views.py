from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from Products.models import Products
from Products.serializers import ProductsSerializer


# Create your views here.
class ProductsView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsDetailsView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsSearchView(ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        if query:
            queryset = Products.objects.filter(name__icontains=query)
        else:
            queryset = Products.objects.all()
            return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
