import numpy as np

# PART 1
# projectile travels downward at y = 0 with an extra unit of velocity, so the initial y must be 98
ymax = abs(-99) # maximum y distance
yf = sum([y for y in range(ymax)]) #
print(yf) 


# PART 2
xmin, xmax = 201, 230
ymin, ymax = -99, -65

valid_vi = []

# Find vxmin where final vx=0 exactly at xmin
vxmin = 0
while sum([i for i in range(vxmin+1)])<xmin:
    vxmin +=1
vxmax = xmax + 1

vymin = ymin
vymax = abs(ymin)

max_num_steps = (abs(ymin)+1)*2+1

for vxi in range(vxmin,vxmax):
    for vyi in range(vymin,vymax):
        #vxi and vyi must put the projectile in the target in the same number of steps
        for num_steps in range(1,max_num_steps+1):
            # xf decreases by 1 each step due to drag, but stops at vx=0
            xf = sum([int((vxi - t)*np.heaviside(vxi-t,0)) for t in range(num_steps)])
            # yf decreases by 1 each step due to gravity, and never stops
            yf = sum([int(vyi - t) for t in range(num_steps)])
            # Check if final position is within bounds
            if xf <= xmax and xf >= xmin and yf <= ymax and yf >= ymin:
                if [vxi,vyi] not in valid_vi:
                    valid_vi += [[vxi,vyi]]
                break

print(len(valid_vi))

    

