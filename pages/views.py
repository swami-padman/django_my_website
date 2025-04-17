from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


class SoftwareTestingPageView(TemplateView):
    template_name = 'pages/software-testing.html'


class FindGeoLocPageView(TemplateView):
    template_name = 'pages/find-geo-loc.html'


class CheckPalindromePageView(TemplateView):
    template_name = 'pages/check-palindrome.html'


class TempConversionPageView(TemplateView):
    template_name = 'pages/temperature-conversion.html'


def palindrome_check(request):
    result = None
    input_value = ''

    if request.method == "POST":
        input_value = request.POST.get('input_string', '')
        accept_spaces = request.POST.get('accept_spaces', False)

        # Remove spaces if the checkbox is not checked
        if not accept_spaces:
            input_value = input_value.replace(" ", "")

        # Check if the string is a palindrome
        is_palindrome = input_value == input_value[::-1]
        result = f'The input "{input_value}" is {"a" if is_palindrome else "not a"} palindrome.'

    return render(request, 'pages/check-palindrome.html', {
        'result': result,
        'input_value': input_value,  # Pass the input value to the template
    })


def temp_conversion(request):
    result = ''
    temp_f = None
    temp_c = None

    if request.method == "POST":
        if 'conversion_type' in request.POST:
            conversion_type = request.POST['conversion_type']
            if conversion_type == 'c_to_f':
                temp_c = float(request.POST.get('temp_in_celsius', ''))
                temp_f = (temp_c * 9/5) + 32
                result = f'{temp_c}°C is {temp_f:.2f}°F'
            elif conversion_type == 'f_to_c':
                temp_f = float(request.POST.get('temp_in_fahrenheit', ''))
                temp_c = (temp_f - 32) * 5/9
                result = f'{temp_f}°F is {temp_c:.2f}°C'

    return render(request, 'pages/temperature-conversion.html', {
        'result': result,
        'temp_in_fahrenheit': temp_f,
        'temp_in_celsius': temp_c,
    })