
# initialize
Pattern = [
{ 'p': 1, 'x1': 0.0, 'x2': 0.0, 't': 0},
{ 'p': 2, 'x1': 0.5, 'x2': 0.0, 't': 0},
{ 'p': 3, 'x1': 0.5, 'x2': 0.5, 't': 0},
{ 'p': 4, 'x1': 1.0, 'x2': 0.5, 't': 1},
{ 'p': 5, 'x1': 0.0, 'x2': 1.0, 't': 1}
]
n = 1.0
w1 = 0.5
w2 = 0.5
theta = 0.5

# calculate
while(True):
  Flag = True
  for i in range(len(Pattern)):
    P = Pattern[i]
    s = w1*P['x1'] + w2*P['x2'] + theta
    s = 1 if s > 0 else 0
    if s != P['t']: #update
      w1 += n * P['x1'] * (P['t'] - s)
      w2 += n * P['x2'] * (P['t'] - s)
      theta += n * (P['t'] - s)
      Flag = False
  if Flag: break

#result
print("w1:", w1)
print("w2:", w2)
print("theta:", theta)
