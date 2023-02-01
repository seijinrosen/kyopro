# frozen_string_literal: true

a, b, K = gets.split.map(&:to_i)

def func(x, y)
  x -= 1 if x.odd?

  tmp = x / 2
  x -= tmp
  y += tmp

  [x, y]
end

K.times do |i|
  if i.even?
    a, b = func a, b
  else
    b, a = func b, a
  end
end

puts "#{a} #{b}"
