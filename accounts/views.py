from django.views import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Index(View):
    def get(self, request, activation_code):
        try:
            print(activation_code)
            user = User.objects.get(activation_code=activation_code)
            print(user)
            user.is_active = True
            user.activation_code = ""
            user.save()
            return render(request, 'index.html', {})
        except User.DoesNotExist:
            return render(request, "dna.html", {})