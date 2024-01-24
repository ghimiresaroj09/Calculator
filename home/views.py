from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from home.models import CalculationResult
from .forms import CalculatorForm  # Create a Django form for the calculator inputs
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
def calculator(request):
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            opt = form.cleaned_data['opt']
            answer = perform_calculation(num1, num2, opt)

            # Save result to the database
            CalculationResult.objects.create(num1=num1, num2=num2, opt=opt, answer=answer)
            return redirect('calculator')  # Redirect to clear the form after POST
    else:
        form = CalculatorForm()

    results = CalculationResult.objects.all()
    return render(request, 'index.html', {"form": form, "results": results})

def perform_calculation(num1, num2, opt):
    # Perform the calculation here
    if opt == '+':
        return num1 + num2
    elif opt == '-':
        return num1 - num2
    elif opt == '*':
        return num1 * num2
    elif opt == '/':
        return num1 / num2
    else:
        return None

def edit_result(request, result_id):
    result = get_object_or_404(CalculationResult, pk=result_id)

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            opt = form.cleaned_data['opt']
            answer = perform_calculation(num1, num2, opt)

            # Update result in the database
            result.num1 = num1
            result.num2 = num2
            result.opt = opt
            result.answer = answer
            result.save()

            return redirect('calculator')  # Redirect to the calculator page
    else:
        # Pre-fill the form with the existing result data
        form = CalculatorForm(initial={'num1': result.num1, 'num2': result.num2, 'opt': result.opt})

    return render(request, 'edit_result.html', {'form': form, "result":result})

def delete_result(request, result_id):
    result = get_object_or_404(CalculationResult, pk=result_id)
    result.delete()
    return redirect('calculator')  # Redirect to the calculator page

def signup_page(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["pass1"]
        confirm_password = request.POST["pass2"]
        email = request.POST["email"]
        # Checking if the passwords match
        if username and password and email and confirm_password is not None:
            if password != confirm_password:
                return HttpResponse("<h1>Password didn't match</h1>")
            else:
                my_user = User.objects.create_user(username=username,password=password,email=email)
                my_user.save()
                return redirect('login')  
        else:
            return HttpResponse('<h1>All fields are required</h1>')
    return render(request,'signup.html',)
      

def login_page(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["pass1"]
        log_user = authenticate(request, username=username,password=password)
        if log_user is not None:
            login(request,log_user)
            return redirect('calculator')   
        else:
            return HttpResponse("<h1>Invalid Login Details</h1>")
    return render(request,'login.html')    
             

def logout_page(request):
    logout(request)
    return redirect('login')