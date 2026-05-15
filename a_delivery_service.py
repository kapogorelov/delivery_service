def calculate_min_platforms(weights: list[int], limit: int) -> int:
    """Вычисляет минимальное количество платформ для перевозки всех роботов."""
    if not weights:
        return 0
    weights = sorted(weights)
    left_pointer = 0
    right_pointer = len(weights) - 1
    platforms = 0
    while left_pointer <= right_pointer:
        if weights[left_pointer] + weights[right_pointer] <= limit:
            left_pointer += 1
        right_pointer -= 1
        platforms += 1
    return platforms


def main() -> None:
    weights = [int(weight) for weight in input().split()]
    limit = int(input())
    print(calculate_min_platforms(weights, limit))


if __name__ == '__main__':
    main()
