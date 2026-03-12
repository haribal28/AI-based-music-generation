📌 Project Overview

This project focuses on generating music automatically using Recurrent Neural Networks (RNN) with LSTM architecture. The model learns musical patterns from MIDI files and generates new melodies based on the learned sequences. The system allows users to provide their mood and preferred instrument, and the model generates music accordingly.

This project demonstrates how deep learning can be applied to creative tasks such as music composition.

🚀 Features

Automatic music generation using RNN (LSTM)

MIDI dataset processing using music21 library

User input for emotion detection (happy, sad, relax)

Instrument selection (piano, guitar, violin)

Generates and saves AI-composed MIDI music

Built and tested using Google Colab

🛠 Technologies Used

Python

TensorFlow / Keras

RNN (LSTM)

Music21

NumPy

Google Colab

⚙️ How It Works

Collect MIDI music files as the dataset.

Extract musical notes and chords using the music21 library.

Convert notes into numerical sequences.

Train an LSTM-based RNN model to learn musical patterns.

Take user input for emotion and instrument type.

Generate a new sequence of musical notes.

Convert predicted notes into a MIDI file and save it.

📊 Algorithm

STEP 1: Load MIDI dataset and extract notes.
STEP 2: Convert notes into numerical values.
STEP 3: Create input-output sequences for training.
STEP 4: Build an LSTM-based RNN model.
STEP 5: Train the model using the dataset.
STEP 6: Accept user input for emotion and instrument.
STEP 7: Generate new musical sequences.
STEP 8: Convert predicted notes back to MIDI format.

🎯 Result

The system successfully generates musical sequences based on learned patterns from MIDI files. Users can provide mood and instrument preferences, and the model generates unique music accordingly. This demonstrates the ability of deep learning models to generate creative content such as music compositions.

📁 Project Structure
music-generation-rnn
│
├── model.py
├── app.py
├── requirements.txt
├── music_model.h5
└── dataset (MIDI files)
🔮 Future Improvements

Add more MIDI datasets for better music quality

Implement Transformer-based music generation

Build a web interface for real-time music generation

Add audio playback instead of only MIDI download
