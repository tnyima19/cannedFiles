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
announcement5= ['[title_val]', '\\x06\\R\\X254\\Dno\\','t_time1', 'first_', '\\X254\\Ano\\Dno\\', 't_time2', 'second_', '\\n\\X254\\Ano\\Dno\\','t_time3', 'third_', '\\n\\X254\\Ano\\Dno\\','t_time4', 'fourth_', '\n\\X254\\Ano\\Dno\\','t_time5', 'fifth_', ' WAIT ', 'wait_time',' SEC SIGNTYPE 0xC "\\x6403" ', 'voice_file_name', ' WAIT ', 'display_time', ' SEC INT "\\x06\x05\\J\\"']
announcement2 = ['[title_val]', '\\x06\\R\\X254\\Dno\\','t_time1', 'first_', '\\X254\\Ano\\Dno\\', 't_time2', 'second_',' WAIT ', 'wait_time',' SEC SIGNTYPE 0xC "\\x6403" ', 'voice_file_name', ' WAIT ', 'display_time', ' SEC INT "\\x06\x05\\J\\"']
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
		line1 = request.POST.get('line1')
		line2 = request.POST.get('line2')
		line3 = request.POST.get('line3')
		line4 = request.POST.get('line4')
		line5 = request.POST.get('line5')
		line6 = request.POST.get('line6')
		line7 = request.POST.get('line7')
		line8 = request.POST.get('line8')
		scroll1 = request.POST.get('scroll1')
		scroll2 = request.POST.get('scroll2')
		scroll3 = request.POST.get('scroll3')
		scroll4 = request.POST.get('scroll4')
		scroll5 = request.POST.get('scroll5')
		scroll6 = request.POST.get('scroll6')
		scroll7 = request.POST.get('scroll7')
		scroll8 = request.POST.get('scroll8')
		flash1 = request.POST.get('flash1')
		flash2 = request.POST.get('flash2')
		flash3 = request.POST.get('flash3')
		flash4 = request.POST.get('flash4')
		flash5 = request.POST.get('flash5')
		flash6 = request.POST.get('flash6')
		flash7 = request.POST.get('flash7')
		flash8 = request.POST.get('flash8')
		transition_time1 = request.POST.get('transition_time1')
		transition_time2 = request.POST.get('transition_time2')
		transition_time3 = request.POST.get('transition_time3')
		transition_time4 = request.POST.get('transition_time4')
		transition_time5 = request.POST.get('transition_time5')
		transition_time6 = request.POST.get('transition_time6')
		transition_time7 = request.POST.get('transition_time7')
		transition_time8 = request.POST.get('transition_time8')

		display_time = request.POST.get('display_time')

		#transition_times = [transition_time1, transition_time2, transition_time3, transition_time4,transition_time4, transition_time5,
		#transition_time5, transition_time6, transition_time7, transition_time8]

		#create new message
		new_message = Message(
			title=title,
			line1=line1,
			line2=line2,
			line3=line3,
			line4=line4,
			line5=line5,
			line6=line6,
			line7=line7,
			line8= line8,
			scroll1=scroll1,
			scroll2 =scroll2,
			scroll3 = scroll3,
			scroll4 = scroll4,
			scroll5 = scroll5,
			scroll6 = scroll6,
			scroll7 = scroll7,
			scroll8 = scroll8,
			flash1 = flash1 if flash1 else False,
			flash2 = flash2 if flash2 else False,
			flash3 = flash3 if flash3 else False,
			flash4 = flash4 if flash4 else False,
			flash5 = flash5 if flash5 else False,
			flash6 = flash6 if flash6 else False,
			flash7 = flash7 if flash7 else False,
			flash8 = flash8 if flash8 else False,
			transition_time1 =transition_time1,
			transition_time2 = transition_time2 if transition_time2 else 0,
			transition_time3 = transition_time3 if transition_time3 else 0,
			transition_time4 = transition_time4 if transition_time4 else 0,
			transition_time5 = transition_time5 if transition_time5 else 0,
			transition_time6 = transition_time6 if transition_time6 else 0,
			transition_time7 = transition_time7 if transition_time7 else 0,
			transition_time8 = transition_time8 if transition_time8 else 0,
			display_time = display_time,

			#date_posted = date_posted,
			)

		#modify the announcement

		print("new-line ", new_message.line1)
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
			'line1': message.line1,
			'line2': message.line2,
			'line3': message.line3,
			'line4':message.line4,
			'line5': message.line5,
			'line6': message.line6,
			'line7': message.line7,
			'scroll1': message.scroll1,
			'scroll2': message.scroll2,
			'scroll3': message.scroll3,
			'scroll4': message.scroll4,
			'scroll5': message.scroll5,
			'scroll6': message.scroll6,
			'scroll7': message.scroll7,
			'scroll8': message.scroll8,
			'flash1': message.flash1,
			'flash2': message.flash2,
			'flash3': message.flash3,
			'flash4': message.flash4,
			'flash5': message.flash5,
			'flash6': message.flash6,
			'flash7': message.flash7,
			'flash8': message.flash8,
			'transition_time1': message.transition_time1,
			'transition_time2': message.transition_time2,
			'transition_time3': message.transition_time3,
			'transition_time4': message.transition_time4,
			'transition_time5': message.transition_time5,
			'transition_time6': message.transition_time6,
			'transition_time7': message.transition_time7,
			'transition_time8': message.transition_time8,
			'display_time': message.display_time,
			'date_posted': message.date_posted.strftime('%Y-%m-%d'),
		}
		messages_list.append(message_data)

	print(messages)
	k  = 17
	lines = []
	for msg in messages_list:
		long_line = ""
		#all_line = msg['line']
		for i in range(len(announcement)):
			print("THE LONG LINE IS : ", long_line)
			#all_line = msg['line']
			k =17
			if announcement[i] == '[title_val]':
				temp = '[' + msg['title'] + ']'
				long_line += temp
			elif announcement[i] ==  'first_' or announcement[i] == 'second_' or announcement[i] == 'third_' or announcement[i] == 'fouth_' or announcement[i] == 'fifth_':
				if announcement[i] == 'first_':
					announcement[i] = msg['line1']
					long_line += announcement[i]
				elif announcement[i] == 'second_':
					announcement[i] = msg['line2']
					long_line += announcement[i]
				elif announcement[i] == 'third_':
					announcement[i] = msg['line3']
					long_line += announcement[i]
				elif announcement[i] == 'fourth_':
					announcement[i] = msg['line4']
					long_line += announcement[i]
				elif announcement[i] == 'fifth_':
					announcement[i] = msg['line5']
					long_line += announcement[i]
				elif announcement[i] == 'sixth_':
					announcement[i] = msg['line6']
					long_line += announcement[i]
				elif announcement[i] == 'seventh_':
					announcement[i] = msg['line7']
					long_line += announcement[i]
				elif announcement[i] == 'eighth_':
					announcement[i] = msg['line8']
					long_line += announcement[i]
				else:
					long_line += 'ERRROR   AT THE MOMEBNT'
			elif announcement[i] == 't_time1' or announcement[i] == 't_time2' or announcement[i] == 't_time3' or announcement[i] == 't_time4' or announcement[i] == 't_time5' or announcement[i] == 't_time6' or announcement[i] == 't_time7' or announcement[i] == 't_time8':
					if announcement[i] == 't_time1':
						announcement[i] = 'T00' + str(msg['transition_time1'])
						long_line += announcement[i]
					elif announcement[i] == 't_time2':
						announcement[i] = 'T00' + str(msg['transition_time2'])
						long_line += announcement[i]
					elif announcement[i] == 't_time3':
						announcement[i] = 'T00' + str(msg['transition_time3'])
						long_line += announcement[i]
					elif announcement[i] == 't_time4':
						announcement[i] = 'T00' + str(msg['transition_time4'])
						long_line += announcement[i]
					elif announcement[i] == 't_time5':
						announcement[i] = 'T00' +str(msg['transition_time5'])
						long_line += announcement[i]
					elif announcement[i] == 't_time6':
						announcement[i] = 'T00' +str(msg['transition_time6'])
						long_line += announcement[i]
					elif announcement[i] == 't_time7':
						announcement[i] = 'T00' +str(msg['transition_time7'])
						long_line += announcement[i]
					elif announcement[i] == 't_time8':
						announcement[i] = 'T00' +str(msg['transition_time8'])
						long_line += announcement[i]
			elif announcement[i] == 'display_time':
				announcement[i] = str(msg['display_time'])
				long_line += announcement[i]
			elif announcement[i] == 'wait_time':
				temp_wait = '5'
				long_line += temp_wait
			elif announcement[i] == 'voice_file_name':
				temp_voice_file = "VX90934"
				announcement[i] = temp_voice_file
				long_line += announcement[i]
			else:
				long_line += announcement[i]
		long_line += '\n'
		lines.append(long_line)
		#long_line = ""
	#lines = [announcement]

	response.writelines(lines)
	return response 

