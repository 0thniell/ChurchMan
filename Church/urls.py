from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_view, name='home'),

    #Members Feature
    path('members', members_view, name='members'),
    path('members/new/', MembersCreateView.as_view(), name='add_members'),
    path('members/update/<int:pk>', MembersUpdateView.as_view(), name='update-member'),
    path('members/delete/<int:pk>', MemberDeleteView.as_view(), name='delete-member'),

    #Service Feature
    path('service', service_view, name='service'),
    path('service/new/', ServiceCreateView.as_view(), name='add_service'),
    path('service/update/<int:pk>', ServiceUpdateView.as_view(), name='update-service'),
    path('service/delete/<int:pk>', ServiceDeleteView.as_view(), name='delete-service'),

    # Event Feature
    path('event', event_view, name='event'),
    path('event/new/', EventCreateView.as_view(), name='add_event'),
    path('event/update/<int:pk>', EventUpdateView.as_view(), name='update-event'),
    path('event/delete/<int:pk>', EventDeleteView.as_view(), name='delete-event'),

    # First-Timer Feature
    path('first-timer', first_view, name='first-timer'),
    path('first-timer/new/', FirstCreateView.as_view(), name='add_firsttimer'),
    path('first-timer/update/<int:pk>', FirstUpdateView.as_view(), name='update-first-timer'),
    path('first-timer/delete/<int:pk>', FirstDeleteView.as_view(), name='delete-first-timer'),

    # Order of Service Feature
    path('order_of_service', order_of_service_view, name='order_of_service'),
    path('order_of_service/new/', OrderCreateView.as_view(), name='add-order-of-service'),
    path('order_of_service/update/<int:pk>', OrderUpdateView.as_view(), name='update-order-of-service'),
    path('order_of_service/delete/<int:pk>', OrderDeleteView.as_view(), name='delete-order-of-service'),

    # Facility Management Feature
    path('facility_management', facility_management_view, name='facility_management'),
    path('facility_management/new/', FacilityCreateView.as_view(), name='add-facility_management'),
    path('facility_management/update/<int:pk>', FacilityUpdateView.as_view(), name='update-facility_management'),
    path('facility_management/delete/<int:pk>', FacilityDeleteView.as_view(), name='delete-facility_management'),

    # Inventory Feature
    path('inventory', inventory_view, name='inventory'),
    path('inventory/new/', InventoryCreateView.as_view(), name='add-inventory'),
    path('inventory/update/<int:pk>', InventoryUpdateView.as_view(), name='update-inventory'),
    path('inventory/delete/<int:pk>', InventoryDeleteView.as_view(), name='delete-inventory'),

    # Income Feature
    path('income', income_view, name='income'),
    path('income/new/', IncomeCreateView.as_view(), name='add-income'),
    path('income/update/<int:pk>', IncomeUpdateView.as_view(), name='update-income'),
    path('income/delete/<int:pk>', IncomeDeleteView.as_view(), name='delete-income'),

    # Expense Feature
    path('expense', expense_view, name='expense'),
    path('expense/new/', ExpenseCreateView.as_view(), name='add-expense'),
    path('expense/update/<int:pk>', ExpenseUpdateView.as_view(), name='update-expense'),
    path('expense/delete/<int:pk>', ExpenseDeleteView.as_view(), name='delete-expense'),

    #profit loss feature
    path('profit_loss', profit_loss_view, name='profit_loss'),

    # Department Feature
    path('department', department_view, name='department'),
    path('department/new/', DepartmentCreateView.as_view(), name='add-department'),
    path('department/update/<str:name>', DepartmentUpdateView.as_view(), name='update-department'),
    path('department/delete/<str:name>', DepartmentDeleteView.as_view(), name='delete-department'),

    path('department/<str:name>/', DepartmentDetailView.as_view(), name='department_detail'),

    # Churcharm Feature
    path('churcharm', churcharm_view, name='churcharm'),
    path('churcharm/new/', ChurcharmCreateView.as_view(), name='add-churcharm'),
    path('churcharm/update/<str:name>', ChurcharmUpdateView.as_view(), name='update-churcharm'),
    path('churcharm/delete/<str:name>', ChurcharmDeleteView.as_view(), name='delete-churcharm'),

    path('churcharm/<str:name>/', ChurcharmDetailView.as_view(), name='churcharm_detail'),

    # Payroll Feature
    path('payroll', PayrollListView.as_view(), name='payroll'),
    # path('payroll/<int:pk>/', PayrollDetailView.as_view(), name='payroll_detail'),
    path('payroll/new/', PayrollCreateView.as_view(), name='payroll_create'),
    path('payroll/<str:pk>/update/', PayrollUpdateView.as_view(), name='payroll_update'),
    path('payroll/<str:pk>/delete/', PayrollDeleteView.as_view(), name='payroll_delete'),
]
