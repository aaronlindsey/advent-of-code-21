#!/usr/bin/env python3

def to_dec(list_of_binary):
    result = 0
    for i in range(len(list_of_binary)):
        result += list_of_binary[i] * 2 ** (len(list_of_binary) - 1 - i)
    return result


def oxygen_generator_criteria(sum_of_bits, bit_count):
    return sum_of_bits >= bit_count


def co2_scrubber_criteria(sum_of_bits, bit_count):
    return sum_of_bits < bit_count


def filter_on_bit_criteria(data, bit_criteria):
    candidates = data.copy()

    for i in range(len(candidates[0])):
        sum_of_bits = 0
        for candidate in candidates:
            sum_of_bits += candidate[i]

        if bit_criteria(sum_of_bits, len(candidates)/2):
            candidates = list(filter(lambda x: x[i] == 1, candidates))
        else:
            candidates = list(filter(lambda x: x[i] == 0, candidates))

        if len(candidates) == 1:
            break

    return to_dec(candidates[0])


# read the data as a 2-dimensional array
data = []
with open("input") as file:
    for line in file:
        stripped = line.rstrip()
        bits = []
        for i in range(len(stripped)):
            bits.append(int(stripped[i]))
        data.append(bits)

oxygen_rating = filter_on_bit_criteria(data, oxygen_generator_criteria)
co2_rating = filter_on_bit_criteria(data, co2_scrubber_criteria)

print(oxygen_rating * co2_rating)

