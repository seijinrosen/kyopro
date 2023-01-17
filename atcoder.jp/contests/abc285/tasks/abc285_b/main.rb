# frozen_string_literal: true

N = gets.to_i
S = gets.chomp.chars

(1...N).each do |i|
  l = 0

  (0...N - i).each do |k|
    break if S[k] == S[k + i]

    l += 1
  end

  p l
end
