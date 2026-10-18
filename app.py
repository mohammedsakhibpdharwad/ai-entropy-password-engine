import string
import secrets
import math
from colorama import Fore, Style, init

# Initialize colorama for clean terminal output
init(autoreset=True)

class AIPasswordEngine:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def generate_password(self, length=16, use_upper=True, use_digits=True, use_symbols=True):
        """Generates a cryptographically secure random password."""
        char_pool = self.lowercase
        if use_upper:
            char_pool += self.uppercase
        if use_digits:
            char_pool += self.digits
        if use_symbols:
            char_pool += self.symbols

        if length < 8:
            raise ValueError("Password length should be at least 8 characters for basic security.")

        # Ensure at least one character from each selected category is present
        password = []
        if use_upper:
            password.append(secrets.choice(self.uppercase))
        if use_digits:
            password.append(secrets.choice(self.digits))
        if use_symbols:
            password.append(secrets.choice(self.symbols))

        # Fill the remaining length
        while len(password) < length:
            password.append(secrets.choice(char_pool))

        # Shuffle to eliminate predictable category placement
        secrets.SystemRandom().shuffle(password)
        return "".join(password)

    def evaluate_strength(self, password):
        """
        AI-inspired security assessment combining Shannon Entropy calculations 
        and pattern analysis.
        """
        pool_size = 0
        if any(c in self.lowercase for c in password):
            pool_size += 26
        if any(c in self.uppercase for c in password):
            pool_size += 26
        if any(c in self.digits for c in password):
            pool_size += 10
        if any(c in self.symbols for c in password):
            pool_size += len(self.symbols)

        if pool_size == 0 or len(password) == 0:
            return 0, "Invalid Password", "Password cannot be empty."

        # Calculate entropy: E = L * log2(R)
        entropy = len(password) * math.log2(pool_size)

        # AI heuristic feedback
        if entropy < 36:
            rating = f"{Fore.RED}Very Weak{Style.RESET_ALL}"
            advice = "Can be cracked almost instantly. Increase length and add numbers/symbols."
        elif entropy < 60:
            rating = f"{Fore.YELLOW}Weak{Style.RESET_ALL}"
            advice = "Vulnerable to targeted brute-force attacks. Recommend at least 14+ characters."
        elif entropy < 80:
            rating = f"{Fore.CYAN}Moderate{Style.RESET_ALL}"
            advice = "Good for standard accounts. Consider lengthening for critical credentials."
        else:
            rating = f"{Fore.GREEN}Strong (AI Approved){Style.RESET_ALL}"
            advice = "Excellent cryptographic randomness! Extremely safe against brute-force attempts."

        return round(entropy, 2), rating, advice

def main():
    engine = AIPasswordEngine()
    
    print("=" * 60)
    print(f"{Fore.MAGENTA}AI PASSWORD GENERATOR & ENTROPY ENGINE{Style.RESET_ALL}")
    print("=" * 60)

    try:
        length = int(input("\nEnter password length (default 16): ") or "16")
    except ValueError:
        length = 16

    password = engine.generate_password(length=length)
    entropy, rating, advice = engine.evaluate_strength(password)

    print("\n------------------------------------------------------------")
    print(f"Generated Password : {Fore.WHITE}{Style.BRIGHT}{password}{Style.RESET_ALL}")
    print(f"Entropy Score      : {entropy} bits")
    print(f"Strength Rating    : {rating}")
    print(f"AI Feedback        : {advice}")
    print("------------------------------------------------------------\n")

if __name__ == "__main__":
    main()
