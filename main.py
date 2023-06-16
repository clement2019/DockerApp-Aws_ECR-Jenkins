from flask import Flask

app=Flask(__name__)

@app.route("/")

def ping_server():
    print("Welcome to my blog, server running....")
    
@app.route("/reg")    
def registration(a=4,b=6):
    return "yes the addition =: " + str(a+b)
   
if __name__=="__main__":
     app.run(DEBUG=True, ports=5000)
        