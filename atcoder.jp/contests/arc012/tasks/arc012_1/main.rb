# frozen_string_literal: true

day = gets.chomp

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
