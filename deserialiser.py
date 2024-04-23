
#First and second arguments of incoming array is a command. The array itself is that of bulk strings.
def deserialize(arr):
    cmd = []
    lenArr = arr[1]
    arr = arr[4:]
    idx = 4
    for i in range(0, lenArr):
        lenMsg = arr[idx + 1]
        msg = arr[idx + 4 : idx + 4 + lenMsg]
        idx = idx + lenMsg + 5
        cmd.append(msg)
    #cmd is the list which contains the command and it's parameters
    return cmd


        
        