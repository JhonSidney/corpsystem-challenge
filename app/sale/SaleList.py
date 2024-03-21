from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sale.models import Sale
from seller.models import Seller
from customer.models import Customer
from sale.api.serializers import SaleSerializer
from datetime import datetime
from django.http import HttpResponse
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class SaleListAPIView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start')
        end_date = request.query_params.get('end')
        seller = request.query_params.get('seller')
        customer = request.query_params.get('customer')

        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
                end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
            except ValueError:
                return Response({"SaleListAPIView-Error": "Invalid date format. Please provide dates in the format dd/mm/yyyy."}, status=status.HTTP_400_BAD_REQUEST)
            
            all_sales = Sale.objects.filter(sale_date__range=(start_date, end_date))
        
        elif seller:
            try:
                seller_list = seller.split()
                seller = Seller.objects.get(first_name=seller_list[0], last_name=seller_list[1])
                all_sales = Sale.objects.filter(associated_seller=seller)

            except ValueError:
                return Response({"SaleListAPIView-Error": "The seller not found."}, status=status.HTTP_400_BAD_REQUEST)
        elif customer:
            try:
                customer_list = customer.split()
                customer = Customer.objects.get(first_name=customer_list[0], last_name=customer_list[1])
                all_sales = Sale.objects.filter(associated_customer=customer)

            except ValueError:
                return Response({"SaleListAPIView-Error": "The customer not found."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            all_sales = Sale.objects.all()
        
        serializer = SaleSerializer(all_sales, many=True)
        if request.query_params.get('export_csv'):
            return SaleListAPIView.export_to_csv(serializer.data)
        if request.query_params.get('export_pdf'):
            return SaleListAPIView.export_to_pdf(serializer.data)
        return Response(serializer.data)
    
    def export_to_csv(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sales_data.csv"'

        csv_columns=['sale_id', 'sale_date', 'associated_customer', 'associated_seller', 'sale_value', 'sale_status',
                    'payment_methods', 'product_id', 'product_name', 'supplier', 'price', 'stock_quantity', 'ean_cod']
        
        writer = csv.DictWriter(response, fieldnames=csv_columns)
        writer.writeheader()
        
        for sale in request:
            for product in sale['products']:
                sale_data = sale.copy()
                sale_data.update(product)
                del sale_data['products']
                writer.writerow(sale_data)

        return response
    
    def export_to_pdf(data):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="sales_report.pdf"'        
        doc = SimpleDocTemplate(response, pagesize=landscape(letter))
        
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        table_data = []
        table_data.append(['SALES REPORT'])

        last_row_index = len(table_data) - 1
        table_data[last_row_index] = ['-' if cell_value == 'SALES REPORT:' else cell_value for cell_value in table_data[last_row_index]]
        style.add('SPAN', (0, last_row_index), (-2, last_row_index))

        table_data.append(['SALE_DATE', 'CUSTOMER','SELLER','SALE_VALUE','SALE_STATUS','EAN COD.','ALL_PRODUCTS','PRICE PROD'])

        for sale in data:
            all_prices = []
            table_data.append([sale['sale_date'], sale['associated_customer'], sale['associated_seller'],sale['sale_value'],sale['sale_status']])  # Modify as per your serializer structure
            for product in sale['products']:
                table_data.append(['-','-','-','-','-',product['ean_cod'],product['product_name'],product['price'],])
                all_prices.append(float(product['price']))
           
            total_price = sum(all_prices)
            subtotal = {"subtotal":f"{total_price:.2f}"}

            
            table_data.append(['SUBTOTAL','-','-','-','-','-','-:','R$ '+subtotal['subtotal']])
            last_row_index = len(table_data) - 1
            table_data[last_row_index] = ['SUBTOTAL' if cell_value == '-' else cell_value for cell_value in table_data[last_row_index]]
            style.add('SPAN', (0, last_row_index), (-2, last_row_index))

        table = Table(data=table_data)
        table.setStyle(style)

        doc.build([table])

        return response