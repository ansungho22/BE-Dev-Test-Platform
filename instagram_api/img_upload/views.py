import boto3
import uuid
from instagram.settings import (
    AWS_SECRET_ACCESS_KEY,
    AWS_ACCESS_KEY_ID,
    AWS_STORAGE_BUCKET_NAME,
    AWS_S3_CUSTOM_DOMAIN,
)
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from .models import Instagram
from django.core.paginator import Paginator

# Create your views here.


class PostAPIView(APIView):
    def get(self, request, pk, format=None):
        PageNum = int(pk)

        paginator = Paginator(Instagram.objects.all(), 3)
        Current_IndexList = paginator.get_page(PageNum)

        Start_PageNum, End_PageNum = (
            list(paginator.page_range)[0],
            list(paginator.page_range)[-1],
        )

        PageIndex = {"start_index": Start_PageNum, "end_index": End_PageNum}
        PostList = []

        for Post in Current_IndexList:
            PostDict = {
                "Title": Post.Title,
                "Context": Post.Context,
                "UploadImage": Post.UploadImage,
            }
            PostList.append(PostDict)

        ReturnContext = {"page_range": PageIndex, "post_list": PostList}
        return JsonResponse(ReturnContext, status=200)

    def post(self, request):
        PostObjects = Instagram.objects.create(
            Title=request.data["title"],
            Context=request.data["content"],
            UploadImage=request.data.getlist("photo_URL"),
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
        URL_list = {}
        index = 1
        ImageList = request.FILES.getlist("photo")
        for Image in ImageList:
            url_generator = str(uuid.uuid4())
            self.s3_client.upload_fileobj(
                Image,
                AWS_STORAGE_BUCKET_NAME,
                "images/{}".format(url_generator),
                ExtraArgs={"ContentType": "image/jpeg"},
            )
            S3_URL = AWS_S3_CUSTOM_DOMAIN + url_generator
            URL_list[index] = S3_URL
            index = index + 1

        return JsonResponse(URL_list, status=200, safe=False)
