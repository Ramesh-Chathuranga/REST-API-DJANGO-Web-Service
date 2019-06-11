from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializer.company_serializers import CompanySerializer
from ..models import Company



class CompanyList(APIView):
    @csrf_exempt
    def get(self,request):
        company=Company.objects.all()
        serializer=CompanySerializer(company,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self,request):
        company_data=JSONParser().parse(request)
        company_serializer= CompanySerializer(data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)




class CompanyDetail(APIView):
    @csrf_exempt
    def get(self,request,company_id):
       try:
          company=Company.objects.get(pk=company_id)
          companyserializer=CompanySerializer(company)
          return Response(companyserializer.data)
       except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def put(self, request,company_id):
       try:
            company = Company.objects.get(pk=company_id)
            company_data = JSONParser().parse(request)
            company_serializer = CompanySerializer(company,data=company_data)
            if company_serializer.is_valid():
               company_serializer.save()
               return Response(status=status.HTTP_204_NO_CONTENT)
       except Company.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request,company_id):
       try:
        company = Company.objects.get(pk=company_id)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



