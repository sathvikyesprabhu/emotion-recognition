import pyedflib
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
import re
import xml.etree.ElementTree as ET

# Maps
video_emotion_map = {
    '69.avi': 'disgust',
    '55.avi': 'anger',
    '58.avi': 'amusement',
    'earworm_f.avi': 'disgust',
    '53.avi': 'amusement',
    '80.avi': 'joy',
    '52.avi': 'amusement',
    '79.avi': 'joy',
    '73.avi': 'fear',
    '90.avi': 'joy',
    '107.avi': 'fear',
    '146.avi': 'sadness',
    '30.avi': 'fear',
    '138.avi': 'sadness',
    'newyork_f.avi': 'neutral',
    '111.avi': 'sadness',
    'detroit_f.avi': 'neutral',
    'cats_f.avi': 'joy',
    'dallas_f.avi': 'neutral',
    'funny_f.avi': 'joy'
}

emotion_number_map = {
    'neutral': 0,
    'anger': 1,
    'disgust': 2,
    'fear': 3,
    'joy': 4,
    'sadness': 5,
    'surprise': 6,
    'scream': 7,
    'bored': 8,
    'sleepy': 9,
    'unknown': 10,
    'amusement': 11,
    'anxiety': 12
}


def construct(dataset_root):
    # Read file names
    dataset_path = Path(dataset_root)
    dataset_dirs = sorted(os.listdir(dataset_root), key=int)
    dataset_dirs = [dataset_path / dataset_dir for dataset_dir in dataset_dirs]

    dataset = []

    bdf_file_pattern = re.compile(r'Part_(?P<subject>\d+)_S_Trial(?P<trial>\d+)_emotion')

    for dataset_dir in dataset_dirs:
        bdf_file = list(dataset_dir.glob("*.bdf"))
        if bdf_file:
            bdf_file = bdf_file[0]
            print(bdf_file.stem)
            session_file = list(dataset_dir.glob("*.xml"))[0]

            # Read signal
            f = pyedflib.EdfReader(str(bdf_file))
            sigbufs = np.zeros((4, f.getNSamples()[0]))
            sigbufs[0, :] = f.readSignal(32)
            sigbufs[1, :] = f.readSignal(33)
            sigbufs[2, :] = f.readSignal(34)
            sigbufs[3, :] = f.readSignal(46)

            # Read metadata
            m = bdf_file_pattern.match(bdf_file.stem)
            subject = m.groups()[0]
            trial = m.groups()[1]

            # Read labels
            root = ET.parse(session_file).getroot()

            # Append to dataset
            dataset.append({
                'ECG1': sigbufs[0],
                'ECG2': sigbufs[1],
                'ECG3': sigbufs[2],
                'status': sigbufs[3],
                'label': [int(emotion_number_map[video_emotion_map[root.attrib['mediaFile']]])],
                'metadata': {
                    'feltEmo': int(root.attrib['feltEmo']),
                    'feltArsl': int(root.attrib['feltArsl']),
                    'feltVlnc': int(root.attrib['feltVlnc']),
                    'feltCtrl': int(root.attrib['feltCtrl']),
                    'feltPred': int(root.attrib['feltPred']),
                    'subject': subject,
                    'trial': trial
                }
            })
    return dataset


if __name__ == "__main__":
    test_dataset_root = '/Users/Russel/myProjects/emotion-recognition/code/datasets/mahnob_hci/Sessions/'
    test_dataset = construct(test_dataset_root)
    print(len(test_dataset))
    print(test_dataset[0].keys())

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(test_dataset[4]['ECG1'][:-250])
    ax[1].plot(test_dataset[4]['status'][:-250])
    plt.show()
