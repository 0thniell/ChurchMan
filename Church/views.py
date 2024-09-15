from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .forms import *
from django.db.models import Sum
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required(login_url='/login')
def home_view(request):
    return render(request, 'Church/base.html')

# MEMBERS

def members_view(request):
    members = Members.objects.all()
    return render(request, 'members.html', {'members': members})

class MembersCreateView(CreateView):
    model = Members
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/members'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class MembersUpdateView(UpdateView):
    model = Members
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/members'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class MemberDeleteView(DeleteView):
    model = Members
    success_url = '/members'
    template_name = 'church/delete.html'


# SERVICE
def service_view(request):
    services = Church_Service.objects.all()
    return render(request, 'service.html', {'services': services})

class ServiceCreateView(CreateView):
    model = Church_Service
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class ServiceUpdateView(UpdateView):
    model = Church_Service
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class ServiceDeleteView(DeleteView):
    model = Church_Service
    success_url = '/service'
    template_name = 'church/delete.html'


# EVENTS
def event_view(request):
    events = Church_Event_Register.objects.all()
    return render(request, 'event.html', {'events': events})

class EventCreateView(CreateView):
    model = Church_Event_Register
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class EventUpdateView(UpdateView):
    model = Church_Event_Register
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class EventDeleteView(DeleteView):
    model = Church_Event_Register
    success_url = '/event'
    template_name = 'church/delete.html'


# First_Timer
def first_view(request):
    firsttimers = First_Timer.objects.all()
    return render(request, 'firsttimer.html', {'firsttimers': firsttimers})

class FirstCreateView(CreateView):
    model = First_Timer
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/first-timer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class FirstUpdateView(UpdateView):
    model = First_Timer
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/first-timer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class FirstDeleteView(DeleteView):
    model = First_Timer
    success_url = '/first-timer'
    template_name = 'church/delete.html'


# Order_Of_Service
def order_of_service_view(request):
    order_of_service = Order_Of_Service.objects.all()
    return render(request, 'order_of_service.html', {'order_of_service': order_of_service})

class OrderCreateView(CreateView):
    model = Order_Of_Service
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/order_of_service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class OrderUpdateView(UpdateView):
    model = Order_Of_Service
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/order_of_service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class OrderDeleteView(DeleteView):
    model = Order_Of_Service
    success_url = '/order_of_service'
    template_name = 'church/delete.html'


# Facility_Management
def facility_management_view(request):
    facility_managements = Facility_Management.objects.all()
    return render(request, 'facilitymanagement.html', {'facility_managements': facility_managements })

class FacilityCreateView(CreateView):
    model = Facility_Management
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/facility_management'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class FacilityUpdateView(UpdateView):
    model = Facility_Management
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/facility_management'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class FacilityDeleteView(DeleteView):
    model = Facility_Management
    success_url = '/facility_management'
    template_name = 'church/delete.html'



# Inventory
def inventory_view(request):
    inventorys = Inventory.objects.all()
    return render(request, 'inventory.html', {'inventorys': inventorys})

class InventoryCreateView(CreateView):
    model = Inventory
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/inventory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class InventoryUpdateView(UpdateView):
    model = Inventory
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/inventory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class InventoryDeleteView(DeleteView):
    model = Inventory
    success_url = '/inventory'
    template_name = 'church/delete.html'


# Income
def income_view(request):
    income = Income.objects.all()
    return render(request, 'income.html', {'income': income})

class IncomeCreateView(CreateView):
    model = Income
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/income'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class IncomeUpdateView(UpdateView):
    model = Income
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/income'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class IncomeDeleteView(DeleteView):
    model = Income
    success_url = '/income'
    template_name = 'church/delete.html'

# Expense
def expense_view(request):
    expenses = Expense.objects.all()
    return render(request, 'expense.html', {'expenses': expenses})

class ExpenseCreateView(CreateView):
    model = Expense
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/expense'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/expense'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = '/expense'
    template_name = 'church/delete.html'

# Profit and Loss
def profit_loss_view(request):
    total_income = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    profit_loss = total_income - total_expenses

    if total_income > total_expenses:
        result = total_income - total_expenses
        status = 'Profit'
    else:
        result = total_expenses - total_income
        status = 'Loss'

    context = {
    'total_income': total_income,
    'total_expenses': total_expenses,
    'profit_loss': profit_loss,
    'status': status,
    }
    return render(request, 'church/profit_loss.html', context)


#Department
def department_view(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departmentdetail.html'
    context_object_name = 'department'

    def get_object(self):
        name = self.kwargs.get("name")
        return get_object_or_404(Department, name=name)


class DepartmentCreateView(CreateView):
    model = Department
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/department'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/department'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

    def get_object(self):
        name = self.kwargs.get("name")
        return get_object_or_404(Department, name=name)

class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = '/department'
    template_name = 'church/delete.html'

    def get_object(self):
        name = self.kwargs.get("name")
        return get_object_or_404(Department, name=name)


#churcharms
def churcharm_view(request):
    churcharms = Churcharm.objects.all()
    return render(request, 'churcharm.html', {'churcharms': churcharms})

class ChurcharmDetailView(DetailView):
    model = Churcharm
    template_name = 'churcharmdetail.html'
    context_object_name = 'churcharm'

    def get_object(self):
        name = self.kwargs.get("name")
        return get_object_or_404(Churcharm, name=name)


class ChurcharmCreateView(CreateView):
    model = Churcharm
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = '/churcharm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        return context

class ChurcharmUpdateView(UpdateView):
    model = Churcharm
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url= '/churcharm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

    def get_object(self):
        name = self.kwargs.get("name")
        return get_object_or_404(Churcharm, name=name)

class ChurcharmDeleteView(DeleteView):
    model = Churcharm
    success_url = '/churcharm'
    template_name = 'church/delete.html'

    def get_object(self):
        name = self.kwargs.get("name")
        return get_object_or_404(Department, name=name)



# Payroll List View (shows a list of payrolls)
class PayrollListView(ListView):
    model = Payroll
    template_name = 'payroll_list.html'
    context_object_name = 'payrolls'

# Payroll Detail View (shows details of a single payroll)
# class PayrollDetailView(DetailView):
#     model = Payroll
#     template_name = 'payroll_detail.html'
#     context_object_name = 'payroll'

# Payroll Create View (allows creation of a payroll)
class PayrollCreateView(CreateView):
    model = Payroll
    fields = ['member', 'date', 'gross']
    template_name = 'church/forms.html'
    success_url = reverse_lazy('payroll')

# Payroll Update View (allows updating a payroll)
class PayrollUpdateView(UpdateView):
    model = Payroll
    fields = '__all__'
    template_name = 'church/forms.html'
    success_url = reverse_lazy('payroll')

# Payroll Delete View (allows deleting a payroll)
class PayrollDeleteView(DeleteView):
    model = Payroll
    template_name = 'church/delete.html'
    success_url = reverse_lazy('payroll')
