from django.shortcuts import render,redirect
from .models import Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

# Create your views here.
first_val = ''
second_val = ''
third_val = ''
fourth_val = ''
fifth_val = ''
sixth_val = ''
curr_sec = 5

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

class MessageDeleteView(DeleteView):
	model = Message
	success_url = '/'


class MessageCreateView(CreateView):
	model = Message
	fields = ['title', 'line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7', 'line8',
	'scroll1','scroll2','scroll3','scroll4','scroll5', 'scroll6','scroll7','scroll8','flash1',
	'flash2','flash3','flash4','flash6','flash7','flash8','transition_time1',
	'transition_time2','transition_time3','transition_time4','transition_time5',
	'transition_time6', 'transition_time7','transition_time8','display_time']


class MessageUpdateView(UpdateView):
	model = Message
	fields = ['title', 'line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7', 'line8',
	'scroll1','scroll2','scroll3','scroll4','scroll5', 'scroll6','scroll7','scroll8','flash1',
	'flash2','flash3','flash4','flash6','flash7','flash8','transition_time1',
	'transition_time2','transition_time3','transition_time4','transition_time5',
	'transition_time6', 'transition_time7','transition_time8','display_time']


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
		line9 = request.POST.get('line9')
		line10 = request.POST.get('line10')
		scroll1 = request.POST.get('scroll1')
		scroll2 = request.POST.get('scroll2')
		scroll3 = request.POST.get('scroll3')
		scroll4 = request.POST.get('scroll4')
		scroll5 = request.POST.get('scroll5')
		scroll6 = request.POST.get('scroll6')
		scroll7 = request.POST.get('scroll7')
		scroll8 = request.POST.get('scroll8')
		scroll9 = request.POST.get('scroll9')
		scroll10 = request.POST.get('scroll10')
		flash1 = request.POST.get('flash1')
		flash2 = request.POST.get('flash2')
		flash3 = request.POST.get('flash3')
		flash4 = request.POST.get('flash4')
		flash5 = request.POST.get('flash5')
		flash6 = request.POST.get('flash6')
		flash7 = request.POST.get('flash7')
		flash8 = request.POST.get('flash8')
		flash9 = request.POST.get('flash9')
		flash10 = request.POST.get('flash10')
		transition_time1 = request.POST.get('transition_time1')
		transition_time2 = request.POST.get('transition_time2')
		transition_time3 = request.POST.get('transition_time3')
		transition_time4 = request.POST.get('transition_time4')
		transition_time5 = request.POST.get('transition_time5')
		transition_time6 = request.POST.get('transition_time6')
		transition_time7 = request.POST.get('transition_time7')
		transition_time8 = request.POST.get('transition_time8')
		transition_time9 = request.POST.get('transition_time9')
		transition_time10 = request.POST.get('transition_time10')

		display_time = request.POST.get('display_time')

		#transition_times = [transition_time1, transition_time2, transition_time3, transition_time4,transition_time4, transition_time5,
		#transition_time5, transition_time6, transition_time7, transition_time8]

		#create new message
		new_message = Message(
			title=title,
			line1=line1.upper() if line1 else line1,
			line2=line2.upper() if line2 else line2,
			line3=line3.upper() if line3 else line3,
			line4=line4.upper() if line4 else line4,
			line5=line5.upper() if line5 else line5,
			line6=line6.upper() if line6 else line6,
			line7=line7.upper() if line7 else line7,
			line8= line8.upper() if line8 else line8,
			line9=line9.upper() if line9 else line9,
			line10=line10.upper() if line10 else line10,
			scroll1=scroll1,
			scroll2 =scroll2,
			scroll3 = scroll3,
			scroll4 = scroll4,
			scroll5 = scroll5,
			scroll6 = scroll6,
			scroll7 = scroll7,
			scroll8 = scroll8,
			scroll9= scroll9,
			scroll10= scroll10,
			flash1 = flash1 if flash1 else False,
			flash2 = flash2 if flash2 else False,
			flash3 = flash3 if flash3 else False,
			flash4 = flash4 if flash4 else False,
			flash5 = flash5 if flash5 else False,
			flash6 = flash6 if flash6 else False,
			flash7 = flash7 if flash7 else False,
			flash8 = flash8 if flash8 else False,
			flash9 = flash9 if flash9 else False,
			flash10 = flash10 if flash10 else False,
			transition_time1 =transition_time1 if transition_time2 else 2,
			transition_time2 = transition_time2 if transition_time2 else 2,
			transition_time3 = transition_time3 if transition_time3 else 2,
			transition_time4 = transition_time4 if transition_time4 else 2,
			transition_time5 = transition_time5 if transition_time5 else 2,
			transition_time6 = transition_time6 if transition_time6 else 2,
			transition_time7 = transition_time7 if transition_time7 else 2,
			transition_time8 = transition_time8 if transition_time8 else 2,
			transition_time9 = transition_time9 if transition_time9 else 2,
			transition_time10 = transition_time10 if transition_time10 else 2,
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

	
	announcement5= ['[title_val]', '\\x06\\R\\X254\\Dno\\','t_time1', 'first_', '\\X254\\Ano\\Dno\\', 't_time2', 'second_', '\\n\\X254\\Ano\\Dno\\','t_time3', 'third_', '\\n\\X254\\Ano\\Dno\\','t_time4', 'fourth_', '\n\\X254\\Ano\\Dno\\','t_time5', 'fifth_', ' WAIT ', 'wait_time',' SEC SIGNTYPE 0xC "\\x6403" ', 'voice_file_name', ' WAIT ', 'display_time', ' SEC INT "\\x06\x05\\J\\"']
	announcement2 = ['[title_val]', '\\x06\\R\\X254\\Dno\\','t_time1', 'first_', '\\X254\\Ano\\Dno\\', 't_time2', 'second_',' WAIT ', 'wait_time',' SEC SIGNTYPE 0xC "\\x6403" ', 'voice_file_name', ' WAIT ', 'display_time', ' SEC INT "\\x06\x05\\J\\"']
	response = HttpResponse(content_type='text/plain')
	print(" I am the response: ", response)
	response['Content-Disposition'] = 'attachment; filename=canned.rte'

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
			'line8':message.line8,
			'line9':message.line9,
			'line10':message.line10,
			'scroll1': message.scroll1,
			'scroll2': message.scroll2,
			'scroll3': message.scroll3,
			'scroll4': message.scroll4,
			'scroll5': message.scroll5,
			'scroll6': message.scroll6,
			'scroll7': message.scroll7,
			'scroll8': message.scroll8,
			'scroll9':message.scroll9,
			'scroll10':message.scroll10,
			'flash1': message.flash1,
			'flash2': message.flash2,
			'flash3': message.flash3,
			'flash4': message.flash4,
			'flash5': message.flash5,
			'flash6': message.flash6,
			'flash7': message.flash7,
			'flash8': message.flash8,
			'flash9':message.flash9,
			'flash10':message.flash10,
			'transition_time1': message.transition_time1,
			'transition_time2': message.transition_time2,
			'transition_time3': message.transition_time3,
			'transition_time4': message.transition_time4,
			'transition_time5': message.transition_time5,
			'transition_time6': message.transition_time6,
			'transition_time7': message.transition_time7,
			'transition_time8': message.transition_time8,
			'transition_time9':message.transition_time9,
			'transition_time10':message.transition_time10,
			'display_time': message.display_time,
			'voice_file_name': message.voice_file_name,
			'date_posted': message.date_posted.strftime('%Y-%m-%d'),
		}
		messages_list.append(message_data)

	print(messages)
	k  = 17
	lines = []
	# for msg in messages_list:
	# 	long_line = ""
	# 	temp_ann = announcement5
	# 	print("THis is THE CURRENT MESSAGE: " ,msg)
	# 	#all_line = msg['line']
	# 	for i in range(len(temp_ann)):
	# 		print("THE LONG LINE IS : ", long_line)
	# 		#all_line = msg['line']
	# 		k =17
	# 		if temp_ann[i] == '[title_val]':
	# 			temp = '[' + msg['title'] + ']'
	# 			long_line += temp
	# 		elif temp_ann[i] ==  'first_' or temp_ann[i] == 'second_' or temp_ann[i] == 'third_' or temp_ann[i] == 'fouth_' or temp_ann[i] == 'fifth_':
	# 			if temp_ann[i] == 'first_':
	# 				#temp_ann[i] = msg['line1']
	# 				long_line += msg['line1']
	# 			elif temp_ann[i] == 'second_':
	# 				#temp_ann[i] = msg['line2']
	# 				long_line += msg['line2']
	# 			elif temp_ann[i] == 'third_':
	# 				#temp_ann[i] = msg['line3']
	# 				long_line += msg['line3']
	# 			elif temp_ann[i] == 'fourth_':
	# 				#temp_ann[i] = msg['line4']
	# 				long_line += msg['line4']
	# 			elif temp_ann[i] == 'fifth_':
	# 				#temp_ann[i] = msg['line5']
	# 				long_line += msg['line5']
	# 			elif temp_ann[i] == 'sixth_':
	# 				#temp_ann[i] = msg['line6']
	# 				long_line += msg['line6']
	# 			elif temp_ann[i] == 'seventh_':
	# 				#temp_ann[i] = msg['line7']
	# 				long_line += msg['line7']
	# 			elif temp_ann[i] == 'eighth_':
	# 				#temp_ann[i] = msg['line8']
	# 				long_line += msg['line8']
	# 			else:
	# 				long_line += 'ERRROR   AT THE MOMEBNT'
	# 		elif temp_ann[i] == 't_time1' or temp_ann[i] == 't_time2' or temp_ann[i] == 't_time3' or temp_ann[i] == 't_time4' or temp_ann[i] == 't_time5' or temp_ann[i] == 't_time6' or temp_ann[i] == 't_time7' or temp_ann[i] == 't_time8':
	# 				if temp_ann[i] == 't_time1':
	# 					#temp_ann[i] = 'T00' + str(msg['transition_time1'])
	# 					long_line += 'T00' + str(msg['transition_time1'])
	# 				elif temp_ann[i] == 't_time2':
	# 					#temp_ann[i] = 'T00' + str(msg['transition_time2'])
	# 					long_line += 'T00' + str(msg['transition_time2'])
	# 				elif temp_ann[i] == 't_time3':
	# 					#temp_ann[i] = 'T00' + str(msg['transition_time3'])
	# 					long_line += 'T00' + str(msg['transition_time3'])
	# 				elif temp_ann[i] == 't_time4':
	# 					#temp_ann[i] = 'T00' + str(msg['transition_time4'])
	# 					long_line += 'T00' + str(msg['transition_time4'])
	# 				elif temp_ann[i] == 't_time5':
	# 					#temp_ann[i] = 'T00' +str(msg['transition_time5'])
	# 					long_line +=  'T00' +str(msg['transition_time5'])
	# 				elif temp_ann[i] == 't_time6':
	# 					#temp_ann[i] = 'T00' +str(msg['transition_time6'])
	# 					long_line += 'T00' +str(msg['transition_time6'])
	# 				elif temp_ann[i] == 't_time7':
	# 					#temp_ann[i] = 'T00' +str(msg['transition_time7'])
	# 					long_line += 'T00' +str(msg['transition_time7'])
	# 				elif temp_ann[i] == 't_time8':
	# 					#temp_ann[i] = 'T00' +str(msg['transition_time8'])
	# 					long_line += 'T00' +str(msg['transition_time8'])
	# 		elif temp_ann[i] == 'display_time':
	# 			#temp_ann[i] = str(msg['display_time'])
	# 			long_line += str(msg['display_time'])
	# 		elif temp_ann[i] == 'wait_time':
	# 			temp_wait = '5'
	# 			long_line += temp_wait
	# 		elif temp_ann[i] == 'voice_file_name':
	# 			#temp_voice_file = msg['voice_file_name']
	# 			#temp_ann[i] = msg['voice_file_name']
	# 			long_line += msg['voice_file_name']
	# 		else:
	# 			long_line += temp_ann[i]
	# 	long_line += '\n'
	# 	lines.append(long_line)
	# 	#long_line = ""
	# #lines = [announcement]

	dictionary = {'flash_true':'\\E',
					'flash_false':'\\G',
					'Intensity_1' : '1',
					'Intensity_2' : '2',
					'Intensity_3' : '3',
					'Intensity_4' : '4',
					'Intensity_5' :  '5',
					'Repeat_off':'R',
					'duration': 'T',
					'appear':'\\Ano',
					'app_right_to_left':'\\Ahs',
					'app_bottom_to_top':'\\Avb',
					'app_top_to_bottom':'\\Avt',
					'app_replace_exiting_msg':'\\Ano',
					'dis_clear_msg':'Dno',
					'dis_right_to_left':'\\Dhs',
					'dis_bottom_to_top':'\\Dvb',
					'disappear':'\\Dno',
					'Scrolling_speed':'S',
					'position_center':'\\X254',
					'position_left':'X253',
					'position_right':'255',
					'flash_on_time':'\\M',
					'flash_off_time':'\\N',
					'time':'H',
					'auto_trigger':'J'
					}

	arr = ['title','const_1','scroll_d1','duration1','line1',
	         'const_2','flash2','scroll_a2','scroll_d2','duration2','line2',
	         'const_3','flash3','scroll_a3','scroll_d3','duration3','line3',
	         'const_4','flash4','scroll_a4','scroll_d4','duration4','line4',
	         'const_5','flash5','scroll_a5','scroll_d5','duration5','line5',
	         'const_6','flash6','scroll_a6','scroll_d6','duration6','line6',
	         'const_7','flash7','scroll_a7','scroll_d7','duration7','line7',
	         'const_8','flash8','scroll_a8','scroll_d8','duration8','line8',
	         'const_9','flash9','scroll_a9','scroll_d9','duration9','line9']

	arr2 = ['wait_time','voice_file_name','display_time']
	const_f = '"\\x06\\R\\X254'
	const_s = '\\n\\X254'
	for msg in messages_list:
		long_line = ""
		for i in arr:
			if i == 'title':
				temp = '[' + msg['title'] + '] '
				long_line += temp
			elif i == 'const_1':
				if msg['line1'] == '':
					long_line += '"'
					break
				temp = const_f
				long_line += temp
			elif i == 'flash1':
				if msg['flash1'] == True:
					temp = dictionary['flash_true']
					long_line += temp
				
			elif i == 'scroll_d1':
				if msg['scroll1'] == 'horizontal':
					temp = dictionary['dis_left_to_right']
				elif msg['scroll2'] == 'vertical':
					temp = dictionary['dis_top_to_bottom']
				else:
					temp = dictionary['disappear']
				long_line += temp
			elif i == 'duration1':
				if msg['transition_time1'] <= 9:
					temp = '\\T00' + str(msg['transition_time1'])
				else:
					temp =  '\\T0' + str(msg['transition_time1'])
				long_line += temp
			elif i =='line1':
				if msg['line1'] == '':
					break
				temp = msg['line1']
				long_line += temp
			elif i == 'const_2':
				if msg['line2'] == '':
					long_line += '"'
					break
				temp = const_s
				long_line += temp
			elif i == 'flash2':
				if msg['flash2'] == True:
					temp = dictionary['flash_true']
					long_line += temp
			elif i == 'scroll_a2':
				if msg['scroll2'] == 'horizontal':
					temp = dictionary['app_right_to_left']
				elif msg['scroll2'] == 'vertical':
					temp = dictionary['app_top_to_bottom']
				else:
					temp = dictionary['appear']
				long_line += temp
			elif i == 'scroll_d2':
				if msg['scroll2'] == 'horizontal':
					temp = dictionary['dis_left_to_right']
				elif msg['scroll2'] == 'vertical':
					temp = dictionary['dis_top_to_bottom']
				else:
					temp = dictionary['disappear']
				long_line += temp
			elif i == 'duration2':
				if msg['transition_time2'] <= 9:
					temp = '\\T00' + str(msg['transition_time2'])
				else:
					temp = '\\T0' + str(msg['transition_time2'])
				long_line += temp
			elif i == 'line2':
				if msg['line2'] == '':
					break
				temp = msg['line2']
				long_line += temp
			elif i == 'const_3':
				if msg['line3'] == '':
					long_line += '"'
					break
				temp = const_s
				long_line += temp
			elif i == 'flash3':
				if msg['flash3'] == True:
					temp = dictionary['flash_true']
					long_line += temp
			elif i == 'scroll_a3':
				if msg['scroll3'] == 'horizontal':
					temp = dictionary['app_right_to_left']
				elif msg['scroll3'] == 'vertical':
					temp = dictionary['app_top_to_bottom']
				else:
					temp = dictionary['appear']
				long_line += temp
			elif i == 'scroll_d3':
				if msg['scroll3'] == 'horizontal':
					temp = dictionary['dis_left_to_right']
				elif msg['scroll3'] == 'vertical':
					temp = dictionary['dis_top_to_bottom']
				else:
					temp = dictionary['disappear']
				long_line += temp
			elif i == 'duration3':
				if not msg['transition_time3']:
					break
				if msg['transition_time3'] <= 9:
					temp = '\\T00' + str(msg['transition_time3'])
				else:
					temp = '\\T0' + str(msg['transition_time3'])
				long_line += temp
			elif i == 'line3':
				if msg['line3'] == '':
					break
				temp = msg['line3']
				long_line += temp
			elif i == 'const_4':
				if msg['line4'] == '':
					long_line += '"'
					break
				temp = const_s
				long_line += temp
			elif i == 'flash4':
				if msg['flash4'] == True:
					temp = dictionary['flash_true']
					long_line += temp
			elif i == 'scroll_a4':
				temp = ""
				if msg['scroll4'] == 'horizontal':
					temp = dictionary['left_to_right']
				elif msg['scroll4'] == 'vertical':
					temp = dicationary['top_to_bottom']
				else:
					temp = dictionary['appear']
				long_line += temp
			elif i == 'scroll_d4':
				if msg['scroll4'] == 'horizontal':
					temp = dictionary['left_to_right']
				elif msg['scroll4'] == 'vertical':
					temp = dictionary['top_to_bottom']
				else:
					temp = dictionary['disappear']
				long_line += temp
			elif i == 'duration4':
				if msg['transition_time4'] < 9:
					temp = '\\T00' + str(msg['transition_time4'])
				else:
					temp = '\\T0' + str(msg['transition_time4'])
				long_line += temp
			elif i == 'line4':
				if msg['line4'] == '':
					break
				temp = msg['line4']
				long_line += temp
			elif i == 'const_5':
				if msg['line5'] == '':
					long_line += '"'
					break
				temp = const_s
				long_line += temp
			elif i == 'flash5':
				if msg['flash5'] == True:
					temp = dictionary['flash_true']
					long_line += temp
			elif i == 'scroll_a5':
				if msg['scroll5'] == 'horizontal':
					temp = dictionary['app_left_to_right']
				elif msg['scroll5'] == 'vertical':
					temp = dictionary['app_top_to_bottom']
				else:
					temp = dictionary['appear']
				long_line += temp
			elif i == 'scroll_d5':
				if msg['scroll5'] == 'horizontal':
					temp = dictionary['dis_left_to_right']
				elif msg['scroll5'] == 'vertical':
					temp = dictionary['dis_top_to_bottom']
				else:
					temp = dictionary['disappear']
				long_line += temp
			elif i == 'duration5':
				if msg['transition_time5']  < 9:
					temp = '\\T00' + str(msg['transition_time5'])
				else:
					temp = '\\T0' + str(msg['transition_time5'])
				long_line += temp
			elif i == 'line5':
				if msg['line5'] == '':
					break
				temp = msg['line5']
				long_line += temp
			elif i == 'const_6':
				if msg['line6'] == '':
					long_line += '"'
					break
				temp = const_s
				long_line += temp
			elif i == 'flash6':
				if msg['flash6'] == True:
					temp = dictionary['flash_true']
					long_line += temp
			elif i == 'scroll_a6':
				if msg['scroll5'] == 'horizontal':
					temp = dictionary['app_left_to_right']
				elif msg['scroll5'] == 'vertical':
					temp = dictionary['app_top_to_bottom']
				else:
					temp = dictionary['appear']
				long_line += temp
			elif i == 'scroll_d6':
				if msg['scroll5'] == 'horizontal':
					temp = dictionary['dis_left_to_right']
				elif msg['scroll6'] == 'vertical':
					temp = dicationary['dis_top_to_bottom']
				else:
					temp = dictionary['disappear']
				long_line += temp
			elif i == 'duration6':
				if msg['transition_time6'] < 9:
					temp = '\\T00' + str(msg['transition_time6'])
				else:
					temp = '\\T0' + str(msg['transition_time6'])
				long_line += temp
			elif i == 'line6':
				if msg['line6'] == '':
					break
				temp = msg['line6']
				long_line += temp
			elif i == 'const_7':
				if msg['line7'] == '':
					long_line += '"'
					break
				temp = const_s
				long_line += temp
			elif i == 'flash7':
				if msg['flash7'] == True:
					temp = dictionary['flash_true']
					long_line += temp
			elif i == 'scroll_a7':
				if msg['scroll7'] == 'horizontal':
					temp = dictionary['app_left_to_right']
				elif msg['scroll7'] == 'vertical':
					temp = dictionary['app_top_to_bottom']
				else:
					temp = dictionary['appear']
				long_line += temp
			elif i == 'scroll_d7':
				if msg['scroll7'] =='horizontal':
					temp = dictionary['dis_left_to_right']
				elif msg['scroll7'] == 'vertical':
					temp = dictionary['dis_top_to_bottom']
				else:
					temp = dictionary['disappear']
				long_line += temp
			elif i == 'duration7':
				if not msg['transition_time7']:
					break
				if msg['transition_time7'] < 9:
					temp = '\\T00' + str(msg['transition_time7'])
				else:
					temp = '\\T0' + str(msg['transition_time7'])
				long_line += temp
			elif i == 'line7':
				if msg['line7'] == '':
					break
				temp = msg['line7']
				long_line += temp
			elif i == 'const_8':
				if msg['line8'] == '':
					long_line += '"'
					break
				temp = const_s
				long_line += temp
			elif i == 'flash8':
				if msg['flash8'] == True:
					temp = dictionary['flash_true']
					long_line += temp
			elif i == 'scroll_a8':
				if msg['scroll8'] == 'horizontal':
					temp = dictionary['app_left_to_right']
				elif msg['scroll8'] == 'vertical':
					temp = dictionary['app_top_to_bottom']
				else:
					temp = dictionary['appear']
				long_line += temp
			elif i == 'scroll_d8':
				if msg['scroll8'] == '':
					break
				if msg['scroll8'] == 'horizontal':
					temp = dictionary['dis_left_to_right']
				elif msg['scroll8'] == 'vertical':
					temp = dicationary['dis_top_to_bottom']
				else:
					temp = dictionary['disappear']
				long_line += temp
			elif i == 'duration8':
				if not msg['transition_time8']:
					break
				if msg['transition_time8'] < 9:
					temp = '\\T00' + str(msg['transition_time8'])
				else:
					temp = '\\T0' + str(msg['transition_time8'])
				long_line += temp
			elif i == 'line8':
				if msg['line8'] == '':
					break
				temp = msg['line8']
				long_line += temp
			elif i == 'const_9':
				if msg['line9'] == '':
					long_line += '"'
					break
				temp = const_s
				long_line += temp
			elif i == 'flash9':
				if msg['flash9'] == True:
					temp = dictionary['flash_true']
					long_line += temp
			elif i == 'scroll_a9':
				if msg['scroll9'] == 'horizontal':
					temp = dictionary['app_left_to_right']
				elif msg['scroll9'] == 'vertical':
					temp = dictionary['app_top_to_bottom']
				else:
					temp = dictionary['appear']
				long_line += temp
			elif i == 'scroll_d9':
				if msg['scroll9'] == 'horizontal':
					temp = dictionary['dis_left_to_right']
				elif msg['scroll9'] == 'vertical':
					temp = dictionary['dis_top_to_bottom']
				else:
					temp = dicationary['disappear']
				long_line += temp
			elif i == 'duration9':
				if not msg['transition_time9']:
					break
				if msg['transition_time9']  <= 9:
					temp = '\\T00' + str(msg['transition_time9'])
				else:
					temp = '\\T0' + str(msg['transition_time9'])
			elif i == 'line9':
				if msg['line9'] == '':
					break
				temp = msg['line9']
				long_line += temp

		for j in arr2:
			if j == 'wait_time':
				temp = ' WAIT 5 SEC SIGNTYPE 0xC "\\x6403" '
				long_line += temp
			elif j == 'voice_file_name':
				temp = msg['voice_file_name']
				long_line += temp
			elif j == 'display_time':
				temp = ' WAIT '+ str(msg['display_time'])+' SEC INT "\\x06\\x05\\J"'
				long_line += temp
		long_line += '\r\n'
		lines.append(long_line)


	response.writelines(lines)
	return response 

