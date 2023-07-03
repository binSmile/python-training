# Technical Specification: Computing Fourier Series Coefficients

## Introduction

This specification describes the development of a program to calculate the Fourier series coefficients of the function $$f(x) = \frac{\sin(x)}{\sin(x) + 2}$$ over the interval [-π, π]. The `scipy.integrate.quad` function will be used for calculating the definite integral.

## Requirements

### Input
- A number `n`, 0 < `n` < 100, representing the number of Fourier series coefficients to be computed.

### Output
- The values of the Fourier series coefficients `a_n` in the first line.
- The values of the Fourier series coefficients `b_n` in the second line.

## Main Components

### 1. Input Data
- The program should accept input from the standard input (keyboard).
- Check that the entered number `n` meets the conditions of the problem (0 < `n` < 100).
- If the conditions are not met, output an appropriate error message.

### 2. Compute Coefficients
- Using the Fourier series formulas:
    - $$a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)dx$$
    - $$a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos(nx)dx$$
    - $$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin(nx)dx$$
- Compute the coefficients `a_0`, `a_n` and `b_n` for `n` using the `scipy.integrate.quad` function.

### 3. Output Data
- Output the values of `a_0`, `a_n` and `b_n` to the standard output (console).
- Output format:
    - First line output the values of `a_n` separated by spaces.
    - Second line output the values of `b_n` separated by spaces.

### 4. Error Handling
- Handle any potential errors and exceptions that arise during computations (e.g., issues with integration).

## Technologies
- Programming Language: Python
- Library for integration computations: SciPy
