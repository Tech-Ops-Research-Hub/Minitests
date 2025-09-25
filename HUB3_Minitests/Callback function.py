def fetch_data(callback):
    #Simulate async operation (e.g fetching data)
    import time
    time.sleep(1)  # Simulate delay
    data = "Some data"
    callback(data) # Call the callback function with the results 
    
def handle_data(data):
    print(f"Received: {data}")
    
#pass handle_data as a callback function
fetch_data(handle_data)

#Output after 1 second: Received: Some data
    
    