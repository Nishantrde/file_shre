from rest_framework import serializers
from .models import *
import shutil

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

class FileList(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=100000000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required = False)

    def zip_files(self, folder):
        shutil.make_archive(f'public/static/zip/{folder}', 'zip', f'public/static/{folder}')

    def create(self, validate_data):
        folder = Folder.objects.create()
        files = validate_data.pop('files')
        file_objs = []
        for file in files:
            file_obj = Files.objects.create(folder = folder, file = file)
            file_objs.append(file_obj)

        self.zip_files(folder.uid)

        return {'files':[], "folder" : str(folder.uid)}
