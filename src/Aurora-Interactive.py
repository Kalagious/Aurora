import Aurora
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

HISTORY_LEN = 15
history = []


ASCIITITLE = [
"    ___                              ",
"   /   | __  ___________  _________ _",
"  / /| |/ / / / ___/ __ \/ ___/ __ `/",
" / ___ / /_/ / /  / /_/ / /  / /_/ /",
"/_/  |_\__,_/_/   \____/_/   \__,_/"]


def addHistory(text, inHistory):
	if len(inHistory) == HISTORY_LEN-2:
		inHistory.pop(0)
	inHistory.append(text)



def formPrompt(promptWin, height):

	prompt = ""
	if Aurora.target.name:
		promptWin.addstr(0, len(prompt), "["+Aurora.target.name+"]", curses.color_pair(1))
		prompt += "["+Aurora.target.name+"]"

	else:
		promptWin.addstr(0, len(prompt), "[Aurora]", curses.color_pair(1))
		prompt += "[Aurora]"

	promptWin.addstr(0, len(prompt), "=>", curses.color_pair(1))
	prompt += "=>"

	promptWin.refresh()
	return curses.newwin(1, 30, height-2, len(prompt))


def processCommand(command, historyWin):
	parts = command.split(" ")

	if not parts[0]:
		return

	match parts[0]:
		case "cd":
			if (len(parts) != 2):
				historyWin.addstr(HISTORY_LEN-1, 0, " [!] cd requires 1 parameter.".format(parts[1]), curses.color_pair(2))
			else:
				items = Aurora.getByNames(parts[1])
				for item in items:
					history.append(item.name)
				if not Aurora.target.name:
					Aurora.loadTargetByName(parts[1])
					history.append(parts[1])
					if not Aurora.target.name:
						historyWin.addstr(HISTORY_LEN-1, 0, " [!] A target has not been selected.".format(parts[1]), curses.color_pair(2))
				elif not len(items):
					historyWin.addstr(HISTORY_LEN-1, 0, " [!] {} not found!".format(parts[1]), curses.color_pair(2))

		case "new":
			print("Tmp")

		case "ls":
			print("Tmp")

		case "clear":
			history.clear()

		case _:
			historyWin.addstr(HISTORY_LEN-1, 0, " [!] Command {} not found!".format(parts[0]), curses.color_pair(2))





def updateObjects(objectWin):
	i = 0
	if not Aurora.target.name:
		objectWin.addstr(1, 25, " [!] Target not selected.", curses.color_pair(2))

		for target in Aurora.getTargets():
			#CONTINUE




def main(stdscr):
	height,width = stdscr.getmaxyx()

	Aurora.loadConfig()
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

	
	title = curses.newwin(10, 45, 0, int(width/2)-22)
	for i in range(0,len(ASCIITITLE)):
		title.addstr(1+i, 2, ASCIITITLE[i], curses.color_pair(1))
	rectangle(title, 0, 0 , 7, 40)

	
	history.append(Aurora.target.name)
	promptWin = curses.newwin(1, width, height-2, 0)
	objectWin = curses.newwin(15, 80, int(height/2)-15, int(width/2)-40)

	historyWin = curses.newwin(HISTORY_LEN, width, height-2-HISTORY_LEN, 0)
	stdscr.refresh()
	objectWin.refresh()
	title.refresh()

	while True:
		rectangle(objectWin, 0, 0, 14, 78)

		editWin = formPrompt(promptWin, height)
		inputBox = Textbox(editWin)
		inputBox.edit()

		userInput = inputBox.gather()

		if len(userInput) != 0 and userInput.lower().rstrip() in "exit":
			break

		processCommand(userInput.rstrip(), historyWin)
		addHistory(userInput, history)

		updateObjects(objectWin)

		for i in range(0, len(history)):
			historyWin.addstr(HISTORY_LEN-2-i, 0, history[len(history)-i-1])
		

		promptWin.clear()
		historyWin.clear()
		historyWin.refresh()
		objectWin.refresh()



wrapper(main)

   
