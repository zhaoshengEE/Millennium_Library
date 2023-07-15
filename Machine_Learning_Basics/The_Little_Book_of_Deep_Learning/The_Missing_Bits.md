# The Missing Bits


## Autoencoder

- A model that maps an input signal, possibly of high dimension, to a low-dimension latent representation, and then maps it back to the original signal, ensuring that information has been preserved.
- `Variational Autoencoder (VAE)` is a generative model with a similar structure.

### Variational Autoencoder (VAE)

- VAE is used for `anomaly detection`
    - VAE is trained on a dataset of normal data
    - Later, VAE is used to identify instances that deviate from normal data
- A part of several other `Generative AI` models


## Generative Adversarial Network (GAN)

- `Generator` and `Discriminator` work together in a competition to improve the `Generator`'s ability ot create realistic data.


## Reinforcement Learning

- A model to estimate an `accumulated long-term reward` given `action choices` and an `observable state`, and what actions to choose to maximize that reward.


## Fine-Tuning

- An approach to `transfer learning` in which the weights of a `pre-trained` model are trained on new data.
- `Fine-tuning` can be done on the entire neural network, or on only a subset of its layers, in which case the layers that are not being fine-tuned are `frozen`


## Graph Neural Networks (GNN)

- A model to process signals that are naturally structured as `graphs`, instead of `grid`.
- Each layer computes `activations` at each `vertex` by linearly combining the `activations` located at its immediate neighboring vertices.
- This operation is similar to a standard `convolution`, except the data structure does not reflect any geometrical information associated with the feature vectors they carry.


## Self-Supervised Learning

- Mitigate the over-dependence on labeled data
- Take advantage of unlabeled data and obtain useful representations that can help with downstream learning tasks.
- For example, even though `GPT` is trained to predict the next word, the model is able to solve various tasks, such as
    - Identifying the grammatical role of a word.
    - Answering questions.
    - Translating from one language to another.
    