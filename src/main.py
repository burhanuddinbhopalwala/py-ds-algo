
# * Algorithm
"""
TC in general:
    TC = T(n/2) + 1 = O(logn) => BS/DC
    TC = 2T(n/2) + 1 = O(n)
    TC = 2T(n/2) + O(n) = O(nlogn) => MS/QS/DC
    TC = T(n-1) + 1 = O(n**2) => Brute Force/DP
    TC = nT(n-1) + 1 = O(n.n!) => Backtracking
"""

# * Compiler
"""
Compiler:
HLL -> Preprocessing -> Compiler -> Loader/Linker -> a.out/exe
HLL -> Macro Expansion->Assembly lang->logical to physical memory
"""

# * Deadlock
"""
Deadlock:
    Deadlock is INF waiting.
    Starvation is long waiting.

Deadlock Solution:
    D&R
    Ignorance
    Avoidance
    Prevention

Critical section: part of code where race condition can occur.
Counting semaphore/Binary semaphore.
"""
