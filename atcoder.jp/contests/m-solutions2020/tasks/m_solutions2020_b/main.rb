# frozen_string_literal: true

a, b, c = gets.split.map(&:to_i)
K = gets.to_i

(K + 1).times do
  if a < b && b < c
    puts 'Yes'
    exit
  end

  if a >= b
    b *= 2
  elsif b >= c
    c *= 2
  end
end

puts 'No'
