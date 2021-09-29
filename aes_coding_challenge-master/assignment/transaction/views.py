from django.http import response
from .models import Transaction,TransactionLineItemDetails,InventoryItem
from .serializers import TransactionSerializers,LineItemSerializer,InventoryItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.




@api_view(['POST'])
def AddTrancDoc(request):
    serilizer = TransactionSerializers(data=request.data)

    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)    



@api_view(['POST'])
def AddLineItem(request):
    serilizerLT = LineItemSerializer(data=request.data)

    if serilizerLT.is_valid():
        serilizerLT.save()
    return Response(serilizerLT.data)    

@api_view(['POST'])
def AddInventryToLineItem(request):
    serilizerLI = LineItemSerializer(data=request.data)
    Rate_per_unit = request.GET.get('Rate_per_unit')

    InventorItem   = InventoryItem.objects.all()
    for i in InventorItem:
        serilizerLI(Article =i.Article,Colour=i.Colour,Unit=i.Unit,Quantity=i.Gross_Quantity,Rate_per_unit=Rate_per_unit)
        if serilizerLI.is_valid():
            serilizerLI.save()
    return Response(serilizerLI.data)  



@api_view(['DELETE'])
def deleteMethod(request,pk):
    task = Transaction.objects.get(Id=pk)
    task.delete()

    return Response("Item sussceFully deleted")


@api_view(['GET'])
def ViewModel(request):
    Tr = Transaction.objects.all()
    LT = TransactionLineItemDetails.objects.all()
    II= InventoryItem.objects.all()

    TrSerializer =TransactionSerializers(Tr, many = True)
    LTserializer = LineItemSerializer(LT , many=True)
    IIserializer = InventoryItemSerializer(II, many=True)
    ResultModel = TrSerializer.data + LTserializer.data +  IIserializer.data
    return Response(ResultModel)



@api_view(['GET'])
def ApiOverview(request):
    api_urls ={
      '1.Add a transaction document with its line items':'AddTrancDoc/',
      '2.Add line items once a transaction is created.':'AddLineItem/',
      '3.Add multiple inventory items to line items.':'AddInventryToLineItem/',
      '4.Delete':'deleteMethod/<str:pk>/',
      '5.View a transaction with all its line items and their inventory items.': 'ViewModel/',
       } 
    return Response(api_urls)      