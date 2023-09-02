from rest_framework import serializers

from staff.models import Staff, Picture ,Categoty



class PictureModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Picture

class CategotyModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Categoty

class StaffModelSerializer(serializers.ModelSerializer):
    pictures = PictureModelSerializer(many=True,required=False)
    categoty = CategotyModelSerializer(required=False)
    class Meta:
        fields = [
            'id',
            'name',
            'price',
            'description',
            'categoty',
            'pictures',
        ]
        model = Staff

