# Create your views here.
from django.shortcuts import render, redirect
from .forms import CSVFileForm
from .models import CSVFile
import pandas as pd
import os
from django.conf import settings
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import unquote


def upload(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            filename = file.name
            filename = filename.replace(" ", "_")
            file_path = os.path.join(settings.MEDIA_ROOT, 'csvs', filename)
            if os.path.exists(file_path):
                return redirect('file_already_uploaded', filename=filename)
            form.save()
            return redirect('success', filename=filename)
    else:
        form = CSVFileForm()
    return render(request, 'main/upload.html', {'form': form})

def success(request, filename):
    return render(request, 'main/success.html', {'filename': filename})

def file_already_uploaded(request, filename):
    return render(request, 'main/file_already_uploaded.html', {'filename': filename})



def first_rows(request, filename):
    filename = unquote(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'csvs', filename)
    df = pd.read_csv(file_path)
    
    # Get column headers
    column_headers = df.columns.tolist()
    
    # Get first few rows excluding the header row as HTML
    first_rows_html = df.head().to_html(index=False)
    
    return render(request, 'main/first_rows.html', {'first_rows': first_rows_html, 'column_headers': column_headers, 'filename': filename})



def statistics(request, filename):
    filename = unquote(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'csvs', filename)
    df = pd.read_csv(file_path)
    statistics = df.describe().to_html()
    return render(request, 'main/statistics.html', {'statistics': statistics,'filename': filename})

def handle_missing_values(request, filename):
    filename = unquote(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'csvs', filename)
    df = pd.read_csv(file_path)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        column = request.POST.get('column')
        fill_value = request.POST.get('fill_value')

        if action == 'drop':
            df = df.dropna(subset=[column])
        elif action == 'fill':
            df[column] = df[column].fillna(fill_value)
        elif action == 'interpolate':
            df[column] = df[column].interpolate()

        df.to_csv(file_path, index=False)
        return redirect('handle_missing_values', filename=filename)

    missing_values = df.isnull().sum().to_frame('Missing Values')
    columns = df.columns
    missing_values_html = missing_values.to_html()

    return render(request, 'main/handle_missing_values.html', {
        'missing_values': missing_values_html,
        'filename': filename,
        'columns': columns
    })

def visualize_data(request, filename):
    filename = unquote(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'csvs', filename)
    df = pd.read_csv(file_path)
    plot_columns = []

    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        df[column].plot(kind='hist')
        plot_filename = f'{column}_hist.png'
        plot_path = os.path.join(settings.MEDIA_ROOT, plot_filename)
        plt.title(f'Histogram of {column}')
        plt.savefig(plot_path)
        plt.close()
        plot_columns.append((plot_filename, column))  # Append tuple of (plot_filename, column_name)

    return render(request, 'main/visualize_data.html', {
        'plot_columns': plot_columns,
        'MEDIA_URL': settings.MEDIA_URL,
        'filename': filename,
    })

