try :
    dct = {"name":"abc","gender":"F"}
    print(dct["age"])
except Exception as e:
    print(f"Exception occurred! key/value mismatch {e}")
    #print(msg)
finally :
    print("Execution complete")