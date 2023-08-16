from django.shortcuts import render,redirect
from django.core.mail import send_mail


def home(request):
	return render(request, 'home.html')
	


def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_subject = request.POST['message-subject']
		message = request.POST['message']
		

		send_mail(
			message_subject, # subject
			message, # message	
			message_name, # from sender							
			['johnitezmwas9@gmail.com'], # To Email
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})


def about(request):
	return render(request, 'about.html', {})



def service(request):
	return render(request, 'service.html', {})


def price(request):
	return render(request, 'price.html', {})


def team(request):
	return render(request, 'team.html', {})


def testimonial(request):
	return render(request, 'testimonial.html', {})


def appointment(request):
	
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_phone = request.POST['your-phone']
		your_time = request.POST['your-time']
		your_date = request.POST['your-date']


		# Send an email
		appointment = " Name: " + your_name + "\n" + " Phone: " + your_phone + "\n" + " Email: " + your_email + "\n" + " Date: " + your_date + "\n" + " Time: " + your_time



		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email,	# from email
			['johnitezmwas9gmail.com'], # To Email
			)

		return render(request, 'appointment2.html', {
		   'your_name': your_name,
		   'your_phone': your_phone,
		   'your_email': your_email,
		   'your_date': your_date,
		   'your_time': your_time,
			})

	else:
		return render(request, 'appointment.html', {})