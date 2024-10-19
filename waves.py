import numpy as np 
import matplotlib.pyplot as plt
import random

NMAX = 10
A = 1.0
F = lambda x: x**2
M = 9.11e-31 # massa elettrone
H_BAR = 1.05e-34 # costante planck / 2 pi

'''
il programma si articola in tre passaggi: 

1. definire i coefficienti "d_n" come l'integrale tra 0 e "a" del prodotto tra una funzione phi_n predefinita e f(x)
2. definire la funzione di cui voglio studiare l'evoluzione temporale, psi, come |sommatoria_n(d_n * phi_n * exp(-i * E_n * t / h_bar))|^2
3. plot di psi(x) in funzione di t

nota: n è un parametro naturale (n = 0, 1, 2, ...): ho scelto di fermarlo a 100
'''

# Funzione phi_n
def phi_n(x, n, a):
    return np.sin((n * np.pi * x) / a)

# Calcola l'integrale con metodo MC (per n fissato)
def monte_carlo_integral(n, a, f, num_samples):
    x_random = np.random.uniform(0, a, num_samples)
    phi_func = phi_n(x_random, n, a)
    integral_estimate = (a / num_samples) * np.sum(phi_func * f(x_random))
    return integral_estimate

# Calcola integrale per ogni n
def monte_carlo_for_ns(nMax, a, f, num_samples=10000): #num_samples = valori per la coordinata x
    results = []
    for n in range(1, nMax + 1):
        result = monte_carlo_integral(n, a, f, num_samples)
        results.append(result)
    return results

def E_n(n, h_bar, m, a):
    return (n**2 * np.pi**2 * h_bar**2) / (2 * m * a**2)

# Funzione di cui fare il plot
def psi(x, t, d_n, nMax, h_bar, m, a):
    psi_val = 0
    for n in range(1, nMax + 1): 
        energy_n = E_n(n, h_bar, m, a)
        phi_val = phi_n(x, n, a)
        psi_val += d_n[n-1] * phi_val * np.exp(-1j * energy_n * t / h_bar)
    return (abs(psi_val))**2

''' 
Secondo me la funzione psi non va bene perche': i d_n si calcolano con la funzione phi_n, ma nella funzione psi sto ricalcolando un'altra volta 
"phi_n" (riga 42) quando immagino che essa debba essere fissata. 
Dovrei salvare questo valore a ogni iterazione? Ma come faccio se phi_n e' una funzione di x? Non credo abbia senso nemmeno cosi'
'''

def main():

    dn_s = monte_carlo_for_ns(nMax, a, f)


    # Per ora fisso x e t come singoli valori, ma dovrei definire t come una coordinata temporale (np.linspace?)
    # Se no come faccio a fare il plot? 
    # x lo fisso a un singolo valore? 
    x_cord = np.linspace(0,A, 1000)
    t = 1
    psi_val = psi(x, t, dn_s, nMax, h_bar, m, a)

    # Stampa il risultato
    print(f"Valore di psi(x={x}, t={t}): {psi_val}")

    ''' 
    Per il plot: una volta nota psi(x, t) fisso x e plotto psi(t)
    '''
if __name__ == "__main__":
    main()
