from .forms import NewsLetterForm


def base_data(request):
    return {"my_form": NewsLetterForm(request.GET)}
