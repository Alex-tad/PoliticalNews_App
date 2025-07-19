from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by('-published')
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_breaking', 'language']  # 🔍 Enable filters
