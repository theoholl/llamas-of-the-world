class CreditCardValidator:
    def validate_card_number(card_number: str) -> bool:
        """This function validates a credit card number."""
        # 1. Change datatype to list[int]
        card_number = [int(num) for num in card_number]

        # 2. Remove the last digit:
        checkDigit = card_number.pop(-1)

        # 3. Reverse the remaining digits:
        card_number.reverse()

        # 4. Double digits at even indices
        card_number = [num * 2 if idx % 2 == 0
                    else num for idx, num in enumerate(card_number)]

        # 5. Subtract 9 at even indices if digit is over 9
        # (or you can add the digits)
        card_number = [num - 9 if idx % 2 == 0 and num > 9
                    else num for idx, num in enumerate(card_number)]

        # 6. Add the checkDigit back to the list:
        card_number.append(checkDigit)

        # 7. Sum all digits:
        checkSum = sum(card_number)

        # 8. If checkSum is divisible by 10, it is valid.
        return checkSum % 10 == 0

    def validate_cardholder_name(name: str) -> bool:
        """This function validates a cardholder name."""
        if len(name) < 1 or len(name) > 30:
            return False
        return True

    def validate_cvv(cvv: str) -> bool:
        """This function validated the card cvv"""
        if len(cvv) == 3 and cvv.isnumeric() and int(cvv) < 100:
            return True
        return False