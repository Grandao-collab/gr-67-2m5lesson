from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from django.forms import model_to_dict
from .serializers import FilmListSerializer, FilmDetailSerializer


@api_view(['GET'])
def film_detail_api_view(request, id):
    try:
        film = Film.objects.get(id=id)
    except:
        return Response(data='Film not found!', status=status.HTTP_404_NOT_FOUND)
    data = FilmDetailSerializer(film, many=False).data
    return Response(data=data)


@api_view(['GET', 'POST'])
def film_list_create_api_view(request):
    if request.method == 'GET':
        # step 1: collect films (queryset)
        films = Film.objects.select_related('director').prefetch_related('genres', 'Review').all()
            # step 2: reformat queryset to list of dictionaries (serializer)
        list_ = FilmListSerializer(films, many=True).data
            # step 3: return response
        return Response(data=list_)
    elif request.method == 'POST':
        # step 1: receive data
        title = request.data.get('title')
        text = request.data.get('text')
        release_year = request.data.get('release_year')
        rating = request.data.get('rating')
        is_hit = request.data.get('is_hit')
        print(title, text, release_year, rating, is_hit)
        # step 2: create film
        film = Film.objects.create(
            title=title,
            text=text,
            release_year=release_year,
            rating=rating,
            is_hit=is_hit
        )
        # step 3: return response
        return Response(status=status.HTTP_201_CREATED, 
                        data=FilmDetailSerializer(film).data)