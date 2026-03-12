import numpy as np
import tensorflow as tf
from music21 import note, stream

model = tf.keras.models.load_model("music_model.h5")

def generate_music(seed):

    seed_notes = seed.split()

    pattern = [0]*20   # simple seed pattern

    prediction_output = []

    for i in range(50):

        prediction_input = np.reshape(pattern,(1,len(pattern),1))

        prediction = model.predict(prediction_input,verbose=0)

        index = np.argmax(prediction)

        prediction_output.append(index)

        pattern.append(index)
        pattern = pattern[1:]

    output_notes = []

    for p in prediction_output:
        new_note = note.Note(int(p))
        output_notes.append(new_note)

    midi_stream = stream.Stream(output_notes)

    midi_stream.write("midi","generated_music.mid")

    return "generated_music.mid"