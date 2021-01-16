#feature extraction
import numpy as np
import pandas as pd
#import parselmouth
#from parselmouth.praat import call
import pickle as pkl
import requests



def generateReport(voiceID, f0min, f0max, unit):
    sound = parselmouth.Sound(voiceID) # read the sound
    pitch = call(sound, "To Pitch", 0.0, f0min, f0max) #create a praat pitch object
    pulses = call([sound, pitch], "To PointProcess (cc)")
    report = parselmouth.praat.call([sound,pitch,pulses],"Voice report",0,0,75,600,1.3, 1.6,0.03,0.45)
    return report

def generateReports(audio_files,data_location):
    reports = []
    for i in audio_files:
        sound = parselmouth.Sound(data_location+i)
        reports.append(generateReport(sound, 75, 300, "Hertz"))
    return reports


def parse_report(report,column_list):
    params = {}
    for j in column_list:
        for item in report.split("\n"):
            if j in item:
                for t in item.split():
                    if t[-1] == '%':
                        t = t.replace('%','')
                    try:
                        temp = float(t)
                    except ValueError:
                        continue
                    params[j] = temp
    return params

def predict():
    """#load model
    url = 'https://github.com/djagathsingh/Parkinson/blob/main/summ_model.sav?raw=true'
    r = requests.get(url, allow_redirects=True)
    fp = open('summ_model.sav', 'wb').write(r.content)
    loaded_model = pkl.load(open('summ_model.sav', 'rb'))
    
    column_list = ['Jitter (local)','Jitter (local, absolute)','Jitter (rap)','Jitter (ppq5)','Jitter (ddp)','Shimmer (local)','Shimmer (local, dB)','Shimmer (apq3)','Shimmer (apq5)','Shimmer (apq11)','Shimmer (dda)','Mean autocorrelation',
                    'Mean noise-to-harmonics ratio','Mean harmonics-to-noise ratio','Median pitch','Mean pitch','Standard deviation','Minimum pitch','Maximum pitch','Number of pulses','Number of periods',
                    'Mean period','Standard deviation of period','Fraction of locally unvoiced frames','Number of voice breaks','Degree of voice breaks']
    
    mob_data_loc = '/storage/emulated/0/'
    
    audio_files = ['sustained_vowel_aaa1.wav','sustained_vowel_aaa2.wav','sustained_vowel_aaa3.wav','sustained_vowel_ooo1.wav','sustained_vowel_ooo2.wav','sustained_vowel_ooo3.wav']
    audio_len = len(audio_files)
    reports = generateReports(audio_files,mob_data_loc)
    
    X_to_predict = []
    
    for report in reports:
        param = parse_report(report,column_list)
        X_to_predict.append(np.array(list(param.values())).reshape(1,26))

    X_to_predict = np.array(X_to_predict).reshape(audio_len,26)
    df = pd.DataFrame(X_to_predict, columns = column_list)
    df = summarize_data(df,audio_len, column_list, audio_len)
    pred = loaded_model.predict(np.array(list(df.iloc[0,:])).reshape(1,182))[0]
    
    if pred == 1:
        return "You have parkinson's disease"
    else:
        return "You don't have parkinson's disease"
    """
    return "You don't have parkinson's disease"