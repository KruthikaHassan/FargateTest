#!/usr/bin/python3
# import json package
import json

# define the dictionary 
parameters = {}

# define the filename
filename = 'task.json'

# read the json file
with open('task.json','r') as f:
	task_aws = json.load(f)

# extract the required task dictionary
task_dict = task_aws['tasks'][0]

# fields for docker image pull 
image_pull_start = task_dict['pullStartedAt']
image_pull_end = task_dict['pullStoppedAt']

# fields for tasks
task_pending_running = task_dict['startedAt']
task_transition_running_stop = task_dict['stoppedAt']
task_running_stopped =  task_dict['stoppingAt']
task_created = task_dict['createdAt']                      # task entered the PENDING state
task_execution_stop = task_dict['executionStoppedAt']      # task execution stopped
task_connectivity = task_dict['connectivityAt']
# cpu and memory
parameters['cpu_'] = task_dict['cpu']
parameters['memory_'] = task_dict['memory']

# print memory and cpu 
#print("Memory: ",memory_, " CPU: ",cpu_)

# print docker image pull times
#print("Docker image pull time: ", image_pull_end-image_pull_start)
parameters['DockerImagePullTime'] = image_pull_end - image_pull_start

# print task pending to running and provisioning to pending
#print("Time for task to transition from provisioning to pending and pending to running: ",task_pending_running - task_created)
parameters['ColdStartTime'] = (task_pending_running - task_created) 

# print task time taken to stop
#print("Execution stopped at: ", task_execution_stop)
#print("Task stopping at: ", task_running_stopped)
#print("Task stopped at: ", task_transition_running_stop)

# stopping time of the task
#print("Total time taken to stop: ", (task_transition_running_stop - task_running_stopped)+(task_running_stopped - task_execution_stop))
parameters['StoppingTime'] = (task_transition_running_stop - task_running_stopped)+(task_running_stopped - task_execution_stop)

# run time of the task
#print("Run time: ", task_execution_stop - task_pending_running)
parameters['RunningTime'] = task_execution_stop - task_pending_running

print(parameters)
