# GitLab Flavored Markdown (GLFM)
https://docs.gitlab.com/user/markdown

### \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)


### $\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$

###  $\int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}$


Symbol	            Script

### $k_{n+1}$	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; k_{n+1}

### $n^2$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^2

### $k_n^2$	&nbsp;&nbsp;&nbsp;&nbsp; k_n^2

### $u_n(l)$ &nbsp;&nbsp;&nbsp;&nbsp; u_n(l)

### $\frac{n!}{k!(n-k)!}$	&nbsp;&nbsp;&nbsp;&nbsp; \frac{n!}{k!(n-k)!}

### $\binom{n}{k}$ &nbsp;&nbsp;&nbsp;&nbsp; \binom{n}{k}

### $\frac{\frac{x}{1}}{x - y}$	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \frac{\frac{x}{1}}{x - y}

### $^3/_7$	 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ^3/_7

### $\dfrac{dT}{dl} = F(l)$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \dfrac{dT}{dl} = F(l)

### I'm a markdown file.

### $I = \int \rho R^{2} dV$

### $\sum_{p \in P} (t_{p,last} - t_{p,first} - \sum_{i \in Proc_p} d_i)$	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\sum_{p \in P} (t_{p,last} - t_{p,first} - \sum_{i \in Proc_p} d_i)$

## Множества и параметры
- \(P\) — множество пациентов.  
- \(R\) — множество процедур.  
- \(S_r\) — множество доступных временных слотов для процедуры \(r \in R\). Каждый слот задаётся как \((start_{rs}, end_{rs})\).  
- \(d_r\) — фиксированная длительность выполнения процедуры \(r\).  
- \(R_p \subseteq R\) — множество процедур, предписанных пациенту \(p \in P\).

---

## Переменные
- \(x_{prs} \in \{0,1\}\) — равно 1, если пациент \(p\) выполняет процедуру \(r\) в слоте \(s \in S_r\), иначе 0.  
- \(t_{pr}\) — время начала процедуры \(r\) у пациента \(p\).  

---

## Ограничения
1. **Все процедуры пациента должны быть выполнены:**  
   \[
   \sum_{s \in S_r} x_{prs} = 1, \quad \forall p \in P, \, r \in R_p
   \]

2. **Процедуры занимают только допустимые слоты:**  
   \[
   t_{pr} \geq start_{rs} \cdot x_{prs}, \quad 
   t_{pr} + d_r \leq end_{rs} \cdot x_{prs}, 
   \quad \forall p, r, s
   \]

3. **Одна процедура в слоте выполняется только одним пациентом:**  
   \[
   \sum_{p \in P} x_{prs} \leq 1, \quad \forall r \in R, \, s \in S_r
   \]

4. **Пациент не может выполнять несколько процедур одновременно:**  
   \[
   [t_{pr}, \, t_{pr}+d_r] \cap [t_{pr'}, \, t_{pr'}+d_{r'}] = \emptyset, 
   \quad \forall p \in P, \, r \neq r'
   \]

---

## Функция цели
Минимизировать суммарное время ожидания пациентов между процедурами:  

\[
\min \sum_{p \in P} \sum_{\substack{r, r' \in R_p \\ r \neq r'}} 
\big| t_{pr'} - (t_{pr} + d_r) \big|_{+}
\]

где \(|x|_{+} = \max(0, x)\), то есть учитывается только ожидание между последовательными процедурами.  
 

