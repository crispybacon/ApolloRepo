#!/usr/bin/env python
#Read the Universal Decleration of Human Rights
import nltk
from nltk.corpus import udhr
from AppKit import NSSpeechSynthesizer
voice="com.apple.speech.synthesis.voice.Boing"
speech=NSSpeechSynthesizer.alloc().initWithVoice_(voice)
raw_rights=nltk.corpus.udhr.words('English-Latin1')[:]
rights=' '.join(raw_rights)
speech.startSpeakingString_(rights)
