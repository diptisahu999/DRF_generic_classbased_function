from django.shortcuts import render
from rest_framework.decorators import api_view 
from .serializers import Serializers
from .models import Student
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

# Create your views here.


# @api_view(['GET','POST'])
# def studentlistview(request):
#     if request.method=='GET':
#         stu_list=Student.objects.all()
#         serializer=Serializers(stu_list,many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=Serializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     else:
#         return Response(serializer.errors)


# @api_view(['DELETE','PUT','GET'])
# def studentdetailview(request,pk):
#     try:
#         student=Student.objects.get(id=pk)
#     except Student.DoesNotExist:
#         return Response(status=404)
#     if request.method=="DELETE":
#         student.delete()
#         return Response({'data':'data delete successfully!!!'})
#     elif request.method=='GET':
#         serializer=Serializers(student)
#         return Response(serializer.data)
#     elif request.method=="PUT":
#         serializer=Serializers(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'data update successfully!!!','alldata':serializer.data})
#     else:
#         return Response(serializer.errors)
class ListViewStudent(APIView):
    def get(self,request,format=None):
        student=Student.objects.all()
        serializer=Serializers(student,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ListDelete(APIView):    
    def delete(self,request,id):
        stu=Student.objects.get(id=id)
        stu.delete()
        student=Student.objects.all()
        serializer=Serializers(student,many=True)
        return Response(serializer.data)
class ListEdit(APIView):    
    def put(self,request,id):
        stu=Student.objects.get(id=id)
        stu_obj=Serializers(stu,data=request.data)
        if stu_obj.is_valid():
            stu_obj.save()
            student=Student.objects.all()
            serializer=Serializers(student,many=True)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    # def get_object(self, pk):
    #     try:
    #         return Student.objects.get(pk=pk)
    #     except Student.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = Serializers(snippet)
    #     return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = Serializers(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)    
