parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(matrix):
  state={}
  total_slots=0
  available_slots= 0
  occupied_slots= 0
  for i in matrix:
    for j in i:
      if j==2:
        total_slots+=1
        available_slots+=1
      elif j==1:
        occupied_slots+=1
        total_slots+=1
  state["total_slots"]=total_slots
  state["available_slots"]=available_slots
  state["occupied_slots"]=occupied_slots
  return state

print(get_parking_lot(parking_state))