from tkinter import *
import pyautogui
import pyperclip
import time

class Spam():
	def __init__(self):
		pass
	def keyboardSpam(self):
		def button():
			global times_num
			sentence = self.inputEntry.get()
			waittime = int(self.secondBox.get())
			times_num = int(self.numberBox.get())
			pyperclip.copy(sentence)
			time.sleep(waittime)
			while times_num > 0:
				pyautogui.hotkey('ctrl', 'v')
				pyautogui.press("enter")
				times_num -= 1

		global spamSpamming, sentence
		self.InputLabel = Label(text = "Write the sentence that you want to spam it!")
		self.inputEntry = Entry()
		self.numberBoxLabel = Label(text = "How many times do you want to paste it")
		self.numberBox = Spinbox(from_=1, to=100000)
		self.secondBoxLabel = Label(text = "How many seconds do you want to wait until paste it")
		self.secondBox = Spinbox(from_=0, to=100000)
		self.spaceLabel = Label(text="")
		self.button = Button(command=button, text = "Spam")
		#Keyboard Packs
		self.InputLabel.pack()
		self.inputEntry.pack()			
		self.numberBoxLabel.pack()
		self.numberBox.pack()
		self.secondBoxLabel.pack()
		self.secondBox.pack()
		self.spaceLabel.pack()
		self.button.pack()			
		self.spamSpamming = False
		try:
			self.refreshTimesLabel.pack_forget()
			self.refreshTimes.pack_forget()
			self.waitTimeRefreshLabel.pack_forget()
			self.waitTimeRefresh.pack_forget()
			self.timeBetweenRefreshLabel.pack_forget()
			self.timeBetweenRefresh.pack_forget()
			self.refreshButton.pack_forget()
		except:
			pass

		try:	
			self.clickNumLabel.pack_forget()
			self.clickNum.pack_forget()
			self.waitTimeClickLabel.pack_forget()
			self.waitTimeClick.pack_forget()
			self.betweenClickLabel.pack_forget()
			self.betweenClick.pack_forget()
			self.left.pack_forget()
			self.middle.pack_forget()
			self.right.pack_forget()
		except:
			pass

	def clickSpam(self):
		def preparing():
			global clicknum, waittime, betweenclick
			clicknum = int(self.clickNum.get())
			waittime = int(self.waitTimeClick.get())
			betweenclick = float(self.betweenClick.get())

		def left():
			preparing()
			waittime = int(self.waitTimeClick.get())
			time.sleep(waittime)
			pyautogui.click(button='left', clicks=clicknum, interval=betweenclick)

		def middle():
			preparing()
			waittime = int(self.waitTimeClick.get())
			time.sleep(waittime)
			pyautogui.click(button='middle', clicks=clicknum, interval=betweenclick)

		def right():
			preparing()
			waittime = int(self.waitTimeClick.get())
			time.sleep(waittime)
			pyautogui.click(button='right', clicks=clicknum, interval=betweenclick)

		#Deleting Widgets
		try:
			self.refreshTimesLabel.pack_forget()
			self.refreshTimes.pack_forget()
			self.waitTimeRefreshLabel.pack_forget()
			self.waitTimeRefresh.pack_forget()
			self.timeBetweenRefreshLabel.pack_forget()
			self.timeBetweenRefresh.pack_forget()
			self.refreshButton.pack_forget()
		except:
			pass
		try:
			self.InputLabel.pack_forget()
			self.inputEntry.pack_forget()
			self.numberBoxLabel.pack_forget()
			self.numberBox.pack_forget()
			self.secondBoxLabel.pack_forget()
			self.secondBox.pack_forget()
			self.spaceLabel.pack_forget()
			self.button.pack_forget()	
		except:
			pass
		#Click Widgets
		self.clickNumLabel = Label(text="How many times do you want to do click spam?")
		self.clickNum = Spinbox(from_=0, to=100000)
		self.waitTimeClickLabel = Label(text = "How many seconds do you want to wait until spam it?")
		self.waitTimeClick = Spinbox(from_=0, to=100000)
		self.betweenClickLabel = Label(text="How many second will pass between clicks?")
		self.betweenClick = Entry()
		self.left = Button(text="Left Click Spam", command = left)
		self.middle = Button(text="Middle Click Spam", command = middle)
		self.right = Button(text="Right Click Spam", command = right)
		#Packing Them
		self.clickNumLabel.pack()
		self.clickNum.pack()
		self.waitTimeClickLabel.pack()
		self.waitTimeClick.pack()
		self.betweenClickLabel.pack()
		self.betweenClick.pack()
		self.left.pack(side=LEFT)
		self.middle.pack(side=LEFT)
		self.right.pack(side=LEFT)

	def refreshSpam(self):
		def refreshDef():
			waitTimeRefreshValue = int(self.waitTimeRefresh.get())
			refreshTimesValue = int(self.refreshTimes.get())
			betweenRefresh = int(self.timeBetweenRefresh.get())
			time.sleep(waitTimeRefreshValue)
			while refreshTimesValue > 0:
				time.sleep(betweenRefresh)
				pyautogui.press('f5')
				refreshTimesValue -= 1

		try:
			self.clickNumLabel.pack_forget()
			self.clickNum.pack_forget()
			self.waitTimeClickLabel.pack_forget()
			self.waitTimeClick.pack_forget()
			self.betweenClickLabel.pack_forget()
			self.betweenClick.pack_forget()
			self.left.pack_forget()
			self.middle.pack_forget()
			self.right.pack_forget()
		except:
			pass

		try:
			self.InputLabel.pack_forget()
			self.inputEntry.pack_forget()
			self.numberBoxLabel.pack_forget()
			self.numberBox.pack_forget()
			self.secondBoxLabel.pack_forget()
			self.secondBox.pack_forget()
			self.spaceLabel.pack_forget()
			self.button.pack_forget()
		except:
			pass
		
		self.refreshTimesLabel = Label(text="How many times do you want to refresh the page?")
		self.refreshTimes = Spinbox(from_=1, to=100000)
		self.waitTimeRefreshLabel = Label(text="How many seconds do you want to wait until spam it?")
		self.timeBetweenRefreshLabel = Label(text = "How much do you want to wait between refreshes?")
		self.timeBetweenRefresh = Spinbox(from_=0, to=100000)
		self.waitTimeRefresh = Spinbox(from_=0, to=100000)
		self.refreshButton = Button(command = refreshDef, text="Refresh Spam")
		#Packing
		self.refreshTimesLabel.pack()
		self.refreshTimes.pack()
		self.waitTimeRefreshLabel.pack()
		self.waitTimeRefresh.pack()
		self.timeBetweenRefreshLabel.pack()
		self.timeBetweenRefresh.pack()
		self.refreshButton.pack()

		