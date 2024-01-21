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

