# K13 Overview 

K13 is a two state model, meaning that we have $S = \{*, \dagger\}$, giving us: 

$$\begin{aligned}
P(t,s) &= 
\begin{bmatrix}
p_{**}(t,s) & p_{*\dagger}(t,s)\\
0 & 1 
\end{bmatrix}
\;\;\text{and}\;\;
\Lambda(s) = 
\begin{bmatrix}
\mu_{**}(s) & \mu_{*\dagger}(s)\\
0 & 0
\end{bmatrix}\
\end{aligned}$$ 

Kolmogorov's backward equation: 
$$\begin{aligned}
\partial_{t}p_{ij}(t,s) &= 
\mu_{i}(t)p_{ij}(t,s) - \sum_{k \neq i}\mu_{ik}(t)p_{kj}(t,s) \\ 
&\Downarrow \\ 
\partial_{t}p_{**}(t,s) &= 
\mu_{*}(t)p_{**}(t,s)
\end{aligned}$$

From the fundamental theorem of calculus we have: 
$$\begin{aligned}
-\int_{t}^{s}\mu_{*}(u)du &= -[ M_{*}(s) - M_{*}(t)] \\ 
&= -M_{*}(s) +M_{*}(t) \\
&\Downarrow \\ 
\partial_{t}\left(-
\int_{t}^{s}\mu_{*}(u)du
\right)
&= 
\partial_{t}(M_{*}(t)) = \mu_{*}(t)
\end{aligned}$$ 

Using this we get: 
$$
p_{**}(t,s) = \exp\left(
-\int_{t}^{s}\mu_{*}(u)du
\right)
$$

The row sum of the intensity matrix $\Lambda$ sums to zero, furthermore we use the convention that $\mu_{i}(t) = - \mu_{ii}(t)$, this yields:
$$
p_{**}(t,s) = \exp\left(
-\int_{t}^{s}\mu_{*\dagger}(u)du
\right)
$$ 

Translating this to K13, where one also accounts for the calculation year $Y$, one gets:
$$\begin{aligned}
p_{**}^{x}(t,s) = p_{**}(x+t, x + s)
&= 
\exp\left(
-\int_{t}^{s}\mu_{Kol}(x+u, Y+u)du    
\right)
\end{aligned}$$