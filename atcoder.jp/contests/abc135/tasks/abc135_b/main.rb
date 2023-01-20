# frozen_string_literal: true

# @return [Array(Integer)]
def input_int_array
  gets.split.map(&:to_i)
end

N = gets.to_i
P = input_int_array

cnt = 0
P.each_with_index do |p, i|
  cnt += 1 if i + 1 != p
end

puts [0, 2].include?(cnt) ? 'YES' : 'NO'
