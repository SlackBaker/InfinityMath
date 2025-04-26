from scipy.integrate import quad

def integrate_function(func, a, b):
    """
    Обчислює визначений інтеграл від функції func на проміжку [a, b].

    :param func: Функція, яку потрібно інтегрувати (має приймати одне число як аргумент).
    :param a: Нижня межа інтегрування.
    :param b: Верхня межа інтегрування.
    :return: Результат інтегрування та оцінка похибки.
    """
    result, error = quad(func, a, b)
    return result, error
