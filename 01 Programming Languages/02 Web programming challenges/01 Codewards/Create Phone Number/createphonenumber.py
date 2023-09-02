def create_phone_number(n):
        #your code here
            return f'({"".join(str(n) for n in n[0:3])}) {"".join(str(n) for n in n[3:6])}-{"".join(str(n) for n in n[6:])}'
