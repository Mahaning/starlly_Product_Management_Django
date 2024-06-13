from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import csv, io

# --------for retrive all data----------
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.active()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'price']
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']

# ---------Create Product------------
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ---------Retrive Single Product------------
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.active()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

# ---------Update Product------------
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.active()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


# ---------Hard Delete Product------------(it will delete actual(physical) product data from db)
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # Hard delete
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------Soft Delete Product------------(it will  marks a record as no longer active or valid without actually deleting it from the database )
class ProductSoftDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

# # ---------Upload CSV File Of  Products------------
class UploadCSVView(APIView):
    def get(self, request):
        return render(request, 'upload_csv.html')

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']
        if not file.name.endswith('.csv'):
            return Response({"error": "File is not a CSV"}, status=status.HTTP_400_BAD_REQUEST)

        data_set = file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # Skip the header row

        for row in csv.reader(io_string, delimiter=','):
            _, created = Product.objects.update_or_create(
                name=row[0],
                defaults={
                    'description': row[1],
                    'price': row[2],
                }
            )

        return Response({"success": "CSV file has been uploaded and processed"})

#---------Filter Product by name ------------

class ProductListByNameAPIView(generics.ListAPIView):
    queryset = Product.objects.active()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']  # Ensure 'name' is included as a filterset field
    search_fields = ['name']  # Ensure 'name' is included as a search field
    ordering_fields = ['price', 'created_at']

#---------Filter Product by Price Range ------------
class ProductListByPriceRangeAPIView(generics.ListAPIView):
    queryset = Product.objects.active()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def get_queryset(self):
        queryset = self.queryset

        # Handle price range filtering
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset
    

# --------it is for bot filter and fetch all filtered data by name and price range(min and max)
class ProductListByNameAndPriceRangeAPIView(generics.ListAPIView):
    queryset = Product.objects.active()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']  # Ensure 'name' is included as a filterset field
    search_fields = ['name']  # Ensure 'name' is included as a search field
    ordering_fields = ['price', 'created_at']

    def get_queryset(self):
        queryset = self.queryset

        # Parse query parameters
        name = self.request.query_params.get('name')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        # Apply filters based on parameters
        if name:
            queryset = queryset.filter(name__icontains=name)

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)

        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset
