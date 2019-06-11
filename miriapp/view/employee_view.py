from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Employee
from ..serializer.employee_serializer import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class EmployeeList(APIView):
    @csrf_exempt
    def get(self,request):
        employee=Employee.objects.all()
        serializer=EmployeeSerializer(employee,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self,request):
        employee_data=JSONParser().parse(request)
        employee_serializer= EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    @csrf_exempt
    def get(self,request,employee_id):
       try:
        employee=Employee.objects.get(pk=employee_id)
        employeeserializer=EmployeeSerializer(employee)
        return Response(employeeserializer.data)
       except Employee.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)


    @csrf_exempt
    def put(self, request,employee_id):
       try:
        employee = Employee.objects.get(pk=employee_id)
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
             employee_serializer.save()
             return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
       except Employee.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def delete(self, request,employee_id):
       try:
            employee = Employee.objects.get(pk=employee_id)
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
       except Employee.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)



