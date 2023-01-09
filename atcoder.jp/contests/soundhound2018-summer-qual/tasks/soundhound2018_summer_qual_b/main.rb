# frozen_string_literal: true

S = gets.chomp
w = gets.to_i

ans = ''
0.step(S.size - 1, w) do |i|
  ans += S[i]
end

puts ans
