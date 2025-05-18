#practicing my coding using boolean operators :)
#POV = a roll coaster needs a new entry system with the height requirement is 137cm and the cost of a ticket is 10 credits 
#learning with Codedex :) 

height = int(input('How tall are you in cm?:'))
credits = int(input('How many credits do you have?:'))

if height >= 137 and credits >= 10:
  print('Enjoy the Ride! :)')
elif height < 137 and credits >= 10:
  print('You are not tall enough to ride, short king :(')
elif height >= 137 and credits < 10:
  print('You dont have enough credits :(')
else:
  print('You dont have height or credits :(')
