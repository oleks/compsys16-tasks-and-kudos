import statistics

def show_turnaround(completion, arrival):
  turnaround = []
  for name, arr in arrival.items():
    turnaround.append(completion[name] - arr)
  print("Turnaround: {} +/- {}".format(
    statistics.mean(turnaround), statistics.stdev(turnaround)))

def show_response(firstrun, arrival):
  response = []
  for name, arr in arrival.items():
    response.append(firstrun[name] - arr)
  print("Response: {} +/- {}".format(
    statistics.mean(response), statistics.stdev(response)))
