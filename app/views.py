from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.views.generic import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from .templatetags.helper_tags import eligible, bizzfuzz
from .models import User
from .utils import ExcelWriter

from xlwt import Workbook
import StringIO


class UserListView(ListView):
    model = User


class UserCreateView(CreateView):
    model = User
    template_name = 'app/user_create.html'
    fields = ['username', 'birthday', 'password']
    success_url = reverse_lazy('user_list')


class UserDetailView(DetailView):
    model = User


class UserEditView(UpdateView):
    model = User
    template_name = 'app/user_create.html'
    fields = ['username', 'birthday', 'password']


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')


class UserExportView(View):

    def post(self, request):
        book = Workbook(style_compression=2)
        sheet = book.add_sheet('User List')
        writer = ExcelWriter(sheet)

        header_columns = ['Username', 'Birthday',
                          'Eligible', 'Random Number', 'BizzFuzz']

        writer.writerow(header_columns)

        for user in User.objects.all():
            export_data = [
                user.username,
                user.birthday,
                eligible(user),
                user.random_number,
                bizzfuzz(user)
            ]

            writer.writerow(export_data)

        out = StringIO.StringIO()
        book.save(out)

        response = HttpResponse(
            out.getvalue(), content_type='application/vnd.ms-excel')

        response['Content-Disposition'] = 'attachment; filename=user_list.xls'
        return response
