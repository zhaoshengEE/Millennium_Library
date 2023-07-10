# Chapter 2. Efficient Computation

- GPUs have been equipped with dedicated sub-components referred to as `tensor cores`.
- Google developed deep-learning specialized chips -- `Tensor Processing Units (TPU)`.
- The limiting factor is usually not the number of computing units but the `read-write operations to memory`.
- `Tensor`: A series of scalars arranged along several discrete axes.
    - The implementation of tensors eliminates the storage of shape representation coefficients in memory.
    - This allows many reshaping, transposing, and extraction operations to be done without coefficient copying, hence extremely rapidly.