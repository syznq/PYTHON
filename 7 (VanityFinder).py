import random
import re

# Chars to use / valid characters
LETTERS = "abcdefghijklmnopqrstuvwxyz0123456789"

def edits1(word):
    """
    Return a set of all strings one edit away from 'word'.
    Edits include deletion, transposition, replacement, and insertion.
    """
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in LETTERS]
    inserts = [L + c + R for L, R in splits for c in LETTERS]
    return set(deletes + transposes + replaces + inserts)

def generate_close_variants(base, count=30):
    """
    Generate variants that are 'super close' to the base by calculating all candidates
    with an edit distance of 1. If needed, expand to edit distance of 2.
    """
    base = base.lower()
    variants = set(edits1(base))
    variants.discard(base)
    
    if len(variants) < count:
        variants2 = set()
        for variant in variants:
            variants2.update(edits1(variant))
        variants2.discard(base)
        variants.update(variants2)
    
    variants_list = list(variants)
    random.shuffle(variants_list)
    return variants_list[:count]

def make_valid_invite(candidate: str) -> str:
    candidate = candidate.strip()                       
    candidate = re.sub(r"[^A-Za-z0-9-]", "", candidate)
    return f"https://discord.gg/{candidate.lower()}"

def main():
    base = "soul" # What vanity would you like to find?
    desired_count = 30  # How many you want to generate
    variants = generate_close_variants(base, count=desired_count)
    valid_invites = [make_valid_invite(variant) for variant in variants]

    header = f"**Custom Discord Invite Variants for `{base}`:**"
    divider = "────────────────────────────"
    lines = [header, divider]

    for idx, invite in enumerate(valid_invites, start=1):
        lines.append(f"`{idx:2}.` {invite}")

    message = "\n".join(lines)
    print(message)

if __name__ == "__main__":
    main()