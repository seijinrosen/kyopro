# frozen_string_literal: true

def leap?(year)
  return true if (year % 400).zero?
  return false if (year % 100).zero?

  (year % 4).zero?
end

day = gets.chomp
Y = gets.to_i

ans = case day
      when 'Monday'
        5
      when 'Tuesday'
        4
      when 'Wednesday'
        3
      when 'Thursday'
        2
      when 'Friday'
        1
      else
        0
      end

p ans
puts (leap? Y) && 'YES' || 'NO'
