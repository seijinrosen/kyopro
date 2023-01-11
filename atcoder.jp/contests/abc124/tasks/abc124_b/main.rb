# frozen_string_literal: true

gets
H = gets.split.map(&:to_i)

current = 0
ans = 0

H.each do |h|
  if current <= h
    current = h
    ans += 1
  end
end

p ans
