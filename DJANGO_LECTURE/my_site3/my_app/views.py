from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html 
    return render(request, 'my_app/example.html')

def variable_view(request):

    # dictionary 
    my_var = {
        'first_name':'rosaLind',
        'last_name': 'franklyn',
        'some_list': [1, 2, 3],
        'some_dict': {'inside_key':'inside_value', 'inside_key2':'inside_value2'},
        'user_logged_in':True,
    }

    # context 렌더링 전달 
    return render(request, 'my_app/variable.html', context=my_var)
