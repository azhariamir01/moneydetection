function TTS(objects) {
    // combine all the information into a single string
    var message = objects.join('. ');

    // speech synthesis API
    var speechSynthesis = window.speechSynthesis;

    // new speech synthesis utterance
    var speechMsg = new SpeechSynthesisUtterance();

    // set the text and speak it using the synthesis API
    speechMsg.text = message;
    speechSynthesis.speak(speechMsg);
}