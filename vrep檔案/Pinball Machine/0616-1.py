import vrep
import sys, math
import keyboard
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
  
vrep.simxFinish(-1)
  
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV = 360  
n=1
U_KickBallVel = (math.pi/180)*KickBallV
D_KickBallVel = -(math.pi/180)*KickBallV
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

errorCode,mov_handle=vrep.simxGetObjectHandle(clientID,'mov',vrep.simx_opmode_oneshot_wait)
errorCode,lrev_handle=vrep.simxGetObjectHandle(clientID,'lrev', vrep.simx_opmode_oneshot_wait)
errorCode,rrev_handle=vrep.simxGetObjectHandle(clientID,'rrev',vrep.simx_opmode_oneshot_wait)


#vrep.simxSetJointTargetVelocity(clientID,mov_handle,0,vrep.simx_opmode_oneshot_wait)
#vrep.simxSetJointTargetVelocity(clientID,lrev_handle,0,vrep.simx_opmode_oneshot_wait)
#vrep.simxSetJointTargetVelocity(clientID,rrev_handle,0,vrep.simx_opmode_oneshot_wait)

vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
#vrep.simxSetJointTargetVelocity(clientID,P1_handle,5,vrep.simx_opmode_oneshot_wait)
while True:
    try:
            if keyboard.is_pressed('a'): 
                vrep.simxSetJointTargetVelocity(clientID,lrev_handle,U_KickBallVel ,vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(clientID,lrev_handle,D_KickBallVel ,vrep.simx_opmode_oneshot_wait)
            if keyboard.is_pressed('l'):  
                vrep.simxSetJointTargetVelocity(clientID,rrev_handle,D_KickBallVel ,vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(clientID,rrev_handle,U_KickBallVel ,vrep.simx_opmode_oneshot_wait)
            if keyboard.is_pressed('up'):  
                vrep.simxSetJointTargetVelocity(clientID,mov_handle,1,vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(clientID,mov_handle,-1,vrep.simx_opmode_oneshot_wait)
                #pass
    except:
            break