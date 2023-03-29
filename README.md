# Method Hoyne
## Solution of the Cauchy problem for a homogeneous first-order differential equation using the Hoyne method.

The Cauchy problem is posed for a first-order differential equation with initial conditions:

$$ y' = f(x,y); x \in [a,b]; y(a) = y_0 $$

The grid is being built

$$ (x_0 = a, x_n = b) \text{ on } [a,b] $$

Нit is necessary to find a numerical solution using the Hoyne method with a predetermined accuracy.  

$$ [a;b] \ y_a = y_0 \ y' = f(x,y), \epsilon $$

We divide our segment [a,b] into n parts. Getting the step value

$$ h = \frac{b - a}{n} $$

$$ y_{i+1} = y_i + \frac{h}{2}\left[f(x_i, y_i) + f(x_i + h, y_i + hf(x_i, y_i))\right] \text{, where } i = 0, 1, \dots, n $$

After we have obtained the corresponding y values, it is necessary to calculate the y values for the partition in increments of two times less. You can compare the obtained accuracy with the specified one as follows:

$$ \max(|y_{i, n} - y_{2i, 2n}|) < \epsilon \text{, where } i = 1, 2, \dots, 2^{n-1} $$

If the accuracy is achieved, then we remember the result for step h = 0.5h and exit the loop

Otherwise, if the accuracy is not achieved, then reduce the step twice again and perform this operation again.

The condition of applicability of the method:

$$ f(x,y) \in C([a;b]) $$
