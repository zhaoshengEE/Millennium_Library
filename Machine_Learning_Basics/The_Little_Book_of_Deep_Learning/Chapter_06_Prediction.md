# Chapter 6. Prediction


## Image Denoising

- `Denoising Autoencoder`: A model that takes a `degraded signal` $\tilde{X}$ as input and computes an estimate of the original one $X$


## Image Classification

- The standard model for this task is `CNN`, such as `ResNets` and `ViT`
- The model generates a vector of logits with as many dimensions as there are classes.


## Object Detection

- Each convolutionaly layer has the following output:
    - Estimated coordinates of the boundbox $(\tilde{x_{1}}, \tilde{x_{2}}, \tilde{y_{1}}, \tilde{y_{2}})$
    - Confidence score.
    - Logits for the $C$ classes of interest $+ 1$ additional "no object" class.


## Semantic Segmentation

- The finest-grain prediction task for image understanding.
- Predict, for every pixel, the class of the object to which it belongs.


## Speech Recognition

- The simple and recent model to solve this is a `sequence-to-sequence translation` $+$ a standard `attention-based transformer`.
- This task consists of multiple objectives:
    - Transcription of English or non-English text.
    - Translation from any language to English.
    - Detection of non-speech sequences, such as background music and ambient noise.
- Procudures:
    - Convert the sound signal into a `spectrogram`, which is a one-dimenional series $T \times D$ and encodes a vector of engeries in $D$ frequency bands at every time step.
    - The associated text is encoded with the `Byte-Pair Encoding (BPE) tokenizer`.
    - Process the `spectrogram` through a few 1D convolutional layers, generating feature representations.
    - Feed the representations into the `encoder` of the `transformer`, and the `decoder` generates a discrete sequence of tokens.


## Text-Image Representations

- A powerful approach to image understanding consists of learning consistent image and text representations.
- The `Contrastive Language-Image Pre-training (CLIP)` combines an `image encoder` (which is a ViT), and a `text encoder` (which is a GPT).

