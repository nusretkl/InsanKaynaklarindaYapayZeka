from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Model ve encoder'ları yükle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/tahmin', methods=['POST'])
def tahmin():
    education = request.form['education']
    experience = int(request.form['experience'])
    certifications = request.form['certifications']
    skills = request.form.getlist('skills')
    projects = int(request.form['projects'])
    job_role = request.form['job_role']
    salary = float(request.form['salary'])

    cert_binary = 1 if certifications == 'Evet' else 0
    skill_count = len(skills)

    # AI skorunu hesapla
    ai_score = (experience * 2 + projects * 1.5 + cert_binary * 5 + skill_count * 1) / 4
    ai_score = round(ai_score, 2)

    # Encode işlemleri
    try:
        edu_enc = encoders['education'].transform([education])[0]
    except:
        edu_enc = 0

    try:
        job_enc = encoders['job'].transform([job_role])[0]
    except:
        job_enc = 0

    # Model girişi
    input_data = np.array([[experience, edu_enc, job_enc, salary, cert_binary, projects]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    skor = round(probability * 100, 2)

    sonuc = "İşe Alınabilir" if prediction == 1 else "Reddedildi"

    return render_template('index.html', prediction=sonuc, score=skor, ai_score=ai_score)

if __name__ == '__main__':
    app.run(debug=True)
