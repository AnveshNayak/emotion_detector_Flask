import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    # return formatted_response

    res = {}

    res['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
    res['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    res['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
    res['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
    res['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    maxi = 0    
    for i,j in res.items():
        if j > maxi:
            dominant_emotion = i
            maxi = j

    res['dominant_emotion'] = dominant_emotion
    return res 
    
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    
    formatted_response = json.loads(response.text)
    # return formatted_response

    res = {}

    res['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
    res['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    res['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
    res['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
    res['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    maxi = 0    
    for i,j in res.items():
        if j > maxi:
            dominant_emotion = i
            maxi = j

    res['dominant_emotion'] = dominant_emotion
    return res 
    

