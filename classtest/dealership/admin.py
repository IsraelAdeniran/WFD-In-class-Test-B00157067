from django.contrib import admin
from .models import Salesperson, Customer, Car, SalesInvoice, Mechanic, Service, ServiceTicket, ServiceMechanic, Parts, PartsUsed


# Register your models here.

admin.site.register(Salesperson)
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(SalesInvoice)
admin.site.register(Mechanic)
admin.site.register(Service)
admin.site.register(ServiceTicket)
admin.site.register(ServiceMechanic)
admin.site.register(Parts)
admin.site.register(PartsUsed)