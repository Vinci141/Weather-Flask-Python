#this is to demonstrate use of weather api in python with flask
from weather import Weather,Unit
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')
	 
@app.route('/weather',methods=['POST','GET'])
def weather():
     city=request.form['cityName']
     try:
         weather=Weather(unit=Unit.CELSIUS)
         location=weather.lookup_by_location(city)
         c=location.condition
         str=c.text
         return render_template('index.html',str=str)
         
     except:
          str="No Data Found"
          return render_template('index.html',str=str)
          

if __name__=='__main__':
    app.run(debug=True)
