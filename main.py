# main.py
# Executa todos os algoritmos do laboratório sobre o MESMO vetor e mostra uma tabela comparativa.
# Uso: python3 main.py [N]     (padrão: N = 16384, potência de 2 por causa do Bitonic)
import os
import random
import sys
import time

from mergesort_paralelo import merge_sort_seq, parallel_merge_sort
from quicksort_paralelo import quicksort_seq, parallel_quicksort
from oddeven_sort_paralelo import odd_even_sort_seq
from bitonic_sort_paralelo import bitonic_sort


def medir(func, dados):
    t0 = time.perf_counter()
    resultado = func(dados.copy())
    return resultado, time.perf_counter() - t0


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 16_384
    if N & (N - 1):
        sys.exit("N deve ser potência de 2 (exigência do Bitonic Sort).")

    cores = os.cpu_count() or 4
    dados = [random.randint(1, 10_000_000) for _ in range(N)]
    esperado = sorted(dados)

    algoritmos = [
        ("MergeSort",  "Serial",   merge_sort_seq),
        ("MergeSort",  "Paralelo", lambda a: parallel_merge_sort(a, num_workers=cores)),
        ("QuickSort",  "Serial",   quicksort_seq),
        ("QuickSort",  "Paralelo", lambda a: parallel_quicksort(a, num_workers=cores)),
        ("Odd-Even",   "Serial",   odd_even_sort_seq),
        ("Bitonic",    "Serial",   bitonic_sort),
    ]

    print(f"=== COMPARATIVO DE ORDENAÇÃO (N = {N:,} | {cores} cores) ===\n")
    linhas = []
    base = None
    for nome, modo, func in algoritmos:
        res, t = medir(func, dados)
        if base is None:
            base = t  # MergeSort serial é a referência
        linhas.append((nome, modo, t, base / t if t > 0 else 0, res == esperado))

    cab = f"{'Algoritmo':<12}{'Modo':<10}{'Tempo (s)':>12}{'Speedup*':>11}{'Correto':>10}"
    print(cab)
    print("-" * len(cab))
    for nome, modo, t, s, ok in linhas:
        print(f"{nome:<12}{modo:<10}{t:>12.4f}{s:>10.2f}x{'sim' if ok else 'NAO':>10}")
    print("\n* Speedup em relação ao MergeSort serial.")

    assert all(l[4] for l in linhas), "Algum algoritmo ordenou incorretamente!"
