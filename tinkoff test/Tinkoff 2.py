n, m, k = tuple(map(int, input().split()))


def calculate_checking_time(N, M, K):
    """N is the count of juniors,
       M is the count of seniors, and
     K is the number of seniors that need to check a code."""
    total_codes = N * K
    total_seniors = M
    max_checks_at_once = total_seniors // K
    remaining_checks = total_seniors % K
    total_minutes = 0
    if max_checks_at_once > 0:
        total_minutes += (total_codes // max_checks_at_once) * K
    if remaining_checks > 0:
        total_minutes += (total_codes // remaining_checks) + 1
    return total_minutes


print(calculate_checking_time(n, m, k))