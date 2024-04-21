import random as ra
import time as ti

class Slot_Mach:
    def __init__(self,amount):
        self.amount = amount
        Slot_Mach.Show(self)

    def Generate():
        return ra.choices(['a', 'b', 'c'], weights=[2, 2, 1], k=3)


    def Help():
        print(
      '\n1 - Bet on a line costs 10$ each.\n2 - Winning a line gives you 15$.\n3 - You can bet on 3 lines at max.'
      )

    def Add(self):
        add_depo = float(input('Enter the deposit amount in your account ->'))
        self.amount += add_depo
        print(f'The additional amount of {add_depo} is made to your account')

    def Show(self):
        self.n = int(input('\nEnter the Number of Lines ->'))
        cost = self.n * 10

        if self.n > 3 or self.n < 1:
            print('Invalid Entry')
            self.Show()

        else:
            if self.amount < cost:
                print('\nNot enough Amount in your Account')
                self.Add()
                
            else:
              self.amount -= cost
              self.Run()


    def Run(self):
        count = 0

        if self.n > 0 and self.n <= 3:
            for i in range(self.n):
                a, b, c = Slot_Mach.Generate()
                print(f'{a} | {b} | {c}')

                if a == b == c:
                    count += 1
                else:
                    pass

                win_am = count * 15
                self.amount += win_am
                print(f'You won {win_am}')

                while True:
                    opt = input('\nDo you want to play again? ->')

                    if opt.lower() in ['yes', 'y']:
                      self.Show()
                      
                    elif opt.lower() in ['no', 'n']:
                      print(f'\nYou got ${self.amount} in your wallet.')
                      print('Thank You for playing here , \nHave a Great Day')
                      ti.sleep(1)
                      exit()
                      
                    else:
                      print('Invalid Entry')
                      continue

    def welcome():
    
        print("Welcome to Play at Slot Machine".center(90))

        while True:
            print("\n1 - Start\n2 - Help\n3 - Exit System")
            ch = int(input('\nEnter the Choice ->'))

            if ch == 1:
                amount = float(input('Enter the Amount in Account ->'))
                Slot_Mach(amount)
                
            elif ch == 2:
                Slot_Mach.Help()
                
            elif ch == 3:
                ti.sleep(1.5)
                exit()
                
            else:
                print("Invalid Entry")
                continue
            
if __name__ == '__main__':
    Slot_Mach.welcome()
