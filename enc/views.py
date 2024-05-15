from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import datas
from .forms import SignUpForm, LogInForm
from .models import UserProfile
from .ipfs import add_text_to_ipfs, get_text_from_ipfs

def add_text_to_ipfs_to_ipfs(text):
    return text


def get_text_from_ipfs_from_ipfs(text):
    return text

def register(request):
    if request.method == "POST":
        data1 = request.POST.get("data1", "")
        data2 = request.POST.get("data2", "")
        data3 = request.POST.get("data3", "")
        data4 = request.POST.get("data4", "")
        data5 = request.POST.get("data5", "")

        file_name_1 = add_text_to_ipfs(data1)
        file_name_2 = add_text_to_ipfs(data2)
        file_name_3 = add_text_to_ipfs(data3)
        file_name_4 = add_text_to_ipfs(data4)
        file_name_5 = add_text_to_ipfs(data5)

        if None in (file_name_1, file_name_2, file_name_3, file_name_4, file_name_5):
            error_message = "Error processing data"
            return render(request, "form.html", {
                'error_message': error_message,
                'data1': data1,
                'data2': data2,
                'data3': data3,
                'data4': data4,
                'data5': data5
            })

        encrypted_data_entry = datas(
            data1=file_name_1,
            data2=file_name_2,
            data3=file_name_3,
            data4=file_name_4,
            data5=file_name_5,
        )
        encrypted_data_entry.save()
        return redirect('decrypt_all_data')

    return render(request, "form.html")

def decrypt_all_data(request):
    encrypted_data_entries = datas.objects.all()
    decrypted_data_list = []

    for entry in encrypted_data_entries:
        data1 = get_text_from_ipfs(entry.data1)
        data2 = get_text_from_ipfs(entry.data2)
        data3 = get_text_from_ipfs(entry.data3)
        data4 = get_text_from_ipfs(entry.data4)
        data5 = get_text_from_ipfs(entry.data5)

        decrypted_data_list.append({
            'data1': data1,
            'data2': data2,
            'data3': data3,
            'data4': data4,
            'data5': data5
        })

    return render(request, 'decrypted_data.html', {'decrypted_data_list': decrypted_data_list})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserProfile.objects.filter(username=username, password=password).first()
            if user:
                return redirect('register')
            else:
                error = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})

def encryption_demo(request):
    return render(request, 'encryption_demo.html')
