from random import randint
from time import sleep
import os



def action(Action_card=0,player=4,low_hp_player=1):
	for action in range(0,Action_card):
		Aseed = randint(0,999999)
		Aplayer = randint(Aseed%10,Aseed*9876)
		print("\n********LÁ BÀI %d ********"%(action+1))
		if(low_hp_action() == True):
			print("Sử dụng lên player: " + str(low_hp_player) + "\n")
		elif((Aseed % 10)+1 < 1):
			print("Không sử dụng\n")
		else:
			print("Sử dụng lên player: " + str(Aplayer%player+1))



def low_hp_target(so_player):
	target = 1
	str_hp_player=input("Nhap số máu từng Player (cách bởi dấu cách): ").split()
	lst_hp_player=list(map(int,str_hp_player))

	#Tìm vị trí player số máu thấp nhất
	smallest_hp = lst_hp_player[0]

	for i in range(0,len(lst_hp_player)):
		if lst_hp_player[i] < smallest_hp:
			smallest_hp = lst_hp_player[i]
			target = i+1
	return target

def low_hp_action():
	l_hp_seed = randint(1,9999) * randint(1,9999)
	l_hp_seed_lst = [randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
	if (l_hp_seed % 10)+1 in l_hp_seed_lst:
		return True
	else:
		return False


def game_run(): #main
	game_loop = True #Sửa thành True để chạy game
	while game_loop:
		os.system('cls')
		p = int(input("Nhập số player: "))
		if p == 0: break
		ac = int(input("Nhập số lá bài có thể sử dụng: "))
		lhp = low_hp_target(p)
		wait_str = ".....\n"
		print("Calculating",end="")
		for c in wait_str:
			print(c,end ='',flush=True)
			sleep(0.7)

		action(ac,p,lhp)
		c = input("Nhấn Enter để tiếp tục")
game_run()
