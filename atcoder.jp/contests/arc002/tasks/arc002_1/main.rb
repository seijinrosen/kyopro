# frozen_string_literal: true

Y = gets.to_i

def leap?(year)
  return true if (year % 400).zero?
  return false if (year % 100).zero?

  (year % 4).zero?
end

puts (leap? Y) && 'YES' || 'NO'
