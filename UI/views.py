from django.shortcuts import render,redirect
from .models import Message
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse

# Create your views here.
first_val = ''
second_val = ''
third_val = ''
fourth_val = ''
fifth_val = ''
sixth_val = ''
curr_sec = 5
announcement= ['[title_val]', '"\x06\\R\\X254\\Dno\\T001', 'first_', '\\X254\\Ano\\Dno\\T002', 'second_', '\n\\X254\\Ano\\Dno\\T002', 'third_', '\n\\X254\\Ano\\Dno\\T002', 'fourth_', '\n\\X254\\Ano\\Dno\\T002', 'fifth_', '" WAIT ', 'transition_time',' SEC SIGNTYPE 0xC "\x6403" V500904 WAIT ', 'display_time', ' SEC INT "\x06\x05\\J\\"']

def home(request):
	context = {
		'message':Message.objects.all()
	}
	return render(request, 'UI/UI.html', context)

def about(request):
	return render(request,'UI/about.html')


class MessageListView(ListView):
	model = Message
	template_name = 'UI/UI.html'
	context_object_name = 'message'
	ordering = ['-id']

class MessageDetailView(DetailView):
	model = Message


def create_message(request):
	if request.method == 'POST':
		title= request.POST.get('title')
		line = request.POST.get('line')
		scroll = request.POST.get('scroll')
		flash = request.POST.get('flash')
		transition_time = request.POST.get('transition_time')
		display_time = request.POST.get('display_time')

		print("Line:", line)
		print("Scroll:", scroll)
		print("Flash:", flash)
		print("Transition Time:", transition_time)
		print("Display_time:", display_time)

		if not transition_time.isdigit():
			return render(request, 'UI/UI.html')

		#create new message
		new_message = Message(
			title=title,
			line=line,
			transition_time= int(transition_time),
			display_time = int(display_time),
			scroll=scroll,
			flash=flash,
			#date_posted = date_posted,
			)

		#modify the announcement
		first_val = title
		temp = line
		words = []
		for i in range(5):
			words.append(temp[:17])
			temp = temp[17:]

		second_val = words[0]
		if len(words) >0:
			third_val = words[1]
		if len(words) > 1:
			fourth_val = words[2]
		if len(words) > 2:
			fifth_val = words[3]
		if len(words) > 3:
			sixth_val = words[4]


		print("new-line ", new_message.line)
		new_message.save()
		return redirect('main-home')
		#return render(request,'UI/UI.html')

	return render(request, 'UI/UI.html')


def delete_message(request, message_id):
	try:
		message = Message.objects.get(pk=message.id)
		message.delete()
		return redirect('main-home')
	except Message.DoesNotExist:
		return render(request, 'error.html', {'error':'message does not exist'})


def canned_text(request):
	response = HttpResponse(content_type='text/plain')
	print(" I am the response: ", response)
	response['Content-Disposition'] = 'attachment; filename=canned.txt'

	# get one message from the model 
	messages = Message.objects.all()
	messages_list = []

	print(messages)
	for message in messages:
		print(" I am the message: ", message)
		message_data = {
			'id': message.id,
			'title': message.title,
			'line': message.line,
			#'line2': message.line2,
			#'line3': message.line3,
			#'line4':message.line4,
			#'line5': message.line5,
			#'line6': message.line6,
			#'line7': message.line7,
			'scroll': message.scroll,
			'flash': message.flash,
			'transition_time': message.transition_time,
			'display_time': message.display_time,
			'date_posted': message.date_posted.strftime('%Y-%m-%d'),
		}
		messages_list.append(message_data)

	print(messages)
	k  = 17
	lines = []
	for msg in messages_list:
		long_line = ""
		all_line = msg['line']
		for values in announcement:
			print("THE LONG LINE IS : ", long_line)
			#all_line = msg['line']
			k =17
			if values == '[title_val]':
				temp = '[' + msg['title'] + ']'
				long_line += temp
			elif values ==  'first_' or values == 'second_' or values == 'third_' or values == 'fouth_' or values == 'fifth_':
				if len(all_line) >= k:
					print(all_line[k])
					while all_line[k] != ' ':
						k -= 1
					long_line += all_line[:k]
					all_line = all_line[k:]
				else:
					long_line += all_line
					all_line = ''
			elif values == 'transition_time':
				long_line += str(msg['transition_time'])
			elif values == 'display_time':
				long_line += str(msg['display_time'])
			else:
				long_line += values
		#long_line += '\n'
		lines.append(long_line)
		#long_line = ""
	#lines = [announcement]

	response.writelines(lines)
	return response 

