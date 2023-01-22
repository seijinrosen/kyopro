# frozen_string_literal: true

# @return [Array(Integer)]
def input_int_array
  gets.split.map(&:to_i)
end

N = gets.to_i
A = input_int_array

ans = A.max - A.min

p ans
