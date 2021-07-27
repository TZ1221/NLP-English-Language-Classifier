class Instance:

    def __init__(self, line, preserve=False):

        if preserve:
            self.goal = None
            self.value = line
        else:
            self.goal = line[:2]
            self.value = line[2:]
        self.features = get_features(line)
        self.weight = None


def get_features(line):

    v_pairs, c_pairs = vow_con_pairs(line)
    words = set(line.split())

    return {
        "cv-ratio": vow_con_ratio(line),
        "av-len": avg_word_len(line),
        "v-pairs": v_pairs,
        "c-pairs": c_pairs,
        "l-pairs": letter_pairs(line),
        "ends-en": ends_in("en", line),
        "ends-e": ends_in("e", line),
        "has-aa": "aa" in line,
        "has-ee": "ee" in line,
        "has-word-het": "het" in words,
        "has-word-een": "een" in words,
        "has-word-en": "en" in words,
        "has-word-de": "de" in words,
        "has-word-the": "the" in words,
        "has-word-and": "and" in words,
        "has-word-in": "in" in words,
        "has-word-of": "of" in words,
    }


def ends_in(suffix, line):

    line = line.split()

    for word in line:
        if len(word) < len(suffix):
            continue

        i = len(word) - len(suffix)
        val = True

        for ch in suffix:
            if word[i] != ch:
                val = False
                break

            i += 1

        if val:
            return val

    return False


def letter_pairs(line):

    pair_count = 0

    for i in range(len(line) - 1):
        ch = line[i]
        next_ch = line[i + 1]

        if ch == next_ch:
            pair_count += 1

    return pair_range(pair_count)


def vow_con_pairs(line):

    vowels = {"a", "e", "i", "o", "u"}
    v_count = c_count = i = 0

    while i < len(line) - 1:
        ch = line[i]
        next_ch = line[i + 1]

        if ch in vowels and ch == next_ch:
            v_count += 1
            i += 2
        elif ch == next_ch:
            c_count += 1
            i += 2
        else:
            i += 1

    return pair_range(v_count), pair_range(c_count)


def pair_range(pair_count):

    range1 = 0, 3
    range2 = 4, 7
    range3 = 8, 10
    range4 = 10, None

    if pair_count <= range1[1]:
        return range1
    if range2[0] <= pair_count <= range2[1]:
        return range2
    if range3[0] <= pair_count <= range3[1]:
        return range3

    return range4


def avg_word_len(line):

    total = 0
    range1 = 0, 4
    range2 = 5, 8
    range3 = 8, None

    for _ in line:
        total += 1

    avg = total//len(line.split())

    if avg <= 4:
        return range1

    if 4 < avg <= 8:
        return range2

    return range3


def vow_con_ratio(line):

    vowels = {"a", "e", "i", "o", "u"}
    v_count = c_count = 0
    range1 = 0, 0.5
    range2 = 0.51, 0.69
    range3 = 0.7, None

    for ch in line:
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
    
    ratio = v_count/c_count

    if ratio <= range1[1]:
        return range1

    if range1[1] < ratio < range3[0]:
        return range2

    return range3
