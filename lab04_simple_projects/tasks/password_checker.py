class PasswordChecker:
    """Задача: password_checker"""

    def __init__(self, pwd: str):
        self.pwd = pwd

    def is_strong(self) -> bool:
        """Длина >= 8 и есть цифра"""
        if len(self.pwd) >= 8:
            for char in self.pwd:
                if char.isdigit():  # ✅ Проверяем, является ли символ цифрой
                    return True

    return False
