# frozen_string_literal: true

# @return [Array(Integer)]
def input_int_array
  gets.split.map(&:to_i)
end

N, K = input_int_array
H = input_int_array

ans = H.sort.reverse.drop(K).sum

p ans
