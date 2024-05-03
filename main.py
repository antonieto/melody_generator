import numpy as np
from typing import List
import sounddevice as sd

# Scale: Do, Re, Mi, Fa, Sol, La, Si

transitions = [
    [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7], # Do
    [0.5,0, 0.2, 0.1, 0.2, 0, 0], # Re 
    [0.5, 0.2, 0, 0.2, 0, 0.1, 0], # Mi
    [0, 0, 0, 0, 0.5, 0.5 ,0], # Fa
    [0.7, 0, 0, 0.2, 0, 0.1, 0], # Sol
    [0.5, 0.2, 0.2, 0, 0, 0, 0.1], # La
    [0.9, 1/60, 1/60, 1/60, 1/60, 1/60, 1/60], # Si
]
note_index = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
note_to_frequency = {
        'Do': 523.25,
        'Re': 587.33,
        'Mi': 659.25,
        'Fa': 698.46,
        'Sol': 783.99,
        'La': 880.00,
        'Si': 987.77,
}

def generate(start: int, iterations: int) -> List[int]:
    current = start
    result = []
    for _ in range(iterations):
        result.append(current)
        current = np.random.choice(len(transitions), p=transitions[current])
    return result


def play_tone(frequency, duration=1.0, sample_rate=44100, amplitude=0.5):
    # Generate time values
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Generate audio signal
    tone = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Play the audio signal
    sd.play(tone, sample_rate)
    
    # Wait for the audio to finish playing
    sd.wait()

def main():
    # Generate a sequence of notes
    sequence = generate(0, 12)
    for note in sequence:
        play_tone(note_to_frequency[note_index[note]], duration=0.5)

main()
