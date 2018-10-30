### simultanous translation (text input)
1. install `anaconda`
1. install `pytorch` and `torchtext`
    ```bash
    conda install pytorch==0.3 torchvision -c pytorch
    pip install torchtext==0.2.3
    pip install msgpack  # this package is required because one error message asked
    ```
    - to check pytorch:
    ```bash
    conda list | grep torch
    ```
    - to configure conda/python as default in zsh:
    ```bash
    echo 'export PATH="/Users/liukaibo/anaconda3/bin/conda:$PATH"' >> ~/.zshrc
    ```
1. install jieba for chinese segmentation
    ```bash
    pip install jieba
    # or pip3 install jieba
    ```
1. copy model files to local
1. to run the translator:
    ```bash
    python translate_stdIO.py -model w2_step_71000.pt
    ```


### stream audio input (google cloud api)(optional)
1. install google cloud speech api client library
    ```bash
    pip install --upgrade google-cloud-speech
    ```
    [online demo on google cloud](https://cloud.google.com/speech-to-text/)
1. install **PyAudio** for Microphone input (as above)
1. install googletrans for word-level translation (as above)
1. get google cloud key and add to **PATH**, described [here](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries)
1. install flask for web UI
	```bash
	pip install flask
	```
1. to run the translation demo with stream audio input:
    ```bash
    python flask_server_line_bulk.py -model w5_step_150000.pt
    ```
