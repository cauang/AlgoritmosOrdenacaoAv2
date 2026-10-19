# Algoritmos de Ordenação Paralelos (Av2)

Laboratório de **Computação Paralela e Concorrente** (Aula 09): implementação e benchmark de algoritmos de ordenação paralelos em Python 3, usando o paradigma Fork-Join com `ProcessPoolExecutor`.

## Objetivos

- Entender o modelo **Fork-Join** e o custo de **IPC** (comunicação entre processos).
- Usar um **threshold** para alternar entre execução paralela e sequencial.
- Calcular **Speedup** (`S = T_serial / T_paralelo`) e **Eficiência** (`E = S / p × 100%`).

## Arquivos

| Arquivo | Descrição |
|---|---|
| `mergesort_paralelo.py` | MergeSort paralelo (dividir e conquistar) com threshold |
| `quicksort_paralelo.py` | QuickSort paralelo com particionamento em chunks |
| `oddeven_sort_paralelo.py` | Odd-Even Transposition Sort (fases par/ímpar) |
| `bitonic_sort_paralelo.py` | Bitonic Sort (rede de ordenação, N = 2^k) |
| `benchmark_ordenacao.py` | Suíte de benchmark: tempos, speedup e eficiência para vários N |

## Requisitos

- Python 3.8 ou superior (só biblioteca padrão, sem dependências).
- Opcional: VS Code com a extensão Python da Microsoft.

## Como executar

```bash
python3 mergesort_paralelo.py
python3 quicksort_paralelo.py
python3 oddeven_sort_paralelo.py
python3 bitonic_sort_paralelo.py
python3 benchmark_ordenacao.py
```

No Windows, use `python` no lugar de `python3`.

> Todos os scripts usam a guarda `if __name__ == '__main__':`, necessária para o `multiprocessing` não entrar em loop de spawn no Windows/macOS.

## Experimentos do roteiro

- **Sensibilidade ao tamanho (N):** edite a lista `tamanhos` em `benchmark_ordenacao.py` (10.000, 100.000, 500.000 e 2.000.000).
- **Ajuste do threshold:** com N = 1.000.000, altere `THRESHOLD` (100, 1.000, 10.000, 50.000 e 100.000) e registre o menor tempo.

## Resultados de exemplo (10 cores)

| N | Serial | Paralelo | Speedup | Eficiência |
|---|---|---|---|---|
| 10.000 | 0,017 s | 0,016 s | 1,02x | 10,2% |
| 100.000 | 0,202 s | 0,193 s | 1,05x | 10,5% |
| 500.000 | 1,178 s | 0,476 s | 2,48x | 24,8% |
| 2.000.000 | 5,908 s | 1,659 s | 3,56x | 35,6% |

Os valores variam conforme o hardware. Para N pequeno, o overhead de IPC anula o ganho. O paralelismo compensa a partir de centenas de milhares de elementos.

## Autor

Atividade da disciplina de Computação Paralela e Concorrente (UNIFOR), baseada no roteiro do Prof. Wellington Brito.
