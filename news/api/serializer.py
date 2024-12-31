from rest_framework import serializers
from news.models import Article,Journalist
from rest_framework.validators import UniqueTogetherValidator
from datetime import datetime
from django.utils.timesince import timesince
from django.core.exceptions import ValidationError

class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField(method_name='the_time')
    author = serializers.StringRelatedField()
    class Meta:         
        model = Article
        # exclude = ['id']
        fields = '__all__'
        
    def the_time(self,object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date,now)
        return time_delta
    
    validators = [
        UniqueTogetherValidator(
            queryset=Article.objects.all(),
            fields=['title', 'description']
        )
    ]

    def validate_title(self,value):
      if len(value) <= 40:
        raise ValidationError("This field must be more than 40 characters.")
      return value
        
class JournalistSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(read_only=True,many=True)
    class Meta:
        model = Journalist
        fields = '__all__'