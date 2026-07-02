import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytrainproject.settings')
django.setup()

from trainapp.models import Train

Train.objects.all().delete()

trains = [
    {
        'train_number': '12621',
        'train_name': 'Tamil Nadu Express',
        'source': 'Chennai Central',
        'destination': 'New Delhi',
        'departure_time': '22:30:00',
        'arrival_time': '05:30:00',
        'total_seats': 720
    },
    {
        'train_number': '12627',
        'train_name': 'Karnataka Express',
        'source': 'KSR Bengaluru',
        'destination': 'New Delhi',
        'departure_time': '20:15:00',
        'arrival_time': '05:40:00',
        'total_seats': 680
    },
    {
        'train_number': '12951',
        'train_name': 'Mumbai Rajdhani Express',
        'source': 'New Delhi',
        'destination': 'Mumbai Central',
        'departure_time': '16:35:00',
        'arrival_time': '08:35:00',
        'total_seats': 590
    },
    {
        'train_number': '12301',
        'train_name': 'Howrah Rajdhani Express',
        'source': 'New Delhi',
        'destination': 'Howrah Junction',
        'departure_time': '17:00:00',
        'arrival_time': '10:05:00',
        'total_seats': 620
    },
    {
        'train_number': '12625',
        'train_name': 'Kerala Express',
        'source': 'Thiruvananthapuram',
        'destination': 'New Delhi',
        'departure_time': '12:20:00',
        'arrival_time': '11:00:00',
        'total_seats': 750
    },
    {
        'train_number': '12259',
        'train_name': 'Sealdah Duronto Express',
        'source': 'New Delhi',
        'destination': 'Sealdah',
        'departure_time': '20:10:00',
        'arrival_time': '12:45:00',
        'total_seats': 560
    },
    {
        'train_number': '22691',
        'train_name': 'Bengaluru Rajdhani Express',
        'source': 'Chennai Central',
        'destination': 'KSR Bengaluru',
        'departure_time': '06:00:00',
        'arrival_time': '11:00:00',
        'total_seats': 480
    },
    {
        'train_number': '12431',
        'train_name': 'Trivandrum Rajdhani Express',
        'source': 'New Delhi',
        'destination': 'Thiruvananthapuram',
        'departure_time': '10:55:00',
        'arrival_time': '09:15:00',
        'total_seats': 650
    },
    {
        'train_number': '12621',
        'train_name': 'Chennai Mail',
        'source': 'Chennai Central',
        'destination': 'Mumbai CST',
        'departure_time': '23:45:00',
        'arrival_time': '05:10:00',
        'total_seats': 700
    },
    {
        'train_number': '12611',
        'train_name': 'Garib Rath Express',
        'source': 'Chennai Central',
        'destination': 'New Delhi',
        'departure_time': '17:30:00',
        'arrival_time': '06:30:00',
        'total_seats': 800
    },
]

for t in trains:
    Train.objects.create(**t)

print("Successfully added", len(trains), "trains!")