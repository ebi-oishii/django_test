from django.shortcuts import render
import logging
import time
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import ListView
# Create your views here.

logger = logging.getLogger(__name__)

class SampleView(View):
    def post(self, request, *args, **kwargs):
        start_time = time.time()
        logging.info(f"User({request.user.id}) posted.")

        logger.debug(f"Finished in {time.time() - start_time:.2f} sec.")
        return render(request, "sample.html")


class BookListView(ListView):
    model = Book

book_detail = BookDetail.as_view()