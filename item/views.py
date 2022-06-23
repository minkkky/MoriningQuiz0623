from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class  ItemView(APIView): # CBV 방식

    # 아이템 조회
    def get(self, request):
        return Response({'message': 'get method!!'})

    #  아이템 등록
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})


class  ItemOrderView(APIView): # CBV 방식

    # order_id로 주문내역 조회
    def get(self, request):
        return Response({'message': 'get method!!'})

    
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})

