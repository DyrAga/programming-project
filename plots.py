from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, AutoDateFormatter
import numpy as np
import os

PLOTS_SAVE_PATH = 'static/'

def save_plot(fig, filename):
    filepath = os.path.join(PLOTS_SAVE_PATH, filename)
    fig.savefig(filepath)
    plt.close()

def draw_temperature_plot(time, temperature):
    time_objects = [datetime.fromisoformat(t) for t in time]
    fig, ax = plt.subplots(figsize = (10, 5))
    ax.plot(time_objects, temperature, linestyle = '-', color = 'b')
    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_major_formatter(AutoDateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Over Time')
    ax.grid(True)
    save_plot(fig, 'temperature_plot.png')

def draw_cloud_cover_plot(time, cloud_cover):
    time_objects = [datetime.fromisoformat(t) for t in time]
    daily_averages = {}
    for t, cc in zip(time_objects, cloud_cover):
        date_key = t.date()
        if date_key not in daily_averages:
            daily_averages[date_key] = []
        daily_averages[date_key].append(cc)
    avg_cloud_cover = [np.mean(daily_averages[date]) for date in sorted(daily_averages.keys())]
    fig, ax = plt.subplots(figsize = (10, 5))
    ax.bar(sorted(daily_averages.keys()), avg_cloud_cover, color = 'b', width = 0.7, edgecolor = 'black', linewidth = 0.7)
    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_major_formatter(AutoDateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    ax.set_xlabel('Time')
    ax.set_ylabel('Average Cloud Cover (%)')
    ax.set_title('Average Cloud Cover Per Day')
    ax.grid(axis = 'y')
    save_plot(fig, 'cloud_cover_plot.png')

def draw_precipitation_plot(time, precipitation):
    time_objects = [datetime.fromisoformat(t) for t in time]
    daily_averages = {}
    for t, cc in zip(time_objects, precipitation):
        date_key = t.date()
        if date_key not in daily_averages:
            daily_averages[date_key] = []
        daily_averages[date_key].append(cc)
    avg_precipitation = [np.mean(daily_averages[date]) for date in sorted(daily_averages.keys())]
    fig, ax = plt.subplots(figsize = (10, 5))
    ax.bar(sorted(daily_averages.keys()), avg_precipitation, color = 'b', width = 0.7, edgecolor = 'black', linewidth = 0.7)
    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_major_formatter(AutoDateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    ax.set_xlabel('Time')
    ax.set_ylabel('Average Precipitation (mm)')
    ax.set_title('Average Precipitation Per Day')
    ax.grid(axis = 'y')
    save_plot(fig, 'precipitation_plot.png')