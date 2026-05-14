def min_platforms(weights: list[int], limit: int) -> int:
    """Вычисляет минимальное количество платформ для перевозки всех роботов."""
    if not weights:
        return 0

    weights = sorted(weights)
    left = 0
    right = len(weights) - 1
    platforms = 0

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1

    return platforms

# Тут я писал дефку для тестирования, чтобы не отвлекаться
# на Контекст и тестировать по ходу дела.


def main():
    weights = list(map(int, input().strip().split()))
    limit = int(input().strip())
    print(min_platforms(weights, limit))


if __name__ == '__main__':
    # test()
    main()
