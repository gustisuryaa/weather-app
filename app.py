from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        
        api_key = "ecdd441763474b80c5d083f96dd24af4" 
        
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        
        response = requests.get(url)
        
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'Waduh, nama kotanya nggak ketemu nih!'}
            
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)