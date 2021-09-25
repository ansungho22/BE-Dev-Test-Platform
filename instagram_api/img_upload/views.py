import boto3
import uuid
from instagram.settings import (
    AWS_SECRET_ACCESS_KEY,
    AWS_ACCESS_KEY_ID,
    AWS_STORAGE_BUCKET_NAME,
    AWS_S3_CUSTOM_DOMAIN,
)
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Instagram
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rest_framework import exceptions
import ast
# Create your views here.


class PostAPIView(APIView):
    def get(self, request, pk, format=None):
        current_pagenum = int(pk)

        paginator = Paginator(Instagram.objects.all(), 3)
        start_pagenum, end_pagenum = (
            list(paginator.page_range)[0],
            list(paginator.page_range)[-1],
        )
        try:
            current_page = paginator.page(current_pagenum)
        except EmptyPage or PageNotAnInteger:
            raise exceptions.ParseError("PageNotFound")
          
        page_range = {"start_page": start_pagenum,"current_page":current_pagenum ,"end_page": end_pagenum}
        posts= []

        for context in current_page:
            post = {
                "Title": context.Title,
                "Context": context.Context,
                "UploadImage": ast.literal_eval(context.Image),
            }
            posts.append(post)
        
        context = {"page_range": page_range, "post_list": posts}
        return JsonResponse(context, status=200)

    def post(self, request):
        PostObjects = Instagram.objects.create(
            Title=request.data["title"],
            Context=request.data["context"],
            Image=request.data.getlist("photo_URL"),
        )
        PostObjects.save()
        return JsonResponse(request.data, status=200)


class ImageAPIView(APIView):

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    def post(self, request):
        URLs = {}
        index = 1
        images = request.FILES.getlist("photo")
        for Image in images:
            url_generator = str(uuid.uuid4())
            self.s3_client.upload_fileobj(
                Image,
                AWS_STORAGE_BUCKET_NAME,
                "images/{}".format(url_generator),
                ExtraArgs={"ContentType": "image/jpeg"},
            )
            S3_URL = AWS_S3_CUSTOM_DOMAIN + url_generator
            URLs[index] = S3_URL
            index = index + 1

        return JsonResponse(URLs, status=200, safe=False)
