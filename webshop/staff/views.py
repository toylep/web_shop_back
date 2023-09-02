from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView
from rest_framework.views import APIView
from staff.models import Staff,Categoty , Picture
from staff.serializers import  StaffModelSerializer,CategotyModelSerializer, PictureModelSerializer
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class StaffListView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffModelSerializer
    
class StaffAddView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Staff.objects.all()
    serializer_class = StaffModelSerializer
    permission_classes = [IsAuthenticated]

class StaffSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffModelSerializer
    permission_classes = [IsAuthenticated]


class ImageAdd(CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureModelSerializer
    permission_classes = [IsAuthenticated]

class ImageDelete(RetrieveDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureModelSerializer
    permission_classes = [IsAuthenticated]


class CategoryListView(ListAPIView):
    queryset = Categoty.objects.all()
    serializer_class = CategotyModelSerializer
    permission_classes = [IsAuthenticated]
 

class ImageLoader(APIView):
    """Класс для выгрузки фото на фронт
    """
    def get(self,request,filename):
        return FileResponse(open(f'./files/images/{filename}','rb'))

def birthday():
    return render('birth.html')