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

![image](https://user-images.githubusercontent.com/113716137/228567629-7b37b8b4-12da-4374-b21e-f2a7495660ed.png)
![image](https://user-images.githubusercontent.com/113716137/228567891-08b07243-c142-4e7f-b107-c4827b1ce91b.png)
![image](https://user-images.githubusercontent.com/113716137/228567200-f1b37498-9511-4de0-b510-78f3e4343912.png)
![image](https://user-images.githubusercontent.com/113716137/228567268-50b1119b-8675-4d11-944f-13254996d8c8.png)
![image](https://user-images.githubusercontent.com/113716137/228567321-619abb31-1cba-4519-84ed-3c58a4d18670.png)
![image](https://user-images.githubusercontent.com/113716137/228567387-e7afdf97-0ca9-408f-8ff0-eede1229b489.png)
![image](https://user-images.githubusercontent.com/113716137/228567450-41e3f8aa-e1e0-4782-b60d-28bd89116576.png)
![image](https://user-images.githubusercontent.com/113716137/228567494-61763c89-2b81-443e-a245-5c627101e1c5.png)
![image](https://user-images.githubusercontent.com/113716137/228567549-0fcaf179-ca94-444e-9fc8-f86a83629708.png)


